

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

from verpy3.analyzer.FunctionAnalyzer import FunctionAnalyzer

# opts = AnalyzerOption('+define+ENTHIS')
# opts = AnalyzerOption('+define+ENTHAT')
# opts = AnalyzerOption('+incdir+./tests/syntaxonly')
# v = ModuleAnalyzer.parse(filename='./tests/syntaxonly/directive.v',
#                         #LexerClass=PreprocLexer,
#                         #lexerInitOpt={'options':opts}
#                         optstr='+incdir+./tests/syntaxonly'
#                         )
# v = ModuleAnalyzer.parse( ( './syntaxonly/legacyver.v',
v = FunctionAnalyzer.parse(("./syntaxonly/legacyver.v", "./syntaxonly/namediff.v", "+incdir+./syntaxonly -y ./syntaxonly"))

v.link()
# v.dump()
v.elaborate()
print("----- elabed")
v.dump()
