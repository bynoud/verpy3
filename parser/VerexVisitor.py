# Generated from Verex.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VerexParser import VerexParser
else:
    from VerexParser import VerexParser

# This class defines a complete generic visitor for a parse tree produced by VerexParser.

class VerexVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VerexParser#vfile.
    def visitVfile(self, ctx:VerexParser.VfileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#description.
    def visitDescription(self, ctx:VerexParser.DescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_declaration.
    def visitModule_declaration(self, ctx:VerexParser.Module_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#integer_declaration.
    def visitInteger_declaration(self, ctx:VerexParser.Integer_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#integer_kw.
    def visitInteger_kw(self, ctx:VerexParser.Integer_kwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#HeaderPortName.
    def visitHeaderPortName(self, ctx:VerexParser.HeaderPortNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#HeaderPortAssign.
    def visitHeaderPortAssign(self, ctx:VerexParser.HeaderPortAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#port_reference.
    def visitPort_reference(self, ctx:VerexParser.Port_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#port_declaration.
    def visitPort_declaration(self, ctx:VerexParser.Port_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_port_identifiers_wrange.
    def visitList_of_port_identifiers_wrange(self, ctx:VerexParser.List_of_port_identifiers_wrangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#port_identifier_wrange.
    def visitPort_identifier_wrange(self, ctx:VerexParser.Port_identifier_wrangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#local_parameter_declaration.
    def visitLocal_parameter_declaration(self, ctx:VerexParser.Local_parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#parameter_declaration_.
    def visitParameter_declaration_(self, ctx:VerexParser.Parameter_declaration_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#net_declaration.
    def visitNet_declaration(self, ctx:VerexParser.Net_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_net_identifiers.
    def visitList_of_net_identifiers(self, ctx:VerexParser.List_of_net_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#net_identifier_wrange.
    def visitNet_identifier_wrange(self, ctx:VerexParser.Net_identifier_wrangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#net_lvalue.
    def visitNet_lvalue(self, ctx:VerexParser.Net_lvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#net_concatenation_value.
    def visitNet_concatenation_value(self, ctx:VerexParser.Net_concatenation_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#variable_lvalue.
    def visitVariable_lvalue(self, ctx:VerexParser.Variable_lvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#expression.
    def visitExpression(self, ctx:VerexParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#inc_or_dec_expression.
    def visitInc_or_dec_expression(self, ctx:VerexParser.Inc_or_dec_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#primary.
    def visitPrimary(self, ctx:VerexParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#hierid_reference.
    def visitHierid_reference(self, ctx:VerexParser.Hierid_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#escaped_hierarchical_identifier.
    def visitEscaped_hierarchical_identifier(self, ctx:VerexParser.Escaped_hierarchical_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#simple_hierarchical_identifier.
    def visitSimple_hierarchical_identifier(self, ctx:VerexParser.Simple_hierarchical_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#conditional_statement.
    def visitConditional_statement(self, ctx:VerexParser.Conditional_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#stat_if.
    def visitStat_if(self, ctx:VerexParser.Stat_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#stat_elseif.
    def visitStat_elseif(self, ctx:VerexParser.Stat_elseifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#stat_else.
    def visitStat_else(self, ctx:VerexParser.Stat_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_conditional_statement.
    def visitFunction_conditional_statement(self, ctx:VerexParser.Function_conditional_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#funct_stat_if.
    def visitFunct_stat_if(self, ctx:VerexParser.Funct_stat_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#funct_stat_elseif.
    def visitFunct_stat_elseif(self, ctx:VerexParser.Funct_stat_elseifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#funct_stat_else.
    def visitFunct_stat_else(self, ctx:VerexParser.Funct_stat_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#arrayed_identifier.
    def visitArrayed_identifier(self, ctx:VerexParser.Arrayed_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#regex_arrayed_identifier.
    def visitRegex_arrayed_identifier(self, ctx:VerexParser.Regex_arrayed_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#identifier.
    def visitIdentifier(self, ctx:VerexParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_parameter_assignments.
    def visitList_of_parameter_assignments(self, ctx:VerexParser.List_of_parameter_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#equal_parameter_assignment.
    def visitEqual_parameter_assignment(self, ctx:VerexParser.Equal_parameter_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_instance.
    def visitModule_instance(self, ctx:VerexParser.Module_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#special_port_connection.
    def visitSpecial_port_connection(self, ctx:VerexParser.Special_port_connectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#comma_special_port_connection.
    def visitComma_special_port_connection(self, ctx:VerexParser.Comma_special_port_connectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_port_connections.
    def visitList_of_port_connections(self, ctx:VerexParser.List_of_port_connectionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#mixed_port_connection.
    def visitMixed_port_connection(self, ctx:VerexParser.Mixed_port_connectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#comma_mixed_port_connection.
    def visitComma_mixed_port_connection(self, ctx:VerexParser.Comma_mixed_port_connectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#port_connection_expression.
    def visitPort_connection_expression(self, ctx:VerexParser.Port_connection_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#range_.
    def visitRange_(self, ctx:VerexParser.Range_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#range_expression.
    def visitRange_expression(self, ctx:VerexParser.Range_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#dimension.
    def visitDimension(self, ctx:VerexParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#text_macro_definition.
    def visitText_macro_definition(self, ctx:VerexParser.Text_macro_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#text_macro_name.
    def visitText_macro_name(self, ctx:VerexParser.Text_macro_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_formal_arguments.
    def visitList_of_formal_arguments(self, ctx:VerexParser.List_of_formal_argumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#text_macro_identifier.
    def visitText_macro_identifier(self, ctx:VerexParser.Text_macro_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#formal_argument_identifier.
    def visitFormal_argument_identifier(self, ctx:VerexParser.Formal_argument_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#macro_text.
    def visitMacro_text(self, ctx:VerexParser.Macro_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#text_macro_usage.
    def visitText_macro_usage(self, ctx:VerexParser.Text_macro_usageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#config_declaration.
    def visitConfig_declaration(self, ctx:VerexParser.Config_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#design_statement.
    def visitDesign_statement(self, ctx:VerexParser.Design_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#config_rule_statement.
    def visitConfig_rule_statement(self, ctx:VerexParser.Config_rule_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#default_clause.
    def visitDefault_clause(self, ctx:VerexParser.Default_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#inst_clause.
    def visitInst_clause(self, ctx:VerexParser.Inst_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#inst_name.
    def visitInst_name(self, ctx:VerexParser.Inst_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#liblist_clause.
    def visitLiblist_clause(self, ctx:VerexParser.Liblist_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#cell_clause.
    def visitCell_clause(self, ctx:VerexParser.Cell_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#use_clause.
    def visitUse_clause(self, ctx:VerexParser.Use_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#source_text.
    def visitSource_text(self, ctx:VerexParser.Source_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_keyword.
    def visitModule_keyword(self, ctx:VerexParser.Module_keywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_parameter_port_list.
    def visitModule_parameter_port_list(self, ctx:VerexParser.Module_parameter_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_ports.
    def visitList_of_ports(self, ctx:VerexParser.List_of_portsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_port_declarations.
    def visitList_of_port_declarations(self, ctx:VerexParser.List_of_port_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#port_expression.
    def visitPort_expression(self, ctx:VerexParser.Port_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_item.
    def visitModule_item(self, ctx:VerexParser.Module_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_or_generate_item.
    def visitModule_or_generate_item(self, ctx:VerexParser.Module_or_generate_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#non_port_module_item.
    def visitNon_port_module_item(self, ctx:VerexParser.Non_port_module_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_or_generate_item_declaration.
    def visitModule_or_generate_item_declaration(self, ctx:VerexParser.Module_or_generate_item_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#parameter_override.
    def visitParameter_override(self, ctx:VerexParser.Parameter_overrideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#parameter_declaration.
    def visitParameter_declaration(self, ctx:VerexParser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#specparam_declaration.
    def visitSpecparam_declaration(self, ctx:VerexParser.Specparam_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#inout_declaration.
    def visitInout_declaration(self, ctx:VerexParser.Inout_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#input_declaration.
    def visitInput_declaration(self, ctx:VerexParser.Input_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#output_declaration.
    def visitOutput_declaration(self, ctx:VerexParser.Output_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#event_declaration.
    def visitEvent_declaration(self, ctx:VerexParser.Event_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#genvar_declaration.
    def visitGenvar_declaration(self, ctx:VerexParser.Genvar_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#time_declaration.
    def visitTime_declaration(self, ctx:VerexParser.Time_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#real_declaration.
    def visitReal_declaration(self, ctx:VerexParser.Real_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#realtime_declaration.
    def visitRealtime_declaration(self, ctx:VerexParser.Realtime_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#reg_declaration.
    def visitReg_declaration(self, ctx:VerexParser.Reg_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#net_type.
    def visitNet_type(self, ctx:VerexParser.Net_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#output_variable_type.
    def visitOutput_variable_type(self, ctx:VerexParser.Output_variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#real_type.
    def visitReal_type(self, ctx:VerexParser.Real_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#variable_type.
    def visitVariable_type(self, ctx:VerexParser.Variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#drive_strength.
    def visitDrive_strength(self, ctx:VerexParser.Drive_strengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#strength0.
    def visitStrength0(self, ctx:VerexParser.Strength0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#strength1.
    def visitStrength1(self, ctx:VerexParser.Strength1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#charge_strength.
    def visitCharge_strength(self, ctx:VerexParser.Charge_strengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#delay3.
    def visitDelay3(self, ctx:VerexParser.Delay3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#delay2.
    def visitDelay2(self, ctx:VerexParser.Delay2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#delay_value.
    def visitDelay_value(self, ctx:VerexParser.Delay_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_event_identifiers.
    def visitList_of_event_identifiers(self, ctx:VerexParser.List_of_event_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_genvar_identifiers.
    def visitList_of_genvar_identifiers(self, ctx:VerexParser.List_of_genvar_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_port_identifiers.
    def visitList_of_port_identifiers(self, ctx:VerexParser.List_of_port_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_net_decl_assignments.
    def visitList_of_net_decl_assignments(self, ctx:VerexParser.List_of_net_decl_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_param_assignments.
    def visitList_of_param_assignments(self, ctx:VerexParser.List_of_param_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_specparam_assignments.
    def visitList_of_specparam_assignments(self, ctx:VerexParser.List_of_specparam_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_real_identifiers.
    def visitList_of_real_identifiers(self, ctx:VerexParser.List_of_real_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_variable_identifiers.
    def visitList_of_variable_identifiers(self, ctx:VerexParser.List_of_variable_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_variable_port_identifiers.
    def visitList_of_variable_port_identifiers(self, ctx:VerexParser.List_of_variable_port_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#net_decl_assignment.
    def visitNet_decl_assignment(self, ctx:VerexParser.Net_decl_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#param_assignment.
    def visitParam_assignment(self, ctx:VerexParser.Param_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#specparam_assignment.
    def visitSpecparam_assignment(self, ctx:VerexParser.Specparam_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#pulse_control_specparam.
    def visitPulse_control_specparam(self, ctx:VerexParser.Pulse_control_specparamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#error_limit_value.
    def visitError_limit_value(self, ctx:VerexParser.Error_limit_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#reject_limit_value.
    def visitReject_limit_value(self, ctx:VerexParser.Reject_limit_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#limit_value.
    def visitLimit_value(self, ctx:VerexParser.Limit_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_declaration.
    def visitFunction_declaration(self, ctx:VerexParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_item_declaration.
    def visitFunction_item_declaration(self, ctx:VerexParser.Function_item_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_port_list.
    def visitFunction_port_list(self, ctx:VerexParser.Function_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_port.
    def visitFunction_port(self, ctx:VerexParser.Function_portContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#range_or_type.
    def visitRange_or_type(self, ctx:VerexParser.Range_or_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#task_declaration.
    def visitTask_declaration(self, ctx:VerexParser.Task_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#task_item_declaration.
    def visitTask_item_declaration(self, ctx:VerexParser.Task_item_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#task_port_list.
    def visitTask_port_list(self, ctx:VerexParser.Task_port_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#task_port_item.
    def visitTask_port_item(self, ctx:VerexParser.Task_port_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#tf_decl_header.
    def visitTf_decl_header(self, ctx:VerexParser.Tf_decl_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#tf_declaration.
    def visitTf_declaration(self, ctx:VerexParser.Tf_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#task_port_type.
    def visitTask_port_type(self, ctx:VerexParser.Task_port_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#block_item_declaration.
    def visitBlock_item_declaration(self, ctx:VerexParser.Block_item_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#block_reg_declaration.
    def visitBlock_reg_declaration(self, ctx:VerexParser.Block_reg_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_block_variable_identifiers.
    def visitList_of_block_variable_identifiers(self, ctx:VerexParser.List_of_block_variable_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#block_variable_type.
    def visitBlock_variable_type(self, ctx:VerexParser.Block_variable_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#gate_instantiation.
    def visitGate_instantiation(self, ctx:VerexParser.Gate_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#cmos_switch_instance.
    def visitCmos_switch_instance(self, ctx:VerexParser.Cmos_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#enable_gate_instance.
    def visitEnable_gate_instance(self, ctx:VerexParser.Enable_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#mos_switch_instance.
    def visitMos_switch_instance(self, ctx:VerexParser.Mos_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#n_input_gate_instance.
    def visitN_input_gate_instance(self, ctx:VerexParser.N_input_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#n_output_gate_instance.
    def visitN_output_gate_instance(self, ctx:VerexParser.N_output_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#pass_switch_instance.
    def visitPass_switch_instance(self, ctx:VerexParser.Pass_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#pass_enable_switch_instance.
    def visitPass_enable_switch_instance(self, ctx:VerexParser.Pass_enable_switch_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#pull_gate_instance.
    def visitPull_gate_instance(self, ctx:VerexParser.Pull_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#name_of_gate_instance.
    def visitName_of_gate_instance(self, ctx:VerexParser.Name_of_gate_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#pulldown_strength.
    def visitPulldown_strength(self, ctx:VerexParser.Pulldown_strengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#pullup_strength.
    def visitPullup_strength(self, ctx:VerexParser.Pullup_strengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#enable_terminal.
    def visitEnable_terminal(self, ctx:VerexParser.Enable_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#ncontrol_terminal.
    def visitNcontrol_terminal(self, ctx:VerexParser.Ncontrol_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#pcontrol_terminal.
    def visitPcontrol_terminal(self, ctx:VerexParser.Pcontrol_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#input_terminal.
    def visitInput_terminal(self, ctx:VerexParser.Input_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#inout_terminal.
    def visitInout_terminal(self, ctx:VerexParser.Inout_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#output_terminal.
    def visitOutput_terminal(self, ctx:VerexParser.Output_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#cmos_switchtype.
    def visitCmos_switchtype(self, ctx:VerexParser.Cmos_switchtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#enable_gatetype.
    def visitEnable_gatetype(self, ctx:VerexParser.Enable_gatetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#mos_switchtype.
    def visitMos_switchtype(self, ctx:VerexParser.Mos_switchtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#n_input_gatetype.
    def visitN_input_gatetype(self, ctx:VerexParser.N_input_gatetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#n_output_gatetype.
    def visitN_output_gatetype(self, ctx:VerexParser.N_output_gatetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#pass_en_switchtype.
    def visitPass_en_switchtype(self, ctx:VerexParser.Pass_en_switchtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#pass_switchtype.
    def visitPass_switchtype(self, ctx:VerexParser.Pass_switchtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_instantiation.
    def visitModule_instantiation(self, ctx:VerexParser.Module_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#parameter_value_assignment.
    def visitParameter_value_assignment(self, ctx:VerexParser.Parameter_value_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#ordered_parameter_assignment.
    def visitOrdered_parameter_assignment(self, ctx:VerexParser.Ordered_parameter_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#named_parameter_assignment.
    def visitNamed_parameter_assignment(self, ctx:VerexParser.Named_parameter_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#name_of_instance.
    def visitName_of_instance(self, ctx:VerexParser.Name_of_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#ordered_port_connection.
    def visitOrdered_port_connection(self, ctx:VerexParser.Ordered_port_connectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#named_port_connection.
    def visitNamed_port_connection(self, ctx:VerexParser.Named_port_connectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#generated_instantiation.
    def visitGenerated_instantiation(self, ctx:VerexParser.Generated_instantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#generate_item_or_null.
    def visitGenerate_item_or_null(self, ctx:VerexParser.Generate_item_or_nullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#generate_item.
    def visitGenerate_item(self, ctx:VerexParser.Generate_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#generate_conditional_statement.
    def visitGenerate_conditional_statement(self, ctx:VerexParser.Generate_conditional_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#generate_case_statement.
    def visitGenerate_case_statement(self, ctx:VerexParser.Generate_case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#genvar_case_item.
    def visitGenvar_case_item(self, ctx:VerexParser.Genvar_case_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#generate_loop_statement.
    def visitGenerate_loop_statement(self, ctx:VerexParser.Generate_loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#genvar_assignment.
    def visitGenvar_assignment(self, ctx:VerexParser.Genvar_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#generate_block.
    def visitGenerate_block(self, ctx:VerexParser.Generate_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#continuous_assign.
    def visitContinuous_assign(self, ctx:VerexParser.Continuous_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_net_assignments.
    def visitList_of_net_assignments(self, ctx:VerexParser.List_of_net_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#net_assignment.
    def visitNet_assignment(self, ctx:VerexParser.Net_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#initial_construct.
    def visitInitial_construct(self, ctx:VerexParser.Initial_constructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#always_construct.
    def visitAlways_construct(self, ctx:VerexParser.Always_constructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#blocking_assignment.
    def visitBlocking_assignment(self, ctx:VerexParser.Blocking_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#nonblocking_assignment.
    def visitNonblocking_assignment(self, ctx:VerexParser.Nonblocking_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#procedural_continuous_assignments.
    def visitProcedural_continuous_assignments(self, ctx:VerexParser.Procedural_continuous_assignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_blocking_assignment.
    def visitFunction_blocking_assignment(self, ctx:VerexParser.Function_blocking_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_statement_or_null.
    def visitFunction_statement_or_null(self, ctx:VerexParser.Function_statement_or_nullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_seq_block.
    def visitFunction_seq_block(self, ctx:VerexParser.Function_seq_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#variable_assignment.
    def visitVariable_assignment(self, ctx:VerexParser.Variable_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#par_block.
    def visitPar_block(self, ctx:VerexParser.Par_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#seq_block.
    def visitSeq_block(self, ctx:VerexParser.Seq_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#statement.
    def visitStatement(self, ctx:VerexParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#statement_or_null.
    def visitStatement_or_null(self, ctx:VerexParser.Statement_or_nullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_statement.
    def visitFunction_statement(self, ctx:VerexParser.Function_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#delay_or_event_control.
    def visitDelay_or_event_control(self, ctx:VerexParser.Delay_or_event_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#delay_control.
    def visitDelay_control(self, ctx:VerexParser.Delay_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#disable_statement.
    def visitDisable_statement(self, ctx:VerexParser.Disable_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#event_control.
    def visitEvent_control(self, ctx:VerexParser.Event_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#event_trigger.
    def visitEvent_trigger(self, ctx:VerexParser.Event_triggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#event_expression.
    def visitEvent_expression(self, ctx:VerexParser.Event_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#event_primary.
    def visitEvent_primary(self, ctx:VerexParser.Event_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#procedural_timing_control_statement.
    def visitProcedural_timing_control_statement(self, ctx:VerexParser.Procedural_timing_control_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#wait_statement.
    def visitWait_statement(self, ctx:VerexParser.Wait_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#if_else_if_statement.
    def visitIf_else_if_statement(self, ctx:VerexParser.If_else_if_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_if_else_if_statement.
    def visitFunction_if_else_if_statement(self, ctx:VerexParser.Function_if_else_if_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#case_statement.
    def visitCase_statement(self, ctx:VerexParser.Case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#case_item.
    def visitCase_item(self, ctx:VerexParser.Case_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_case_statement.
    def visitFunction_case_statement(self, ctx:VerexParser.Function_case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_case_item.
    def visitFunction_case_item(self, ctx:VerexParser.Function_case_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_loop_statement.
    def visitFunction_loop_statement(self, ctx:VerexParser.Function_loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#loop_statement.
    def visitLoop_statement(self, ctx:VerexParser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#system_task_enable.
    def visitSystem_task_enable(self, ctx:VerexParser.System_task_enableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#task_enable.
    def visitTask_enable(self, ctx:VerexParser.Task_enableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#specify_block.
    def visitSpecify_block(self, ctx:VerexParser.Specify_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#specify_item.
    def visitSpecify_item(self, ctx:VerexParser.Specify_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#pulsestyle_declaration.
    def visitPulsestyle_declaration(self, ctx:VerexParser.Pulsestyle_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#showcancelled_declaration.
    def visitShowcancelled_declaration(self, ctx:VerexParser.Showcancelled_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#path_declaration.
    def visitPath_declaration(self, ctx:VerexParser.Path_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#simple_path_declaration.
    def visitSimple_path_declaration(self, ctx:VerexParser.Simple_path_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#parallel_path_description.
    def visitParallel_path_description(self, ctx:VerexParser.Parallel_path_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#full_path_description.
    def visitFull_path_description(self, ctx:VerexParser.Full_path_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_path_inputs.
    def visitList_of_path_inputs(self, ctx:VerexParser.List_of_path_inputsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_path_outputs.
    def visitList_of_path_outputs(self, ctx:VerexParser.List_of_path_outputsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#specify_input_terminal_descriptor.
    def visitSpecify_input_terminal_descriptor(self, ctx:VerexParser.Specify_input_terminal_descriptorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#specify_output_terminal_descriptor.
    def visitSpecify_output_terminal_descriptor(self, ctx:VerexParser.Specify_output_terminal_descriptorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#input_identifier.
    def visitInput_identifier(self, ctx:VerexParser.Input_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#output_identifier.
    def visitOutput_identifier(self, ctx:VerexParser.Output_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#path_delay_value.
    def visitPath_delay_value(self, ctx:VerexParser.Path_delay_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#list_of_path_delay_expressions.
    def visitList_of_path_delay_expressions(self, ctx:VerexParser.List_of_path_delay_expressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#t_path_delay_expression.
    def visitT_path_delay_expression(self, ctx:VerexParser.T_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#trise_path_delay_expression.
    def visitTrise_path_delay_expression(self, ctx:VerexParser.Trise_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#tfall_path_delay_expression.
    def visitTfall_path_delay_expression(self, ctx:VerexParser.Tfall_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#tz_path_delay_expression.
    def visitTz_path_delay_expression(self, ctx:VerexParser.Tz_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#t01_path_delay_expression.
    def visitT01_path_delay_expression(self, ctx:VerexParser.T01_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#t10_path_delay_expression.
    def visitT10_path_delay_expression(self, ctx:VerexParser.T10_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#t0z_path_delay_expression.
    def visitT0z_path_delay_expression(self, ctx:VerexParser.T0z_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#tz1_path_delay_expression.
    def visitTz1_path_delay_expression(self, ctx:VerexParser.Tz1_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#t1z_path_delay_expression.
    def visitT1z_path_delay_expression(self, ctx:VerexParser.T1z_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#tz0_path_delay_expression.
    def visitTz0_path_delay_expression(self, ctx:VerexParser.Tz0_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#t0x_path_delay_expression.
    def visitT0x_path_delay_expression(self, ctx:VerexParser.T0x_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#tx1_path_delay_expression.
    def visitTx1_path_delay_expression(self, ctx:VerexParser.Tx1_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#t1x_path_delay_expression.
    def visitT1x_path_delay_expression(self, ctx:VerexParser.T1x_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#tx0_path_delay_expression.
    def visitTx0_path_delay_expression(self, ctx:VerexParser.Tx0_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#txz_path_delay_expression.
    def visitTxz_path_delay_expression(self, ctx:VerexParser.Txz_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#tzx_path_delay_expression.
    def visitTzx_path_delay_expression(self, ctx:VerexParser.Tzx_path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#path_delay_expression.
    def visitPath_delay_expression(self, ctx:VerexParser.Path_delay_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#edge_sensitive_path_declaration.
    def visitEdge_sensitive_path_declaration(self, ctx:VerexParser.Edge_sensitive_path_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#parallel_edge_sensitive_path_description.
    def visitParallel_edge_sensitive_path_description(self, ctx:VerexParser.Parallel_edge_sensitive_path_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#full_edge_sensitive_path_description.
    def visitFull_edge_sensitive_path_description(self, ctx:VerexParser.Full_edge_sensitive_path_descriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#data_source_expression.
    def visitData_source_expression(self, ctx:VerexParser.Data_source_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#edge_identifier.
    def visitEdge_identifier(self, ctx:VerexParser.Edge_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#state_dependent_path_declaration.
    def visitState_dependent_path_declaration(self, ctx:VerexParser.State_dependent_path_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#polarity_operator.
    def visitPolarity_operator(self, ctx:VerexParser.Polarity_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#checktime_condition.
    def visitChecktime_condition(self, ctx:VerexParser.Checktime_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#delayed_data.
    def visitDelayed_data(self, ctx:VerexParser.Delayed_dataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#delayed_reference.
    def visitDelayed_reference(self, ctx:VerexParser.Delayed_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#end_edge_offset.
    def visitEnd_edge_offset(self, ctx:VerexParser.End_edge_offsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#event_based_flag.
    def visitEvent_based_flag(self, ctx:VerexParser.Event_based_flagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#notify_reg.
    def visitNotify_reg(self, ctx:VerexParser.Notify_regContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#remain_active_flag.
    def visitRemain_active_flag(self, ctx:VerexParser.Remain_active_flagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#stamptime_condition.
    def visitStamptime_condition(self, ctx:VerexParser.Stamptime_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#start_edge_offset.
    def visitStart_edge_offset(self, ctx:VerexParser.Start_edge_offsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#threshold.
    def visitThreshold(self, ctx:VerexParser.ThresholdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#timing_check_limit.
    def visitTiming_check_limit(self, ctx:VerexParser.Timing_check_limitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#concatenation.
    def visitConcatenation(self, ctx:VerexParser.ConcatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#constant_concatenation.
    def visitConstant_concatenation(self, ctx:VerexParser.Constant_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#constant_multiple_concatenation.
    def visitConstant_multiple_concatenation(self, ctx:VerexParser.Constant_multiple_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_path_concatenation.
    def visitModule_path_concatenation(self, ctx:VerexParser.Module_path_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_path_multiple_concatenation.
    def visitModule_path_multiple_concatenation(self, ctx:VerexParser.Module_path_multiple_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#multiple_concatenation.
    def visitMultiple_concatenation(self, ctx:VerexParser.Multiple_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#net_concatenation.
    def visitNet_concatenation(self, ctx:VerexParser.Net_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#variable_concatenation.
    def visitVariable_concatenation(self, ctx:VerexParser.Variable_concatenationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#variable_concatenation_value.
    def visitVariable_concatenation_value(self, ctx:VerexParser.Variable_concatenation_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#constant_function_call.
    def visitConstant_function_call(self, ctx:VerexParser.Constant_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_call.
    def visitFunction_call(self, ctx:VerexParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#system_function_call.
    def visitSystem_function_call(self, ctx:VerexParser.System_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#genvar_function_call.
    def visitGenvar_function_call(self, ctx:VerexParser.Genvar_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#base_expression.
    def visitBase_expression(self, ctx:VerexParser.Base_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#constant_base_expression.
    def visitConstant_base_expression(self, ctx:VerexParser.Constant_base_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#constant_expression.
    def visitConstant_expression(self, ctx:VerexParser.Constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#constant_mintypmax_expression.
    def visitConstant_mintypmax_expression(self, ctx:VerexParser.Constant_mintypmax_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#constant_range_expression.
    def visitConstant_range_expression(self, ctx:VerexParser.Constant_range_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#dimension_constant_expression.
    def visitDimension_constant_expression(self, ctx:VerexParser.Dimension_constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#term.
    def visitTerm(self, ctx:VerexParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#lsb_constant_expression.
    def visitLsb_constant_expression(self, ctx:VerexParser.Lsb_constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#mintypmax_expression.
    def visitMintypmax_expression(self, ctx:VerexParser.Mintypmax_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_path_conditional_expression.
    def visitModule_path_conditional_expression(self, ctx:VerexParser.Module_path_conditional_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_path_expression.
    def visitModule_path_expression(self, ctx:VerexParser.Module_path_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_path_mintypmax_expression.
    def visitModule_path_mintypmax_expression(self, ctx:VerexParser.Module_path_mintypmax_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#msb_constant_expression.
    def visitMsb_constant_expression(self, ctx:VerexParser.Msb_constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#width_constant_expression.
    def visitWidth_constant_expression(self, ctx:VerexParser.Width_constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#constant_primary.
    def visitConstant_primary(self, ctx:VerexParser.Constant_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_path_primary.
    def visitModule_path_primary(self, ctx:VerexParser.Module_path_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#unary_operator.
    def visitUnary_operator(self, ctx:VerexParser.Unary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#binary_operator.
    def visitBinary_operator(self, ctx:VerexParser.Binary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#unary_module_path_operator.
    def visitUnary_module_path_operator(self, ctx:VerexParser.Unary_module_path_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#binary_module_path_operator.
    def visitBinary_module_path_operator(self, ctx:VerexParser.Binary_module_path_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#number.
    def visitNumber(self, ctx:VerexParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#timing_spec.
    def visitTiming_spec(self, ctx:VerexParser.Timing_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#attribute_instance.
    def visitAttribute_instance(self, ctx:VerexParser.Attribute_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#attr_spec.
    def visitAttr_spec(self, ctx:VerexParser.Attr_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#attr_name.
    def visitAttr_name(self, ctx:VerexParser.Attr_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#block_identifier.
    def visitBlock_identifier(self, ctx:VerexParser.Block_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#cell_identifier.
    def visitCell_identifier(self, ctx:VerexParser.Cell_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#config_identifier.
    def visitConfig_identifier(self, ctx:VerexParser.Config_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#escaped_arrayed_identifier.
    def visitEscaped_arrayed_identifier(self, ctx:VerexParser.Escaped_arrayed_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#event_identifier.
    def visitEvent_identifier(self, ctx:VerexParser.Event_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#function_identifier.
    def visitFunction_identifier(self, ctx:VerexParser.Function_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#gate_instance_identifier.
    def visitGate_instance_identifier(self, ctx:VerexParser.Gate_instance_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#generate_block_identifier.
    def visitGenerate_block_identifier(self, ctx:VerexParser.Generate_block_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#genvar_function_identifier.
    def visitGenvar_function_identifier(self, ctx:VerexParser.Genvar_function_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#genvar_identifier.
    def visitGenvar_identifier(self, ctx:VerexParser.Genvar_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#hierarchical_block_identifier.
    def visitHierarchical_block_identifier(self, ctx:VerexParser.Hierarchical_block_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#hierarchical_event_identifier.
    def visitHierarchical_event_identifier(self, ctx:VerexParser.Hierarchical_event_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#hierarchical_function_identifier.
    def visitHierarchical_function_identifier(self, ctx:VerexParser.Hierarchical_function_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#hierarchical_identifier.
    def visitHierarchical_identifier(self, ctx:VerexParser.Hierarchical_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#hierarchical_net_identifier.
    def visitHierarchical_net_identifier(self, ctx:VerexParser.Hierarchical_net_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#hierarchical_variable_identifier.
    def visitHierarchical_variable_identifier(self, ctx:VerexParser.Hierarchical_variable_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#hierarchical_task_identifier.
    def visitHierarchical_task_identifier(self, ctx:VerexParser.Hierarchical_task_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#inout_port_identifier.
    def visitInout_port_identifier(self, ctx:VerexParser.Inout_port_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#input_port_identifier.
    def visitInput_port_identifier(self, ctx:VerexParser.Input_port_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#instance_identifier.
    def visitInstance_identifier(self, ctx:VerexParser.Instance_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#library_identifier.
    def visitLibrary_identifier(self, ctx:VerexParser.Library_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#memory_identifier.
    def visitMemory_identifier(self, ctx:VerexParser.Memory_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_identifier.
    def visitModule_identifier(self, ctx:VerexParser.Module_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#module_instance_identifier.
    def visitModule_instance_identifier(self, ctx:VerexParser.Module_instance_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#net_identifier.
    def visitNet_identifier(self, ctx:VerexParser.Net_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#output_port_identifier.
    def visitOutput_port_identifier(self, ctx:VerexParser.Output_port_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#parameter_identifier.
    def visitParameter_identifier(self, ctx:VerexParser.Parameter_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#port_identifier.
    def visitPort_identifier(self, ctx:VerexParser.Port_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#real_identifier.
    def visitReal_identifier(self, ctx:VerexParser.Real_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#simple_arrayed_identifier.
    def visitSimple_arrayed_identifier(self, ctx:VerexParser.Simple_arrayed_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#specparam_identifier.
    def visitSpecparam_identifier(self, ctx:VerexParser.Specparam_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#system_function_identifier.
    def visitSystem_function_identifier(self, ctx:VerexParser.System_function_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#system_task_identifier.
    def visitSystem_task_identifier(self, ctx:VerexParser.System_task_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#task_identifier.
    def visitTask_identifier(self, ctx:VerexParser.Task_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#terminal_identifier.
    def visitTerminal_identifier(self, ctx:VerexParser.Terminal_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#topmodule_identifier.
    def visitTopmodule_identifier(self, ctx:VerexParser.Topmodule_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#udp_identifier.
    def visitUdp_identifier(self, ctx:VerexParser.Udp_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#udp_instance_identifier.
    def visitUdp_instance_identifier(self, ctx:VerexParser.Udp_instance_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#variable_identifier.
    def visitVariable_identifier(self, ctx:VerexParser.Variable_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#simple_hierarchical_branch.
    def visitSimple_hierarchical_branch(self, ctx:VerexParser.Simple_hierarchical_branchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerexParser#escaped_hierarchical_branch.
    def visitEscaped_hierarchical_branch(self, ctx:VerexParser.Escaped_hierarchical_branchContext):
        return self.visitChildren(ctx)



del VerexParser