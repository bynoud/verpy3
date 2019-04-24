

from verpy.analyzer.FunctionAnalyzer import *
a = FunctionAnalyzer()
m = a.unit.newModule("testmod1")
a.analyzeFile("adb400_functions.v",
        m, 'module_or_generate_item_declaration')

