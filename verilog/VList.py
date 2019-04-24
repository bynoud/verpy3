

from .VerilogMixins import CloneableMixin
from .VerilogObject import VerilogObject
from ..VerpyError import *
from collections import MutableSequence

class VList(MutableSequence, CloneableMixin):
    def __init__(self, parent, clstype=VerilogObject):
        assert issubclass(clstype, VerilogObject)
        self._parent = parent
        self._cls = clstype
        self._items = []
        self._bynames = {}

    def copyfrom(self, frm, **kwargs):
        if 'parent' in kwargs:
            #print("VList copyfrom parent applied %s" % type(self))
            self.parent = kwargs['parent']
        else:
            self.parent = frm._parent
        self._cls = frm._cls
        self._items = []
        self._bynames = {}
        for v in frm._items:
            self.append(v.clone(**kwargs))

    def new(self, clstype=None, **kwargs):
        if clstype is None: clstype = self._cls
        assert 'name' in kwargs
        assert issubclass(clstype, self._cls)
        return self.append(clstype(**kwargs))

    def append(self, item):
        return self.insert(item,0,1)

    def insert(self, item, ind, append=0):
        assert isinstance(item, self._cls)
        name = item.name
        assert name not in self._bynames
        if item.parent is None:
            item.parent = self.parent
        if append: self._items.append(item)
        else: self._items.insert(ind, item)
        self._bynames[name] = item
        return item

    def isLast(self, item):
        try: return (self._items[-1] is item)
        except: return False

    def isFirst(self, item):
        try: return (self._items[0] is item)
        except: return False

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, val):
        self._parent = val
        #for x in self._items: x.parent = val

    ## abtract method need to override
    def __getitem__(self, key):
        #return self._itemoper('getItem', key)
        if isinstance(key, str):
            return self._bynames[key]
        elif isinstance(key, int):
            return self._items[key]
        else:
            c = type(self)(parent=self._parent)
            for i in self._items[key]: c.append(i)
            return c

    def __setitem__(self, key, val):
        #self._itemoper('setItem', key, val)
        if isinstance(key, str):
            self._bynames[key] = val
        else:
            self._items[key] = val

    def __delitem__(self, key):
        #print("VList del: %s : %s" % (self._cls, key))
        #def dump():
        #    print("items: ", end="")
        #    for i in self._items:
        #        print("%s, " % i.name, end="")
        #    print("\nnames: ", end="")
        #    for i in self._bynames.keys():
        #        print("%s, " % i, end="")
        #    print("")

        #print("before")
        #dump()
        #self._itemoper('delItem', key)
        if isinstance(key, str):
            ind = self._items.index(self._bynames[key])
            del self._items[ind]
            del self._bynames[key]
        elif isinstance(key, int):
            name = self._items[key].name
            del self._items[key]
            del self._bynames[name]
        else:
            for i in self._items[key]:
                del self._bynames[self._items[i].name]
            del self._items[key]
        #print("after")
        #dump()


    def __len__(self):
        return len(self._items)

    # i in o -> __contains__(o,i)
    def __contains__(self, item):
        return (item in self._bynames)

    #def getAttrs(self, name):
    #    return [getattr(x, name) for x in self._items]

    #def setAttrs(self, name, val):
    #    vals = val
    #    if not isinstance(val, list):
    #        vals = [val] * len(self)
    #    for (i,v) in enumerate(self._items):
    #        setattr(v, name, vals[i])

    #def _itemoper(self, op, key, *args):
    #    from types import StringTypes
    #    if isinstance(key, (int, StringTypes)):
    #        return getattr(self, op)(key, *args)
    #    elif isinstance(key, slice):
    #        return getattr(self, op+'s')(key.start or 0, key.stop or len(self), *args)
    #    elif isinstance(key, tuple):
    #        return getattr(self, op+'s')(key, *args)

    #def getItem(self, ind):
    #    if isinstance(ind, int):
    #        return self._items[ind]
    #    else:
    #        return self._bynames[ind]

    #def getItems(self, start, stop):
    #    #return self.filter(lambda x: start <= x.index < stop)
    #    return self._items[start:stop]

    #def setItem(self, ind, val):
    #    if isinstance(ind, int):
    #        self._items[ind] = val
    #    else:
    #        self._bynames[ind] = val

    #def setItems(self, start, stop, vals):
    #    self._items
    #    for i in range(start, stop):
    #        self._items[i] = vals[i]

    #def delItem(self, ind):
    #    name = ind
    #    if isinstance(ind, int):
    #        name = self._items[ind].name
    #    else:
    #        ind = self._bynames[ind]
    #    del self._items[ind]
    #    del self._bynames[name]

    #def delItems(self, start, stop):
    #    for i in range(start, stop):
    #        del self._bynames[self._items[i].name]
    #    del self._items[start, stop]

    def filter(self, func):
        if func is None:
            func = lambda x: x is not None
        c = type(self)(parent=self._parent)
        for v in self._items:
            if func(v): c.append(v)
        return c

    def keys(self):
        return [x.name for x in self._items]
    def iterkeys(self):
        for x in self._items: yield x.name

    def values(self):
        return self._items
    def itervalues(self):
        for x in self._items: yield x

    def items(self):
        return [(x.name, x) for x in self._items]
    def iteritems(self):
        for x in self._items: yield x.name, x

    def dump(self, indent=''):
        for x in self._items:
            x.dump(indent)

class ModuleList(VList):
    def __init__(self, parent):
        from .Module import Module
        super(ModuleList,self).__init__(parent, Module)

class CellList(VList):
    def __init__(self, parent):
        from .Cell import Cell
        super(CellList,self).__init__(parent, Cell)

class PinList(VList):
    def __init__(self, parent):
        from .Pin import Pin
        super(PinList,self).__init__(parent, Pin)

class NetList(VList):
    def __init__(self, parent):
        from .Net import Net
        super(NetList,self).__init__(parent, Net)

class AssignList(VList):
    def __init__(self, parent):
        from .Assignment import Assignment
        super(AssignList,self).__init__(parent, Assignment)
    def new(self, clstype=None, **kwargs):
        if 'name' not in kwargs:
            kwargs['name'] = '__assign_' + str(self.parent.uninum) + '__'
        return super(AssignList, self).new(clstype, **kwargs)

class ContainerList(VList):
    def __init__(self, parent):
        from .Assignment import NetContainer
        super(ContainerList,self).__init__(parent, NetContainer)
    def new(self, clstype=None, **kwargs):
        if 'name' not in kwargs:
            kwargs['name'] = '__container_' + str(self.parent.uninum) + '__'
        return super(ContainerList, self).new(clstype, **kwargs)

class SeqblkList(VList):
    def __init__(self, parent):
        from .SeqBlock import SeqBlock
        super(SeqblkList,self).__init__(parent, SeqBlock)
    def new(self, clstype=None, **kwargs):
        if 'name' not in kwargs:
            kwargs['name'] = '__Seqblk_' + str(self.parent.uninum) + '__'
        return super(SeqblkList, self).new(clstype, **kwargs)

