
class CloneableMixin(object):

    def clone(self, *args, **kwargs):
        c = object.__new__(self.__class__)
        c.copyfrom(self, *args, **kwargs)
        return c

class ContainableMixin(object):
    def init(self, depth=1):
        self.__contRef = []
        for i in range(depth):
            self.__contRef.append([])
        return self

    def containerCopy(self, frm, **kwargs):
        from .VerilogObject import primaryCopy
        self.__contRef = primaryCopy(frm.__contRef, False) # shadow copy if already resolved

    # this normally called ad analyze time, bus-width maybe in form of expression
    # 'addto' is a list of :
    # [ [netname, [[3:1]]],
    #   [otehname, [[4:1],[2:0]],
    #   [netname, []
    # ]
    def referNet(self, name, arr=None, ind=0):
        #print("container refer net [%d] %s (%s) -> %s %s" %
        #        (ind, self.name, type(self), name, arr))
        n = self.parent.referNet(name, arr)
        self.__contRef[ind].append([name, arr or []])
        return n

    def containerResolve(self, nets, params=None, ind=-1):
        from .VList import NetList
        from .AstEvaluation import eval_expression
        inds = list(range(len(self.__contRef))) if ind<0 else [ind]
        for ii in inds:
            r = []
            for name, arr in self.__contRef[ii]:
                net = nets[name]
                for m,l in arr:
                    m,l = (eval_expression(m, params),
                           eval_expression(l, params))
                    net = net[m:l]
                r.append(net)
            self.__contRef[ii] = r

    #def containerRef(self, ind=0):
    #    return self.__contRef[ind]

    def containerIter(self, ind=0):
        for i in self.__contRef[ind]:
            yield i

    def containerDel(self, ind=0):
        self.__contRef[ind] = []

    def containerDump(self, indent='', ind=0):
        from .VerilogObject import VerilogObject
        for i in self.__contRef[ind]:
            # even with Net, use 'name [selbit]' for clarify
            print(("%s%s" % (indent, i)))
            #if isinstance(i, VerilogObject):
            #    #i.dump(indent)
            #    print("%s
            #else:
            #    print("%s%s" % (indent, i))

