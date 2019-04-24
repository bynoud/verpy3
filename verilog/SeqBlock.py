

from .VerilogObject import *
from .VList import AssignList, VList
from .Assignment import NetContainer

class SeqBlock(VerilogObject):
    def __init__(self, name, kw='assign', parent=None):
        super(SeqBlock, self).__init__(name, parent)
        self.keyw = kw
        self.others = NetContainer(
                name=self.name+'otherRHS', parent=self)
        self.assigns = AssignList(parent=self)
        self.loops   = LoopstmList(parent=self)

    def copyfrom(self, frm, **kwargs):
        super(SeqBlock, self).copyfrom(frm, **kwargs)
        self.keyw = frm.keyw
        self.others = frm.others.clone()
        self.assigns = frm.assigns.clone()
        self.loops = frm.loops.clone()

    def newAssign(self, kw):
        return self.assigns.new(
                name=self.name+"asign"+str(self.parent.uninum),
                kw=kw)

    def newOtherRhs(self, kw):
        return self.others

    def newLoopSeq(self, kw):
        return self.loops.new(name=self.name+kw+str(self.parent.uninum), kw=kw)

    # this called from under assigmnent
    def referNet(self, name, arr=None):
        return self.parent.referNet(name, arr)

    def checkDriverLoad(self, nets, params=None):
        self.others.checkDriverLoad(nets, params, self)
        for i in self.assigns:
            i.checkDriverLoad(nets, params, self)

    def dump(self, indent=''):
        print("%sSequence Block: %s (%s)" % (indent, self.name, self.keyw))
        indent+='  '
        print("%sOther RHS" % indent)
        self.others.dump(indent+'  ')
        print("%sAssignments" % indent)
        self.assigns.dump(indent+'  ')
        print("%sLoops" % indent)
        self.loops.dump(indent+'  ')

# On the loop, dont forward bit-select expression since it may have
# not-constant value in it
class LoopStatement(SeqBlock):
    def __init__(self, name, kw, parent=None):
        super(LoopStatement, self).__init__(name, kw, parent)

    def referNet(self, name, arr=None):
        return self.parent.referNet(name, None) # dont send bit-select

class LoopstmList(VList):
    def __init__(self, parent):
        super(LoopstmList,self).__init__(parent, LoopStatement)
    def new(self, clstype=None, **kwargs):
        if 'name' not in kwargs:
            kwargs['name'] = '__Seqblk_' + str(self.parent.uninum) + '__'
        return super(LoopstmList, self).new(clstype, **kwargs)

