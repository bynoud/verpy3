
from ..VerpyError import *
from .Net import Parameter

def _isGlobal(x):
    return x.ntype == 'parameter'
def _isLocal(x):
    return x.ntype == 'localparam'
def _isParam(x):
    return _isGlobal(x) or _isLocal(x)

class ParamMixin(object):
    def paramInit(self, paramList):
        self._params = paramList

    def _newParam(self, kw, name, val):
        p = self._params.new(Parameter, name=name, ntype=kw)
        p.val = val
        return p

    def newParam(self, name, val):
        return self._newParam('parameter', name, val)

    def newLocalparam(self, name, val):
        return self._newParam('localparam', name, val)

    # Use to manual overwrite paramenter which include unknow-value (ex:function call)
    def overwriteParam(self, params):
        for (p,v) in params.items():
            assert isinstance(self._params[p], Parameter)
            self._params[p].val = v

    @property
    def parameters(self):
        #try: return self._paramresolved
        #except:
            return {x.name : x.val for x in self._params.filter(_isParam)}

    @property
    def globalParams(self):
        return {x.name : x.val for x in self._params.filter(_isGlobal)}

    def defparams(self, defp):
        par = self._params.filter(_isGlobal)
        if isinstance(defp,list):
            try:
                for k in range(len(defp)):
                    par[k].val = defp[k]
            except IndexError:
                raise VerpyElabError("To many Parameter for '%s'")
        else:
            try:
                for (k,v) in defp.items():
                    if k in par: par[k].val = v
            except KeyError:
                raise VerpyElabError("Parameter '%s' not found in '%s'")

    def elaborate(self, varspace, defparams=None):
        from .AstEvaluation import eval_expression
        if defparams: self.defparams(defparams)
        s = ""
        for k,v in list(self.parameters.items()):
            s += "%s = %s\n" % (k,v)
        try:
            exec(s, varspace)
        except Exception as e:
            raise VerpySyntaxError("Failed to resolved parameter : %s" % e)
        #resolved = True
        #params = self.parameters
        ## parameter can be string
        #for i in range(100):
        #    resolved = True
        #    for (k,v) in params.iteritems():
        #        if isinstance(v, int):  # already number
        #            pass
        #        elif v[0]=='"' and v[-1]=='"':    # string parameter
        #            pass
        #        else:
        #            try: params[k] = eval_expression(v, params)
        #            except Exception,e:
        #                resolved = False
        #    if resolved: break
        #if not resolved:
        #    raise Exception("Cannot resolve parameter dependence: %s" % params)
        #self._paramresolved = params


