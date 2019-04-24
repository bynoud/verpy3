


from antlr4 import *
from ..parser import VerexParser, VerexLexer


fromstr = "a+b * c-1 / (a+4) ? c+2**a : d ? 3&a+3 : d^2"

istr = InputStream(fromstr)
lexer = VerexLexer(istr)
tokens = CommonTokenStream(lexer)
parser = VerexParser(tokens)
parser.buildParseTrees = True

