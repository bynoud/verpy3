

from .VerilogObject import *
from ..VerpyError import *

def _unpack2dList(msb, lsb):
    if isinstance(msb,list): [m,l] = (msb + [None])[:2]
    else: [m,l] = [msb,lsb]

    if m == '*':
        m=l=-1
    elif l is None:
        m = int(m)-1
        l = 0
    else:
        m = int(m)
        l = int(l)
    return [m,l]

class SliceableObject(VerilogObject):
    # arrdeep: where the next slice operation will effect
    # ex: net [...] [...] , with deep=-1
    #     ->  ^^^^^        net[3:2] slice here (and new object have deep=0)
    #               ^^^^^  net[3:2][3] : new object have deep=1
    def __init__(self, name, parent=None):
        super(SliceableObject, self).__init__(name, parent) # from NetlistObject
        self.adeep  = -1
        self.selbit = []
        self.fixsize = False
        self._arr = []    # [[msb,lsb, packed], [msb,lsb, packed]...]
                                            #  [-1,-1,packed ] if array size is unknown

    def copyfrom(self, frm, **kwargs):
        super(SliceableObject, self).copyfrom(frm, **kwargs)
        self.adeep = frm.adeep
        self.fixsize = frm.fixsize
        # array of array
        self._arr = primaryCopy(frm._arr)
        self.selbit = primaryCopy(frm.selbit)

    def new_dim(self, msb, lsb=None, packed=True):
        if self.fixsize:
            raise VerpySyntaxError("Cannot create new dimention on '%s'" % self)
        [rm,rl] = _unpack2dList(msb,lsb)
        #        [ ] [ ] .. [ ] [ ]
        # index:  0   1      3   4
        #        unpacked    packed
        if packed:
            ind = len(self._arr)  # if pack, insert at the end
        else:
            ind = 0
            for i in range(len(self._arr)):
                if self._arr[i][2]: break # find first pack array
                ind += 1
        self._arr.insert(ind, [rm,rl,packed])

    def expand(self, msb, lsb=None):
        if self.adeep<0 or not self.bus:
            raise VerpySyntaxError("Cannot expand on net '%s'" % self)
        [rm,rl] = _unpack2dList(msb,lsb)
        [m,l,p] = self._arr[self.adeep]
        if rm<m: rm = m
        if l>=0 and l<rl: rl = l
        if rl<l and rm>m and self.fixsize and m>=0:
                raise VerpySyntaxError("Cannot change bus size of '%s'" % self)
        self._arr[self.adeep] = [rm,rl,p]


    def regslice(self, msb, lsb=None):
        if self.isScala: raise VerpySyntaxError("Cannot slice scala object '%s'" % (self.decl))

        [m1,l1,p1] = self._arr[0]
        if msb == '*' : [msb,lsb] = [m1,l1]
        elif lsb is None: lsb = msb
        [msb,lsb] = [int(msb), int(lsb)]
        if m1<msb or l1>lsb: raise VerpySyntaxError("Slice out-of-range '%s' : %d-%d" %
                (self.decl, msb,lsb))
        [msb,lsb] = [int(msb),int(lsb)]

        # only selbit/adeep need change
        #s = copy(self)
        s = type(self)(name=self.name, parent=self.parent)
        s.fixsize = self.fixsize
        s._arr = self._arr
        s.adeep = self.adeep+1
        s.selbit = []
        for b in self.selbit: s.selbit.append(b)
        s.selbit.append([msb,lsb,p1])
        return s

    # slice is in reverse, ex [3:0]
    def __getitem__(self, key):
        if isinstance(key, slice): return self.regslice(key.start, key.stop)
        return self.regslice(key, key)
    def __getslice__(self, i, j):
        return self.__getitem__(slice(i,j))

    # this used in expression
    def __str__(self):
        t = self.name
        for [m,l,p] in self.selbit:
            if   m<0  : t += '[*]'
            elif m!=l : t += ("[%s:%s]" % (m,l))
            else      : t += ("[%s]" % m)
        return t

    @property
    def nextbus(self):
        if self.adeep < len(self._arr)-1: return self._arr[self.adeep+1][:2]
        else: return None

    @property
    def bus(self):
        if len(self._arr)==0 : return None
        else : return self._arr[0][:2] if not self.selbit else self.selbit[-1][:2]

    @property
    def isScala(self): return True if not self.nextbus else False
    @property
    def msb(self): return None if not self.bus else self.bus[0]
    @property
    def lsb(self): return None if not self.bus else self.bus[1]



