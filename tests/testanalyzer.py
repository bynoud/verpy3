


import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

from verpy.analyzer.IOAnalyzer import IOAnalyzer
from verpy.analyzer.ModuleAnalyzer import ModuleAnalyzer

#v = ModuleAnalyzer.parse('./syntaxonly/legacyver.v')
v = ModuleAnalyzer.parse('./rdma_top.v')
v.link()
v.dump()
v.elaborate()
print("----- elabed")
v.dump()
