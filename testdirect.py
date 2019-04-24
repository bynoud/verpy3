

from analyzer.IOAnalyzer import IOAnalyzer
from analyzer.ModuleAnalyzer import ModuleAnalyzer
from analyzer.PreprocLexer import PreprocLexer
from analyzer.AnalyzerOption import AnalyzerOption

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

#opts = AnalyzerOption('+define+ENTHIS')
#opts = AnalyzerOption('+define+ENTHAT')
#opts = AnalyzerOption('+incdir+./tests/syntaxonly')
#v = ModuleAnalyzer.parse(filename='./tests/syntaxonly/directive.v',
#                         #LexerClass=PreprocLexer,
#                         #lexerInitOpt={'options':opts}
#                         optstr='+incdir+./tests/syntaxonly'
#                         )
v = ModuleAnalyzer.parse( ('./tests/syntaxonly/directive.v',
                           './tests/syntaxonly/legacyver.v',
                           '+incdir+./tests/syntaxonly')
                         )
#v.link()
#v.dump()
v.elaborate()
print("----- elabed")
v.dump()
