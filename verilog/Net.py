

from .VList import NetList
from .SliceableObject import SizeSliceable
from .AstEvaluation import eval_expression
from .VerilogObject import primaryCopy
from ..VerpyError import *

class Net(SizeSliceable):
    def __init__(self, name, ntype='wire', direction='net', parent=None):
        super(Net, self).__init__(name, parent)
        self.ntype = ntype
        self.direction = direction
        self.nets = NetList(self)   # drivens nets
        self._rawbus = []
        self._rawref = []

    def copyfrom(self, frm, **kwargs):
        super(Net, self).copyfrom(frm, **kwargs)
        # simple string
        self.ntype = frm.ntype
        self.direction = frm.direction
        self.nets = frm.nets    # should be shallow??
        # array-of-array
        self._rawbus = primaryCopy(frm._rawbus)
        self._rawref = primaryCopy(frm._rawref)

    def copyBus(self, frm):
        for a in frm._rawbus: self._rawbus.append(primaryCopy(a))
        for a in frm._rawref: self._rawref.append(primaryCopy(a))

    # arr = [[2,1], [3,2], [4,1]]
    def declBus(self, parr, uarr=None):
        if not (parr or uarr): return
        if uarr is None: uarr = []
        self._rawbus.append( [ [x[0],x[1],False] for x in uarr ] +
                             [ [x[0],x[1],True]  for x in parr ] )

    # arr = [[2,1], [3,3]..]
    def refBus(self, arr):
        if arr: self._rawref.append(arr)

    def _buswidthResolve(self, params=None):
        if not self._rawbus: return
        # resolve buswidth first
        for (i,a) in enumerate(self._rawbus):
            for (j,a2) in enumerate(a):
                self._rawbus[i][j] = [eval_expression(a2[0], params),
                                      eval_expression(a2[1], params), a2[2]]

        r = self._rawbus.pop()
        for [m,l,p] in r:
            self.new_dim(m,l,p)
        self.fixsize = True

        for a in self._rawbus:
            self._declCheck(a)
        self._rawbus = []

    # for multiple declaration, check for consistency
    def _declCheck(self, arr):
        if len(arr) != len(self._arr):
            raise VerpySyntaxError("Decl bus size mismatch")
        for (i,a) in enumerate(arr):
            if self._arr[i] != a:
                raise VerpySyntaxError("Decl bus width mismathc")

    # reference check
    def _busrefCheck(self, params):
        if not self._rawref: return
        for (i,a) in enumerate(self._rawref):
            if len(a) > len(self._arr):
                raise VerpySyntaxError("Reference out-of-index")
            for (j,a2) in enumerate(a):
                m,l = (eval_expression(a2[0], params),
                       eval_expression(a2[1], params))
                if m>self._arr[j][0] or l<self._arr[j][1]:
                    raise VerpySyntaxError("Reference out-of-bit range")
        self._rawref = []

    def elaborate(self, params=None):
        try:
            self._buswidthResolve(params)
            self._busrefCheck(params)
            super(Net, self).elaborate(params)
        except VerpySyntaxError as e:
            raise VerpyElabError("elab failed, net '%s' : %s" % (self, e))

    def _array(self):
        ptxt = utxt = ""
        if self._rawbus:    # if not elab yet, only get first decl encounter
            ptxt = ''.join("[%s:%s]" % (m,l) for m,l,p in self._rawbus[0] if p)
            utxt = ''.join("[%s:%s]" % (m,l) for m,l,p in self._rawbus[0] if not p)
        else:
            for [m,l,p] in self._arr:
                t = '[*]' if m<0 else ("[%s:%s]" % (m,l))
                if p: ptxt += t+" "
                else: utxt += " "+t
        return ptxt, utxt

    @property
    def arrayBus(self):
        ptxt, utxt = self._array()
        return "%s%s" % (ptxt, "" if not utxt else utxt+"u")

    # use for declare
    @property
    def decl(self):
        ptxt, utxt = self._array()
        txt = ptxt+self.name+utxt
        return txt

    def dump(self, indent=""):
        #print(indent+self.direction+": "+str(self.ntype)+" ", end="")
        print("%s%s: %s %s" % (indent, self.direction, self.ntype, self.decl))
        indent+='  '
        if self._rawbus:
            print("%srawbus %s" % (indent, self._rawbus))
        if self._rawref:
            print("%srefbus %s" % (indent, self._rawref))
        #print("%sDrivers : " % indent)
        self.dumpDrivers(indent)
        #print("%sLoads : " % indent)
        self.dumpLoads(indent)
        if self.undrivens:
            print("%sUNDRIVENS :" % indent, end='')
            for u in self.undrivens: print(" %s," % u, end='')
            print("")
        if self.unloads:
            print("%sUNLOADS:" % indent, end='')
            for u in self.unloads: print(" %s," % u, end='')
            print("")


class Port(Net):
    pass

class Parameter(Net):
    def __init__(self, name, ntype):
        super(Parameter, self).__init__(name=name, ntype=ntype, direction='net')
        self.val = ''

    def copyfrom(self, frm, **kwargs):
        super(Parameter, self).copyfrom(frm, **kwargs)
        self.val = frm.val

    def dump(self, indent=""):
        print("%s%s: %s = %s" % (indent, self.ntype, self.name, self.val))


