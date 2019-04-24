

from .VerilogObject import *
from .VList import PinList
from .ParamMixin import ParamMixin
from ..VerpyError import *

class Cell(VerilogObject):
    def __init__(self, name, modname="", parent=None):
        super(Cell, self).__init__(name=name, parent=parent)
        self.modname = modname
        self.modref  = None
        self.pins    = PinList(parent=self)
        self._defp   = None

    def copyfrom(self, frm, **kwargs):
        super(Cell, self).copyfrom(frm, **kwargs)
        self.modname = frm.modname
        self.modref  = None # Link must run again to correct this
        self.pins = frm.pins.clone(parent=self)
        self._defp = primaryCopy(frm._defp)

    def newPin(self, name, _dir='any'):
        return self.pins.new(name=name, direction=_dir)

    #def inferNet(self, name):
    #    return self.parent.inferNet(name)
    def referNet(self, name, arr=None):
        return self.parent.referNet(name, arr)

    def elaborate(self):
        if not self.modref: return
        # unify module-ref, by parameter value
        modref = self.modref.clone()
        modref.elaborate(self._defp)
        self.modref = modref
        # resolve pin connection
        _pinnames = []
        debug("start to resolves : %s -> %s" % (self.name, self.modref))
        for (i,p) in enumerate(self.pins):
            try:
                p.elaborate(self.modref.ports, _pinnames)
            except VerpySyntaxError as e:
                raise VerpySyntaxError("Failed to resolve cell '%s' : %s" %
                                       self.name, e)

    def defparams(self,val):
        if not val: return
        if isinstance(val,dict):
            if not self._defp: self._defp = {}
            self._defp.update(val)
        else:
            if not self._defp: self._defp = []
            if isinstance(val, (list, tuple)):
                self._defp += val
            else:
                self._defp.append(val)

    def checkDriverLoad(self, nets, params=None, tbused=None):
        for p in self.pins:
            p.checkDriverLoad(nets, params, tbused)

    def dump(self, indent=""):
        print(indent+"cell: "+self.modname+" "+self.name)
        indent+="  "
        print(indent+"defparam : '%s'" % (self._defp))
        for p in self.pins: p.dump(indent)
        if self.modref:
            print(indent+"--- Mod ref ---")
            self.modref.dump(indent)

