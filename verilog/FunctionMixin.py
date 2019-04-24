

from ..VerpyError import *

class FunctionMixin(object):
    def functionInit(self):
        self.funcs = {}

    def functionCopy(self, frm):
        self.funcs = {}
        for k,v in list(frm.funcs.items()):
            self.funcs[k] = v.clone()

    def newFunction(self, name):
        if name in self.funcs:
            raise VerpySyntaxError("function '%s' is redefined" % name)
        self.funcs[name] = VerilogFunction(name, self)
        return self.funcs[name]

    def elaborate(self, params=None):
        r = ""
        varspace = {}
        for f in list(self.funcs.values()):
            r += f.elaborate()
        if params:
            for k,v in list(params.items()):
                r += "%s = %s\n" % (k,v)
        exec(r, varspace)
        return varspace

class VerilogFunction(object):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.args = []
        self.outs = []  # should be index bits, output/inout will be change to globals()[name]
        self.body = ''  # functioncall is repalce with '<fcall[index]>'
        self._in = 1    # current indent, start at already indented
        self._inready = True    # after indent there's must be code

    def clone(self):
        c = VerilogFunction(self.name)
        c.args = self.args[:]
        c.outs = self.outs[:]
        c.body = self.body
        return c

    def newArg(self, arg, adir):
        self.args.append(arg)
        if adir in ['output', 'inout']:
            self.outs.append(len(self.args)-1)

    def newCode(self, code):
        if code.isspace(): return
        self.body += " "*self._in + code + "\n"
        self._inready = True

    def indent(self, code=""):
        if code: self.newCode(code)
        self._in += 1
        self._inready = False

    def dedent(self, code=""):
        if code: self.newCode(code)
        if not self._inready:
            self.newCode("pass")
            self._inready = True
        self._in -= 1

    def elaborate(self):
        assert self._in == 1
        r = "def %s(" % self.name
        for a in self.args: r += a + ","
        r += "):\n"
        for a in self.outs:
            r += " __%s = %s\n" % (a,a)         # save pass-in name
            r += " %s = globals()[%s]" % (a,a)  # get in global vars
        # set output to global var
        for a in self.outs:
            r += " globals()[__%s] = %s" % (a,a)
        # add return at last, which will return function name value
        return r + self.body + " return %s\n" % self.name


class FunctionCall(object):
    def __init__(self, name, args=None):
        self.name = name
        self.args = args or []

    def newArgs(self, arg):
        self.args.append(arg)

    def elaborate(self, fnlist):
        for fn in fnlist:
            if fn.name == self.name:
                r = self.name+'('
                if len(self.args) != len(fn.args):
                    raise VerpySyntaxError( "function '%s' number of call arg %0d not match with definition %0d" % (fn.name, len(self.args), len(fn.args)))
                for i,v in enumerate(self.args):
                    if i in fn.outs: r += '"%s",' % v   # use string-name
                    else           : r += '%s,' % v
                return r+')'
        raise VerpySyntaxError("Cannot find function '%s'" % self.name)


