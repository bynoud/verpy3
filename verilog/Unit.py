

from .VerilogObject import *
from .VList import ModuleList
from ..VerpyError import *

class Unit(VerilogObject):
    def __init__(self, options, name='$unit'):
        super(Unit, self).__init__(name=name)
        self._root = self
        self.opts = options
        self.mods = ModuleList(self)
        self.tops = ModuleList(self)

    def copyfrom(self, frm):
        super(Unit, self).copyfrom(frm)
        self.__root = self
        self.opts = frm.opts    # shallow
        self.mods = frm.mods.clone()
        self.tops = ModuleList(self) # need to run link again!!!

    def newModule(self, name, kw="module"):
        debug("new %s for %s : %s" % (kw, self.name, name))
        for m in self.mods: print("  %s" % m.name)
        return self.mods.new(name=name, kw=kw)

    def findModule(self, name):
        return None if name not in self.mods else self.mods[name]

    def removeModule(self, name):
        if name in self.mods:
            for m in self.mods:
                for c in m.cells:
                    if c.modref is self.mods[name]:
                        c.modref = None
            del self.mods[name]
            del self.tops[name]

    def link(self):
        """
        mainly use to fix hierachycal instance
        """
        self.tops = self.mods[:]
        for m in self.mods:
            for c in m.cells:
                if c.modname in self.mods:
                    c.modref = self.mods[c.modname]
                if c.modname in self.tops:
                    del self.tops[c.modname]
        self._linked = True

    def elaborate(self, topname=''):
        # move instanced-module under thier parent
        try: self._linked
        except: self.link()
        if topname:
            if topname not in self.mods:
                raise VerpyUserError("Unknown top module name '%s'" % topname)
            self.mods[topname].elaborate()
        else:
            for m in self.tops: m.elaborate()

    def dump(self, indent=""):
        print(indent+"Unit: "+self.name)
        indent+="  "
        for m in self.tops: m.dump(indent)

    @property
    def topModules(self):
        return [ x for x in self.tops ]

