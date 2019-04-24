

from ..VerpyError import *
from .VerilogMixins import *
import logging


logger = logging.getLogger(__name__)
def debug(msg, *args): logger.debug(msg, *args)
def info(msg, *args): logger.info(msg, *args)
def warning(msg, *args): logger.warning(msg, *args)

def primaryCopy(frm, vdeep=True):
    ret = None
    if isinstance(frm, VerilogObject):
        ret = frm if not vdeep else frm.clone()
    elif isinstance(frm, list):
        ret = []
        for i in frm: ret.append(primaryCopy(i))
    elif isinstance(frm, set):
        ret = set()
        for i in frm: ret.add(i)
    elif isinstance(frm, dict):
        ret = {}
        for (k,v) in list(frm.items()):
            ret[primaryCopy(k)] = primaryCopy(v)
    else:
        ret = frm
    return ret


class VerilogObject(CloneableMixin):
    def __init__(self, name="", parent=None):
        self.parent = parent
        self.name = name
        self.index = 0
        self.filename = ''
        self.startline = -1
        self.endline = -1
        self.column = -1
        self._uninum = 0

    # deep copy
    # allow parent tobe change by kwargs
    def copyfrom(self, frm, **kwargs):
        assert isinstance(frm, VerilogObject)
        if 'parent' in kwargs:
            #print("Vobject copyfrom parent applied %s" % type(self))
            self.parent = kwargs['parent']
        else:
            self.parent = frm.parent
        self.name   = frm.name
        self.index = frm.index
        self.filename = frm.filename
        self.startline = frm.startline
        self.endline = frm.endline
        self.column = frm.column
        self._uninum = frm._uninum

    @property
    def root(self):
        try:
            return self._root
        except:
            r = self
            for i in range(100000):
                try:
                    self._root = r._root
                except:
                    r = r.parent
                return self._root
            raise Exception('Internal fatal')

    @property
    def uninum(self):
        self._uninum += 1
        return self._uninum

    def elaborate(self, params=None):
        pass

    def link(self):
        pass

    def dump(self):
        pass

    def __str__(self):
        return self.name

