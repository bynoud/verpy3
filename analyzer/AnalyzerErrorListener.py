


import sys
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException

class AnalyzerErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        #print("line %s:%s [%s] : %s" % (line, column, offendingSymbol, msg), file=sys.stderr)
        #t = e.offendingToken
        #print(" ::", t.text)
        # the RecognitionException is catched by DefaultErrorStrategy
        # I need to stop parsing when syntax error happend
        tok = e.offendingToken
        istr = tok.getTokenSource().inputStream
        #try: src = istr.fileName
        #except: 
        src = istr.name
        #print("D: %s :" % istr.data)
        raise ParseCancellationException("Syntax error in '%s' line %s:%s, near '%s'" % (
            src, line, column, tok.text))

