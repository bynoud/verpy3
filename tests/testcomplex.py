

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

from verpy.analyzer.IOAnalyzer import IOAnalyzer

#opts = AnalyzerOption('+define+ENTHIS')
#opts = AnalyzerOption('+define+ENTHAT')
#opts = AnalyzerOption('+incdir+./tests/syntaxonly')
#v = ModuleAnalyzer.parse(filename='./tests/syntaxonly/directive.v',
#                         #LexerClass=PreprocLexer,
#                         #lexerInitOpt={'options':opts}
#                         optstr='+incdir+./tests/syntaxonly'
#                         )
#v = ModuleAnalyzer.parse( ( './syntaxonly/legacyver.v',
try:
    v = IOAnalyzer.parse( './munit_excl_mon.sv' )
except Exception as e:
    print("FAILED: %s" % e)
    exit()
v.dump()
v.link()
print("---- linked")
v.dump()
v.elaborate()
print("----- elabed")
v.dump()
