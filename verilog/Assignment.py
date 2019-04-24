

from .VerilogObject import *
from .VerilogMixins import ContainableMixin
from ..VerpyError import *

class NetContainer(VerilogObject, ContainableMixin):
    def __init__(self, name, kw='__otherrhs__', parent=None):
        super(NetContainer, self).__init__(name, parent)
        self.keyw = kw
        ContainableMixin.init(self) # list of nets

    def copyfrom(self, frm, **kwargs):
        super(NetContainer, self).copyfrom(frm, **kwargs)
        self.keyw = frm.keyw
        self.containerCopy(frm, **kwargs)

    def checkDriverLoad(self, nets, params=None, tbused=None):
        from .SeqBlock import SeqBlock
        tbused = tbused or self
        self.containerResolve(nets, params)
        for n in self.containerIter():
            n.setLoads(tbused)

    def dump(self, indent=''):
        print("%sContainer: %s (%s) " % (indent, self.name, self.keyw))
        self.containerDump(indent+'  ')

class Assignment(VerilogObject, ContainableMixin):
    LHS = 0
    RHS = 1
    def __init__(self, name, kw='assign', parent=None):
        super(Assignment, self).__init__(name, parent)
        self.keyw = kw
        self._side = Assignment.LHS
        ContainableMixin.init(self, 2)  # 2 for lhs/rhs

    def copyfrom(self, frm, **kwargs):
        super(Assignment, self).copyfrom(frm, **kwargs)
        self.keyw = frm.keyw
        self._side = frm._side
        self.containerCopy(frm, **kwargs)

    def setRhs(self):
        self._side = Assignment.RHS

    def setLhs(self):
        self._side = Assignment.LHS

    def referNet(self, name, arr=None):
        return ContainableMixin.referNet(self, name, arr, self._side)

    #@property
    #def lhs(self):
    #    return self.containerRef(Assignment.LHS)

    #@property
    #def rhs(self):
    #    return self.containerRef(Assignment.RHS)

    def checkDriverLoad(self, nets, params=None, tbused=None):
        from .SeqBlock import SeqBlock
        tbused = tbused or self
        self.containerResolve(nets, params)
        for n in self.containerIter(Assignment.LHS):
            n.setDrivers(tbused)
        for n in self.containerIter(Assignment.RHS):
            n.setLoads(tbused)

    def dump(self, indent=''):
        print("%sAssignment: %s (%s) " % (indent, self.name, self.keyw))
        indent+='  '
        print("%sLHS:" % indent)
        self.containerDump(indent+'  ', Assignment.LHS)
        print("%sRHS:" % indent)
        self.containerDump(indent+'  ', Assignment.RHS)