class SizeSliceable(SliceableObject):
    def __init__(self, name='', parent=None):
        super(SizeSliceable, self).__init__(name, parent)
        self._drv = []
        self._lds = []

    def copyfrom(self, frm, **kwargs):
        super(SizeSliceable, self).copyfrom(frm, **kwargs)
        # array-of-array or simple array
        self._drv = []
        #for a in frm._drv:
        #    if isinstance(a,list): self._drv.append(a[:])
        #    else: self._drv.append(a)
        self._lds = []
        #for a in frm._lds:
        #    if isinstance(a,list): self._lds.append(a[:])
        #    else: self._lds.append(a)

    def regslice(self, msb, lsb=None):
        r = super(SizeSliceable, self).regslice(msb, lsb)
        r._drv = self._drv
        r._lds = self._lds
        return r

    # to resolve parameter.
    # except new_dim, all function need elab first
    def elaborate(self, params=None):
        self._drv = []  # [ [ d11, d12], [d21], ...]
                                        #                ^bit[0] drv
                                        #                            ^bit[2]
                                        # else, [ d1, d2 ...] driver summary of ALL bit
        self._lds = []
        if len(self._arr)==1 and self._arr[0][0]>=0:
            for i in range(self._arr[0][0]+1):
                self._drv.append([]) # redundance from 0
                self._lds.append([]) # redundance from 0

    def expand(self, msb, lsb=None):
        super(SizeSliceable, self).expand(msb,lsb)
        # keep driver/load is already there
        if len(self._arr)==1:
            for i in range( len(self._drv), self._arr[self.adeep][0]+1 ):
                self._drv.append([])
                self._lds.append([])

    def _drvlds_getmax(self, ptr):
        if len(self._arr)==0: return len(ptr)
        if len(self._arr)>1 : return 0 if len(ptr)==0 else 1
        # 1d array
        [m,l] = self.bus
        nmax = 0
        for ds in ptr[ l : m+1 ]:
            if len(ds)>nmax: nmax=len(ds)
        return nmax

    def _drvlds_getunuse(self, ptr):
        ret = []
        if len(self._arr)!=1:
            if len(ptr)==0: ret.append(self)
        else :
            [m,l] = self.bus
            lunu = -1
            for i in range(l, m+1):
                if len(ptr[i])==0 and lunu<0:
                    lunu = i
                if len(ptr[i])>0 and lunu>=0:
                    ret.append( self[i-1:lunu] )
                    lunu = -1
            if lunu>=0: ret.append( self[m:lunu] )
        return ret

    def _drvlds_set(self, ptr, val):
        if len(self._arr)!=1: ptr.append(val)
        else:
            [m,l] = self.bus
            for i in range(l,m+1):
                if val not in ptr[i]:
                    ptr[i].append(val)

    # max of drivers all bit
    def maxDrivers(self):
        return self._drvlds_getmax(self._drv)

    def setDrivers(self, val):
        self._drvlds_set(self._drv, val)

    @property
    def undrivens(self):
        return self._drvlds_getunuse(self._drv)

    def maxLoads(self):
        return self._drvlds_getmax(self._lds)

    def setLoads(self, val):
        self._drvlds_set(self._lds, val)

    @property
    def unloads(self):
        return self._drvlds_getunuse(self._lds)

    def _drvlds_dump(self, ptr, pref, indent):
        if len(self._arr)!=1:    # just dump out all things, if not 1D array
            m,l = (len(ptr), 0)
            withbit = False
        else:
            m,l = (self.msb+1, self.lsb)
            withbit = True
        withbit = True
        cl = -1
        last = None
        first = True

        def _print(l,m):
            if first:
                print("%s%s" % (indent, pref))
            xs = ""
            if isinstance(last, list):
                for i in last: xs += (", %s" % i)
            else:
                xs = str(last)
            if withbit:
                print("%s  [%d:%d] %s, " % (indent, m, l, xs))
            else:
                print("%s  %s, " % (indent, xs))
            return False    # set this to first

        for i in range(l,m):
            x = ptr[i] or None
            if x != last:
                #print("  %s -- %s" % (ptr[i], last))
                if cl>=0 and last: first = _print(cl, i-1)
                cl = i
                last = ptr[i]
        if last: _print(cl, m-1)

    def dumpDrivers(self, indent=''):
        self._drvlds_dump(self._drv, "Drivers", indent)

    def dumpLoads(self, indent=''):
        self._drvlds_dump(self._lds, "Loads", indent)

    @property
    def width(self):
        if self.isScala:
            return 1
        else:
            w = 0
            for [m,l,p] in self._arr:
                w += abs(m-l+1)
            return w


