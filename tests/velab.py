
import logging, sys
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

from verpy.analyzer.FunctionAnalyzer import FunctionAnalyzer as VA

#opts = AnalyzerOption('+define+ENTHIS')
#opts = AnalyzerOption('+define+ENTHAT')
#opts = AnalyzerOption('+incdir+./tests/syntaxonly')
#v = ModuleAnalyzer.parse(filename='./tests/syntaxonly/directive.v',
#                         #LexerClass=PreprocLexer,
#                         #lexerInitOpt={'options':opts}
#                         optstr='+incdir+./tests/syntaxonly'
#                         )
v = VA.parse( sys.argv[1:])
#v.link()
#v.dump()
v.elaborate()
print("----- elabed")
v.dump()
