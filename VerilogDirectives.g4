/*
  Directive support for Verilog Lexer
  ALL directive should be single Token, to allow token rewrite
*/

grammar VerilogDirectives;

//dummy : (builtin | usercall)*;
//builtin : Builtin_directive ;
//usercall : User_macro_call;
//New_line : '\r'? '\n' -> skip;
//WhiteSpace : [ \t]+ -> skip;

fragment F_COND_DIRECT
    : ( 'ifdef' |
        'ifndef' |
        'else' |
        'elsif' |
        'endif'
      )
    ;

fragment F_SUPPORTED_DIRECT
    : ( 'define' |
        'undef' |
        'include' |
        'resetall' |
        'celldefine' |
        'endcelldefine' |
        'default_nettype' |
        'line' |
        'timescale' |
        'nounconnected_drive' |
        'unconnected_drive' |
        // not sure, this is used in lib cell
        'delay_mode_path' |
        'suppress_faults' |
        'enable_portfaults'
      )
    ;

fragment F_WS   : [ \t] ;
fragment F_NL   : '\r'? '\n' ;
fragment F_MCHAR : ~('\r' | '\n') | '\\' '\r'? '\n';

fragment F_SIMPLETXT : [a-zA-Z_] [a-zA-Z0-9_]*;

fragment Macro_arguments
    : '(' ( ~(')') | Macro_arguments )* ')'
    ;

Condition_directive
    : '`' F_COND_DIRECT F_MCHAR* F_NL
    ;

Builtin_directive
    : '`' F_SUPPORTED_DIRECT F_MCHAR* F_NL
    ;

User_macro_call
    : '`' F_SIMPLETXT ( F_WS* Macro_arguments )?
    ;

// supported Rules
text_macro_definition
    : text_macro_name macro_text
    ;
text_macro_name
    : text_macro_identifier ( '(' list_of_formal_arguments ')' )?
    ;
list_of_formal_arguments
    : formal_argument_identifier ( ',' formal_argument_identifier )*
    ;
text_macro_identifier
    : Simple_identifier
    ;
formal_argument_identifier
    : Simple_identifier
    ;
macro_text
    : .*;   // any character to the end

text_macro_usage
    : text_macro_identifier ( '(' expression (',' expression)* ')' )?
    ;

// place holder
expression : 'expr_holder';
Simple_identifier : 'id holder';

