

from .VerilogObject import *
from .VList import ModuleList
from ..VerpyError import *

class VerilogUnit(VerilogObject):
    def __init__(self, name='$unit'):
        super(VerilogUnit, self).__init__(name=name)
        self.mods = ModuleList(self)
        self.tops = ModuleList(self)

    def copyfrom(self, frm):
        super(VerilogUnit, self).copyfrom(frm)
        self.mods = frm.mods.clone()
        self.tops = frm.tops.clone()

    def newModule(self, name, kw="module"):
        debug("new %s for %s : %s" % (kw, self.name, name))
        return self.mods.new(name=name, kw=kw)

    def link(self):
        """
        mainly use to fix hierachycal instance
        """
        self.tops = self.mods[:]
        for m in self.mods:
            for c in m.cells:
                try:
                    c.modref = self.mods[c.modname]
                    self.tops.remove(c.modname)     # not in tops, if not in mods
                except:
                    pass

    def elaborate(self, topname=''):
        # move instanced-module under thier parent
        self.link()
        if topname:
            if topname not in self.mods.names:
                raise VerpyUserError("Unknown top module name '%s'" % topname)
            self.mods[topname].elaborate()
        else:
            for m in self.tops: m.elaborate()

    def dump(self, indent=""):
        print(indent+"VerilogUnit: "+self.name)
        indent+="  "
        for m in self.tops: m.dump(indent)

    @property
    def topModules(self):
        return [ x for x in self.tops ]

