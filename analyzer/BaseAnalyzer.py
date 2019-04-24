


import logging, os
from antlr4 import *
from ..verilog.Unit import Unit
from ..VerpyError import *
from ..parser import VerexParser, VerexLexer
from .AnalyzerOption import AnalyzerOption
from .PreprocLexer import PreprocLexer
from .AnalyzerErrorListener import AnalyzerErrorListener

logger = logging.getLogger(__name__)
def debug(msg, *args): logger.debug(msg, *args)
def info(msg, *args): logger.info(msg, *args)
def warning(msg, *args): logger.warning(msg, *args)


def range2arr(ctx):
    ret = []
    if ctx != None:
        if ctx.msb != None :
            ret.append( [ctx.msb.getText(), ctx.lsb.getText()] )
        else :
            ret.append( [ctx.star.text] )
    return ret

def rexpr2arr(ctx):
    if ctx is None: return []
    if ctx.expression():
        return [ctx.expression().getText()]*2
    if ctx.msb_constant_expression():
        return [ctx.msb_constant_expression().getText(),
                ctx.lsb_constant_expression().getText()]
    if ctx.base_expression():
        b = ctx.base_expression().getText()
        if ctx.inckey:
            return [   b+'-1+'+ctx.width_constant_expression().getText(), b]
        else:
            return [b, b+'+1-'+ctx.width_constant_expression().getText()]
    else:
        return [ctx.star.text]*2

def dim2arr(ctx):
    ret = []
    if ctx != None:
        for d in ctx:
            if d.bit != None   :
                ret.append(d.bit.getText())
            elif d.msb != None :
                ret.append( [d.msb.getText(), d.lsb.getText()] )
            else :
                ret.append([ctx.star.text])
    return ret

#def initDefaultChild(s):
#    import re
#    nodes = {}
#    for c in s.split():
#        #if c[0] in ('>', '!', '?', '-'): continue
#        if c[:2] == '>>':
#            visit = 'visit' + c[2].upper() + c[3:]
#            nodes[visit] = 'visitChildren' # all grand
#        elif re.match(r'[a-z_]', c):
#            visit = 'visit' + c[0].upper() + c[1:]
#            nodes[visit] = 'visitChilds'    # only childs
#    return nodes

class VisitUnknownChild(Exception):
    pass

