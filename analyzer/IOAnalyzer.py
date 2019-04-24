

from .BaseAnalyzer import *
#from __builtin__ import classmethod

# use prefix '>>' to accept al child&grand child
# other prefix not letter will remove that
_defaultNodes = """
    vfile description
        >module_declaration
            module_parameter_port_list
                >parameter_declaration_
            >>list_of_ports
                #accept_this
                    ?port_identifier
                    >port_reference
            list_of_port_declarations
                >port_declaration
            module_item non_port_module_item
                parameter_declaration
                    >parameter_declaration_
                >local_parameter_declaration
                module_or_generate_item
                    module_or_generate_item_declaration
                        >net_declaration
                        >reg_declaration
"""

# from Liclipse
class IOAnalyzer(BaseAnalyzer):
    def __init__(self, strOpts=None, options=None,
            parser=None, lexer=None, defaultVisit=""):
        super(IOAnalyzer, self).__init__(strOpts, options, parser, lexer,
                defaultVisit + " " + _defaultNodes)

    def visitModule_declaration(self, ctx):
        m = self.curCont().newModule(ctx.module_identifier().getText(),
                              ctx.module_keyword().getText())
        self.pushCont(m)
        self.visitChilds(ctx)
        self.popCont()

    def visitParameter_declaration_(self, ctx):
        # just ignore the 'range_'
        for c in ctx.list_of_param_assignments().param_assignment():
            self.curCont().newParam(c.parameter_identifier().getText(),
                             c.constant_expression().getText())

    def visitLocal_parameter_declaration(self, ctx):
        for c in ctx.list_of_param_assignments().param_assignment():
            self.curCont().newLocalparam(c.parameter_identifier().getText(),
                                  c.constant_expression().getText())

    # port header inside module <name> (portname [...] , portname, [...])
    def visitPort_reference(self, ctx):
        p = self.curCont().newPortHeader(ctx.port_identifier().getText())
        if ctx.constant_expression():
            p.refBus([[ctx.constant_expression().getText()]*2])
        elif ctx.range_expression():
            p.refBus(range2arr(ctx.range_expression()))

    # port declare inside module <name> ( input ..., out ...)
    # or declare after module <name (...); input ...
    def visitPort_declaration(self, ctx):
        nt = 'wire'
        if ctx.net_type() != None : nt = ctx.net_type().getText()
        elif ctx.regtype != None  : nt = ctx.regtype.text
        parr = range2arr(ctx.range_())
        for pctx in ctx.list_of_port_identifiers().port_identifier():
            p = self.curCont().newPort(pctx.getText(), ctx.portkw.text, nt)
            p.declBus(parr)

    # net decl
    def visitNet_declaration(self, ctx):
        nt = ctx.net_type().getText() if ctx.net_type() else ctx.regtype.text
        parr = range2arr(ctx.range_())
        if ctx.list_of_net_identifiers() != None:
            for nctx in ctx.list_of_net_identifiers().net_identifier_wrange():
                n = self.curCont().newNet(nctx.net_identifier().getText(), nt)
                n.declBus(parr, dim2arr(nctx.dimension()))
        else:
            for nctx in ctx.list_of_net_decl_assignments().net_decl_assignment():
                n = self.curCont().newNet(nctx.net_identifier().getText(), nt)
                n.declBus(parr)

    # reg decl
    def visitReg_declaration(self, ctx):
        parr = range2arr(ctx.range_())
        for nctx in ctx.list_of_variable_identifiers().variable_type():
            n = self.curCont().newNet(nctx.variable_identifier().getText(), 'reg')
            n.declBus(parr, dim2arr(nctx.dimension()))

