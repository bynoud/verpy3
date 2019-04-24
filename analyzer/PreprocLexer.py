

import sys
import logging
from io import StringIO

from antlr4.Token import Token
from antlr4.CommonTokenStream import CommonTokenStream
from ..parser.VerexLexer import VerexLexer
from ..parser.VerexParser import VerexParser
from ..VerpyError import *
from .PRCHelper import createInputStream, fullText
from .AnalyzerOption import AnalyzerOption

# match a preprocessor directive will span another lexer
# this is to keep track of where error is come from

logger = logging.getLogger(__name__)
def debug(msg, *args): logger.debug(msg, *args)
def info(msg, *args): logger.info(msg, *args)
def warning(msg, *args): logger.warning(msg, *args)

def _strName(tok):
    return tok.getInputStream().name

# method to be overrided:
#   nextToken & reset
class PreprocLexer(VerexLexer):
    def __init__(self, input=None, output=sys.stdout, options=None):
        super(PreprocLexer, self).__init__(input, output)
        self.opts = options or AnalyzerOption()
        #self.condStack = [True]
        #self.tokgen = True
        self.condDirect = PreprocLexer.ConditionDirective(defines=self.opts.defines)
        self._lexStack = [self] # active lexer stack

    @property
    def actLex(self):
        return self._lexStack[-1]

    @actLex.setter
    def actLex(self, val):
        #if isinstance(val, PreprocLexer):
        #    val = super(PreprocLexer, val)
        if isinstance(val, int):
            assert len(self._lexStack) > 1
            self._lexStack.pop()
        else:
            self._lexStack.append(val)

    def nextToken(self):
        t = super(PreprocLexer, self.actLex).nextToken()
        #debug("   attemped: %s -> %s" % (t.getInputStream().name, t))
        skipThis = False

        if t.type == VerexLexer.Condition_directive:
            #self.tokgen = self._condDirective(t.text)
            self._condDirective(t.text)
            return self.nextToken()

        if t.type != Token.EOF and self.condDirect.dismiss:
            return self.nextToken() # ignore token by directive

        if t.type == Token.EOF and self.actLex != self:
            self.actLex = -1    # step back to last active Lex
            return self.nextToken()

        if t.type == VerexLexer.Builtin_directive:
            kw, txt = (t.text.split(None,1) + [''])[:2]
            kw = kw[1:] # remove '`'
            if kw == 'define':
                self._newDefine(t, txt)
            elif kw == 'undef':
                self.opts.delDefine(txt)
            elif kw == 'resetall':
                self.opts.resetDefine()
            elif kw == 'include':
                self.actLex = self._expandIncFile(t, txt)
            #elif kw in ('ifdef', 'ifndef', 'elsif', 'else', 'endif'):
            #    self.tokgen = self._condDirective(kw, txt)
            else:
                pass    # other just throught away
            return self.nextToken()    # fetch next token

        if t.type == VerexLexer.User_macro_call:
            self.actLex = self._expandDefine(t)
            return self.nextToken()

        #debug("-> returned: %s -> %s" % (t.getInputStream().name, t))
        return t

    def _newDefine(self, tok, txt):
        srcName = '<define on %s(%d:%d)>' % (
                tok.getInputStream().name, tok.line, tok.column)
        debug("---- internal parsing ---")
        istr = createInputStream(fromstr=txt, srcName=srcName)
        lex = type(self)(
            input=istr,
            options=self.opts)
        tokens = CommonTokenStream(lex)
        par = VerexParser(tokens)
        macro = par.text_macro_definition()
        name = macro.text_macro_name().text_macro_identifier().getText()
        if name in self.opts.defines:
            warning("redefine macro '%s'" % name)

        ud = self.opts.newDefine(name)
        args = macro.text_macro_name().list_of_formal_arguments()
        if args :
            for a in args.formal_argument_identifier():
                ud.addArg(a.getText())
        ud.body = tokens.getText([macro.macro_text().start, macro.macro_text().stop])
        debug("---- new define '%s' = %s" % (name, ud.body))

    def _condDirective(self, txt):
        kw, txt = (txt.split() + [''])[:2]
        self.condDirect = self.condDirect.newCond(kw[1:], txt)

    def _condDirective_old(self, txt):
        txts = txt.split()
        kw = txts[0][1:]    # remove '`'
        if kw in ('ifdef', 'ifndef', 'elsif'):
            if len(txts) != 2:
                raise VerpySyntaxError()
            meet = (txts[1] in self.opts.defines) ^ (kw == 'ifndef')
        elif len(txts) > 1:
            raise VerpySyntaxError()

        if kw in ('ifdef', 'ifndef'):
            self.condStack.append(meet)
            return meet
        elif kw == 'endif':
            if len(self.condStack) < 2:
                raise VerpySyntaxError("un-match `endif directive")
            self.condStack.pop()
            return self.condStack[-1]
        elif kw == 'elsif':
            if len(self.condStack) < 2:
                raise VerpySyntaxError("un-match `elsif directive")
            if self.condStack[-1]:   # previous already matched
                return False
            else:
                self.condStack[-1] = meet
                return meet
        elif kw == 'else':
            if self.condStack[-1]:  # already met
                return False
            else:
                self.condStack[-1] = True
                return True

    # do a LEX for defined text
    def _expandDefine(self, tok):
        srcName = "macro '%s' on %s(%d:%d)" % (
            tok.text, tok.getInputStream().name, tok.line, tok.column)
        # try to get syntax of usage
        debug("---- internal macro processed ---")
        lex = type(self)(
            input=createInputStream(fromstr=tok.text[1:],
                                    srcName="<usage %s>" % srcName),
            options=self.opts)
        par = VerexParser(CommonTokenStream(lex))
        usage = par.text_macro_usage()
        name = usage.text_macro_identifier().getText()
        if name not in self.opts.defines:
            raise VerpySyntaxError("Unknown macro '%s'" % name)
        args = []
        for a in usage.expression():
            args.append(a.getText())

        # create a LEX to handle expanded code
        expanded = self.opts.expandDefines(name, *args)
        debug("---- macro expaned '%s' -> %s ---" % (name, expanded))
        return type(self)(
            input=createInputStream(fromstr=expanded,
                                    srcName="<expand %s>" % srcName),
            options=self.opts)

    def _expandIncFile(self, tok, name):
        #  future support for <filename>
        name = name.strip(' \t\n"<>')
        fname = self.opts.findIncludeFile(name)
        debug("---- included file '%s'" % fname)
        srcName = "<included file '%s' on %s(%d:%d)>" % (
            name, _strName(tok), tok.line, tok.column)
        return type(self)(
            input=createInputStream(filename=fname, srcName=srcName),
            options=self.opts)

    def reset(self):
        self._lexStack = [self]
        super(PreprocLexer,self).reset()

    class ConditionDirective(object):
        def __init__(self, defines=None, parent=None, kw=''):
            self.kw = kw
            self.parent = parent
            self.dirs = defines if defines is not None else parent.dirs
            self.macro = ''
            self.childs = []    # nested ifdef

        @property
        def empty(self):
            return (len(self.childs) == 0)

        @property
        def isIf(self):
            return self.kw in ('ifdef', 'ifndef')

        def newChild(self, kw, name):
            if kw != 'else' and name == '':
                raise VerpySyntaxError()
            c = type(self)(kw=kw, parent=self)
            c.macro = name
            self.childs.append(c)
            return c

        def newCond(self, kw, name=''):
            if kw in ('ifdef', 'ifndef'):
                r = self.newChild(kw, name)
            else:
                if self.parent is None:
                    raise VerpySyntaxError("Un-matched condition directive '%s'" % kw)
                if kw == 'endif':
                    r = self.parent
                else:
                    r = self.parent.newChild(kw, name)
            debug("  new Cond direct '%s' ? %s -> %s" % (kw, name, r.dismiss))
            return r

        @property
        def sibb(self): # only from nearest 'ifdef'
            p = self.parent.childs
            ifdpos = 0
            for i,x in enumerate(p):
                if x.isIf:
                    ifdpos = i
            return p[ifdpos:p.index(self)]

        @property
        def dismiss(self):
            try:
                return self.__dism
            except:
                finish = False
                if self.parent is None:
                    self.__dism = False
                    finish = True

                if not finish:
                    p = self.parent
                    # if parent already mot matched, all child also dont
                    if p.dismiss:
                        self.__dism = True
                        finish = True
                    for x in self.sibb:
                        if not x.dismiss:   # previous child already meet
                            self.__dism = True
                            finish = True
                            break

                if not finish:
                    if self.kw == 'else':
                        self.__dism = False # if came here, mean it will meet
                    elif (self.macro in self.dirs) ^ (self.kw == 'ifndef'):
                        self.__dism = False
                    else:
                        self.__dism = True
                return self.__dism


