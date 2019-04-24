

from analyzer.IOAnalyzer import IOAnalyzer
from analyzer.ModuleAnalyzer import ModuleAnalyzer

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

v = ModuleAnalyzer.parse(filename='./tests/syntaxonly/legacyver.v')
v.link()
v.dump()
v.elaborate()
print("----- elabed")
v.dump()
