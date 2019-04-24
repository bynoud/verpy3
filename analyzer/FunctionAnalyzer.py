

from .ModuleAnalyzer import *
from .Ver2Py import *

# use prefix '>>' to accept al child&grand child
# other prefix not letter will remove that
_defaultNodes = """
    =module_or_generate_item_declaration#inherit_from_Module
        >function_declaration
"""

# verilog-function now converted to Python-code string to be anlyzable
class FunctionAnalyzer(ModuleAnalyzer):
    def __init__(self, strOpts=None, options=None,
            parser=None, lexer=None, defaultVisit=""):
        super(FunctionAnalyzer, self).__init__(strOpts, options, parser, lexer,
                defaultVisit + " " + _defaultNodes)
        self._inFn = False

    def visitFunction_declaration(self, ctx):
        self.pushCont(self.curCont().newFunction(ctx.function_identifier().getText()))
        self._inFn = True
        self.visitGrands(ctx) # visit all grand child
        self._inFn = False
        self.popCont()

    def visitTf_declaration(self, ctx):
        if self._inFn:
            for p in ctx.list_of_port_identifiers().port_identifier():
                self.curCont().newArg(p.getText(), ctx.tf_decl_header().tfdir.text)


    def _visitVariableDecl(self, ctx):
        rname = ctx.variable_identifier().getText()
        try:
            ival = ctx.constant_expression()
        except:
            ival = None
        if ctx.dimension():
            raise VerpySyntaxError("Not support array in function yet")
        #else:
        #    #curCont.newCode("%s = %s" % (
        #    #    rname, '0' if not ival or expr2py(ival)))
        elif ival:
            self.curCont().newCode("%s = %s" % (rname, expr2py(ival)))

    def visitBlock_reg_declaration(self, ctx):
        if self._inFn:
            for r in ctx.list_of_block_variable_identifiers().block_variable_type():
                self._visitVariableDecl(r)
        else:
            self.raiseChild(ctx)


    def visitInteger_declaration(self, ctx):
        if self._inFn:
            for r in ctx.list_of_variable_identifiers().variable_type():
                self._visitVariableDecl(r)
        else:
            self.raiseChild(ctx)

    def visitLocal_parameter_declaration(self, ctx):
        if self._inFn:
            for r in ctx.list_of_param_assignments().param_assignment():
                self.curCont().newCode("%s = %s" % (
                    r.parameter_identifier().getText(),
                    expr2py(r.constant_expression())))
        else:
            self.raiseChild(ctx)

    def visitparameter_declaration(self, ctx):
        if self._inFn:
            self.visitLocal_parameter_declaration(ctx)
        else:
            self.raiseChild(ctx)

    def visitFunction_blocking_assignment(self, ctx):
        lv = ctx.variable_lvalue()
        #if lv.expression() or lv.range_expression() or lv.variable_concatenation():
        if lv.net_concatenation():
            raise VerpySyntaxError("Not support LHS concat")
        self.curCont().newCode("%s = %s" % (
            lv.hierid_reference().hierarchical_identifier().getText(),
            expr2py(ctx.expression())))

    def visitFunction_case_statement(self, ctx):
        cond = expr2py(ctx.expression())
        for c in ctx.function_case_item():
            if c.casedefault:
                self.curCont().indent("else:")
            else:
                test = "True"
                for s in c.expression(): test += " or " + expr2py(s)
                self.curCont().indent("if %s == %s:" % (cond, test))
            self.visitGrands(ctx.function_statement_or_null())
            self.curCont().dedent()

    #only need check child ctx#def visitFunction_conditional_statement(self, ctx):

    def visitFunct_stat_if(self, ctx, kw='if'):
        if kw == 'else':
            self.curCont().indent("else:")
        else:
            self.curCont().indent("%s %s:" % (kw, expr2py(ctx.expression())))
        self.visitGrands(ctx.function_statement_or_null())
        self.curCont().dedent()

    def visitFunct_stat_elseif(self, ctx):
        self.visitFunct_stat_if(ctx, 'elif')

    def visitFunct_stat_else(self, ctx):
        self.visitFunct_stat_if(ctx, 'else')

    def visitFunction_loop_statement(self, ctx):
        ival, incr, cond = {
                'forever'   : ('', '', 'True'),
                'repeat'    : ('__li=0', '__li+=1',
                                '__li < (%s)' % expr2py(ctx.expression())),
                'while'     : ('', '', expr2py(ctx.expression())),
                'for'       : ('%s=%s' % (ctx.ival.variable_lvalue().getText(),
                                          expr2py(ctx.ival.expression())),
                                '%s=%s' % (ctx.incr.variable_lvalue().getText(),
                                          expr2py(ctx.incr.expression())),
                                expr2py(ctx.expression())),
                }[ctx.loopkw.text]
        self.curCont().newCode(ival)
        self.curCont().indent('while %s:' % cond)
        self.visitGrands(ctx.function_statement())
        self.curCont().newCode(incr)
        self.curCont().dedent()

    def visitFunction_seq_block(self, ctx):
        self.curCont().indent("if True:")    # just prety?
        self.visitGrands(ctx)
        self.curCont().dedent()

    def visitDisable_statement(self, ctx):
        # assume this is disable last inner loop
        # otherwise, this will not work
        self.curCont().newCode("break")

    #def visitSystem_task_enable(self, ctx):
    #nothing need to do

