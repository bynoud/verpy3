


## conver Verilog Context to Python string
## Currnetly support function & expr
import re
from ast import *
from ..VerpyError import *
from ..parser import VerexParser as VP

#fn_outlist = {}
#
#def function2py(ctx):
#    assert isinstance(ctx, VP.Function_declarationContext)
#    fn = ctx.function_identifier().getText()
#    # add one addtion argument for saving output port
#    fn_outlist[fn] = []
#    args = []
#    def getPort(tf):
#        for p in tf.list_of_port_identifiers().port_identifier():
#            pname = p.getText()
#            args.append(pname)
#            if tf.tfdir.text in ['output', 'inout']:
#                fn_outlist[fn].append(pname)
#    if ctx.function_port_list():
#        for pdecl in ctx.function_port_list().function_port():
#            getPort(decl.tf_declaration())
#    else:
#        for pitem in ctx.function_item_declaration():
#            if pitem.tf_declaration():
#                getPort(pitem.tf_declaration())
#
#    r = indent + "def " + fn + '(' + ('_args' if fn_ports or '') + ')\n'
#    idecl = ctx.block_item_declaration() or \
#            ctx.function_item_declaration().block_item_declaration()

def expr2py(ctx):  # VP.ExpressionContext
    assert isinstance(ctx, VP.ExpressionContext)
    if ctx.binary_operator():
        return "%s %s %s" % (
                expr2py(ctx.op1),
                binop2py(ctx.binary_operator()),
                expr2py(ctx.op2))
    elif ctx.expression():
        return "(%s) if (%s) else (%s)" % (
                expr2py(ctx.iftrue),
                expr2py(ctx.cond),
                expr2py(ctx.iffalse))
    else:
        return term2py(ctx.term())

def binop2py(ctx):
    t = ctx.getText()
    return {
            '==='   : '==',
            '!=='   : '!=',
            '&&'    : 'and',
            '||'    : 'or',
            '~^'    : 'not_supported',
            '>>>'   : '>>',     # TODO : should be signed shift
            '<<<'   : '<<',
            }.get(t, t)   # default use as it is

def unop2py(ctx):
    t = ctx.getText()
    return {
            '&'     : 'TODO',
            '~&'    : 'TODO',
            '|'     : 'TODO',
            '~|'    : 'TODO',
            '^'     : 'TODO',
            '~^'    : 'TODO',
            '^~'    : 'TODO',
            }.get(t, t)

def term2py(ctx):
    assert isinstance(ctx, VP.TermContext)
    pre = "" if not ctx.unary_operator() else unop2py(ctx.unary_operator())
    if ctx.String():
        return pre + ctx.String().text
    else:
        return pre + primary2py(ctx.primary())

def primary2py(ctx):
    if ctx.number():
        return number2py(ctx.number())
    elif ctx.hierid_reference():
        return ctx.hierid_reference().getText()
    elif ctx.concatenation():
        #return 'todo_concat'
        raise VerpySyntaxError("Not supported Concat in primary")
    elif ctx.multiple_concatenation():
        #return 'todo_multiconcat'
        raise VerpySyntaxError("Not supported Concat in primary")
    elif ctx.function_call():
        return fcall2py(ctx.function_call())
    elif ctx.system_function_call():
        return fcall2py(ctx.system_function_call())
    elif ctx.constant_function_call():
        return fcall2py(ctx.constant_function_call())
    elif ctx.mintypmax_expression():
        #return 'notsupported_mintypmax'
        e = ctx.mintypmax_expression().expression()
        if len(e) > 1:
            raise VerpySyntaxError("Not supported mintypmax in primary")
        return "(" + expr2py(e[0]) + ")"
    else:
        return 'unknown_primary'

def number2py(ctx):
    t = re.sub("_", "", ctx.getText())
    if ctx.Decimal_number():
        return re.sub(r"^[0-9]*'[sS]?[dD]", "", t)
    elif ctx.Octal_number():
        return '0' + re.sub(r"^[0-9]*'[sS]?[oO]", "", t)
    elif ctx.Binary_number():
        return '0b' + re.sub(r"^[0-9]*'[sS]?[bB]", "", t)
    elif ctx.Hex_number():
        return '0x' + re.sub(r"^[0-9]*'[sS]?[hH]", "", t)
    elif ctx.Real_number():
        return t
    else:
        return '0'

def fcall2py(ctx):
    if ctx.system_function_identifier:  # remove starting '$'
        fn = "VSF__" + ctx.system_function_identifier().getText()[1:]
    elif ctx.hierarchical_function_identifier:
        fn = "unsupported_hier_function_call"
    else:
        fn = ctx.function_identifier().getText()
    if ctx.constant_expression:
        args = ctx.constant_expression()
    else:
        args = ctx.expression()
    arg = ""
    for a in args: arg += expr2py(a) + ","
    # TODO : assign back the outputs
    return "__args=[%s]; %s(__args); # assign output here" % (args, fn)

