
from .analyzer.ModuleAnalyzer import ModuleAnalyzer as MA
v = MA.parse( ('./tests/syntaxonly/directive.v',
               '+define+ENTHIS' )
             )
v.elaborate()
m = v.mods['legacy_direct']
with open('stub.v', 'w') as fh:
    fh.write('module %s (\n' % m.name)
    ports = m.ports
    for i,p in enumerate(ports, 1):
        fh.write('  %s %s %s%s\n' % (
            p.direction, p.ntype, p.decl,
            ',' if i<len(ports) else ''))
    fh.write(');\n')
    for p in m.outputs:
        fh.write("  assign %s = %d'b0;\n" % (p.name, p.width))
    fh.write('endmodule\n')