class BaseAnalyzer(ParseTreeVisitor):
    def __init__(self, strOpts=None, options=None,
            parser=None, lexer=None, defaultVisit=""):
        self._savedctx = {}
        self.opts = options or AnalyzerOption(strOpts)
        self.lexer = lexer or PreprocLexer(options=self.opts)
        self.tokens = CommonTokenStream(self.lexer)
        self.parser = parser or VerexParser(self.tokens)
        self.parser.buildParseTrees = True
        self.unit = Unit(options=self.opts)
        self.__initDefaultChilds(defaultVisit)

        self._contStack = []
        self.pushCont(self.unit)

        self.parser.removeErrorListeners()  # remove console log
        self.parser.addErrorListener(AnalyzerErrorListener())
        self.lexer.removeErrorListeners()  # remove console log
        self.lexer.addErrorListener(AnalyzerErrorListener())

    def initCont(self, mindeep=1):
        #_contStack = []
        while len(self._contStack) > mindeep: self._contStack.pop()
    def pushCont(self, cont):
        #debug("%sPush %s" % ("  "*len(_contStack), type(cont)))
        #print("%sPush %s" % ("  "*len(_contStack), type(cont)))
        self._contStack.append(cont)
        return cont
    def popCont(self):
        #debug("%sPop %s" % ("  "*(len(_contStack)-1), type(curCont())))
        #print("%sPop %s" % ("  "*(len(_contStack)-1), type(curCont())))
        try: return self._contStack.pop()
        except: raise InternalFatal("contStack overflow")
    def curCont(self):
        try: return self._contStack[-1]
        except: return None
    def lenCont(self):
        return len(self._contStack)

    def __initDefaultChilds(self, s):
        # NOTE : the first appear has higher priority
        import re
        for c in s.split():
            #if c[0] in ('>', '!', '?', '-'): continue
            if c[:2] == '>>':
                visit = 'visit' + c[2].upper() + c[3:]
                if not hasattr(self, visit):
                    self.__dict__[visit] = self.visitGrands
            elif re.match(r'[a-z_]', c):
                visit = 'visit' + c[0].upper() + c[1:]
                if not hasattr(self, visit):
                    self.__dict__[visit] = self.visitChilds # only childs

    # to explicit ignore a node, that hard because we need implement all
    # visitNode function to ignore
    # "accept" will find visitNode function of just run visitChildren
    # which travel all grand childs
    # Here's I modify this to use "access" as ignore that node

    ## default visit will go through all children & grand-child ...
    ## we only want to go to children
    #def visitChildren(self, node):
    #    debug("visitChildren %s" % type(node))
    #    super(BaseAnalyzer, self).visitChildren(node)

    def visitChildren(self, node):
        raise VisitUnknownChild()

    # let parent decide
    def raiseChild(self, node):
        try:
            return node.accept(super(type(self), self))   # this implement a hasattr(visitor, "visitNode")
            # in turn, it will call visitChildren if no function is found
        except VisitUnknownChild:
            return None



    # call this to accept all Grands instead
    def visitGrands(self, node):
        self.visitChilds(node, True)

    def visitChilds(self, node, recur=False):
        #self.visitChildren(node, False)
        n = node.getChildCount()
        debug("visitChilds %s : %d" % (type(node), n))
        for i in range(n):
            c = node.getChild(i)
            try:
                c.accept(self)
            except VisitUnknownChild:    # there's no define visit
                if recur:   # visit grands if required by default
                    self.visitChilds(c, True)
            #visit = 'visit' + type(c).__name__[:-7]
            #try:
            #    proc = getattr(self, visit)
            #except AttributeError, e:
            #    try:
            #        proc = getattr(self, self._visitChildNodes[visit])
            #    except KeyError, e:
            #        proc = None
            #if proc is not None:
            #    proc(c)

    def visitErrorNode(self, node):
        raise VerpySyntaxError("Parser failed: %s" % node)

    def addOptions(self, fstr):
        self.opts.addOpt(fstr)

    def removeModule(self, name):
        self.unit.removeModule(name)

    def findModule(self, name):
        return self.unit.findModule(name)

    def _parse(self, filename='', fromstr='', srcName='', entry=''):
        if filename:
            #info("Analyzing file '%s' ..." % filename)
            print("Analyzing file '%s' ..." % filename)
            istr = FileStream(filename)
            istr.name = srcName or ("<file: %s>" % os.path.basename(filename))
        elif fromstr:
            #info("Analyzing String for Rule '%s' ..." % entry)
            print("Analyzing String for Rule '%s' ..." % entry)
            istr = InputStream(fromstr)
            istr.name = srcName or "<input_str>"
        else:
            raise Exception("Either filename of fromstr must be specified")   

        curDeep = self.lenCont()
        #print("currentCont : %s" % type(curCont()))
        # reset token stream
        self.lexer.inputStream = istr
        self.tokens.setTokenSource(self.lexer)
        if not entry:
            entryFn = self.parser.vfile
        else:
            try:
                entryFn = getattr(self.parser,entry)
            except AttributeError:
                raise VerpyUserError("Parser %s doesnt have entry '%s'" %
                                     (type(self.parser), entry))
        tree = entryFn()
        self.visitChilds(tree)  # dont use visit or accept, it visit Grand
        # safe gaurd
        if self.lenCont() != curDeep:
            raise InternalFatal("Analyzing failed")

    # Top level analyze
    def analyze(self):
        self.initCont()
        for f in self.opts.unprocessedFiles():
            self._parse(filename=f)
            self.opts.processedFile(f)
        self.unit.link()
        return self.unit

    def analyzeFile(self, name, vunit=None, entry=''):
        if vunit: self.pushCont(vunit)
        f = self.opts.newFile(name)
        self._parse(filename=f.fullname, entry=entry)
        self.opts.processedFile(f.fullname)
        if vunit: self.popCont()

    def analyzeString(self, fstr, vunit=None, entry=''):
        if vunit: self.pushCont(vunit)
        self._parse(fromstr=fstr, entry=entry)
        if vunit: self.popCont()

    # parse a file or list of file
    @classmethod
    def parse(cls, srcList=None, vunit=None, options=None,
            parser=None, lexer=None):
        if not (srcList or options):
            raise VerpyUserError("Need either String-opt or an option-obj")
        aobj = cls(srcList, options, parser, lexer)
        return aobj.analyze()


