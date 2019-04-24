


from ..VerpyError import *

def entryName(ctx):
    n = type(ctx).__name__
    # context class name must always end with 'Context'
    if len(n) < 8: raise ParserContextError("'%s' not a valid Context name" % n)
    return (n[0].lower() + n[1:-7])

def tokens(ctx):
    return ctx.parser.getTokenStream()


def removeChild(ctx, child):
    ctx.children.remove(child)

def addNextSib(ctx, sib):
    parent = ctx.parentCtx
    cind = parent.children.index(ctx)
    insertChild(parent, cind+1, sib)
    return sib

def addPrevSib(ctx, sib):
    parent = ctx.parentCtx
    cind = parent.children.index(ctx)
    insertChild(parent, cind, sib)
    return sib

def insertChild(ctx, ind, child):
    child.parentCtx = ctx
    ctx.children.insert(ind, child)

def startIndex(ctx):
    return ctx.start.tokenIndex

def stopIndex(ctx):
    stop = ctx.stop.tokenIndex
    htoks = tokens(ctx).getHiddenTokensToRight(stop)
    if htoks is not None:
        stop = htoks[-1].tokenIndex
    return stop

# include hidden tokens text
def fullText(ctx):
    print("XX fulltext [%d:%d]" % (ctx.start.tokenIndex, ctx.stop.tokenIndex))
    return tokens(ctx).getText([startIndex(ctx), stopIndex(ctx)])

def tokenReplace(ctx, tokreps, types=None):
    toks = tokens(ctx)
    start = startIndex(ctx)
    stop = stopIndex(ctx)
    #print("tokrep [%d-%d]: %s <- %s (%s)" % (
    #    ctx.startIndex, ctx.stopIndex, ctx.fullText, tokreps, types))
    #for i in toks.tokens[start : stop+1]:
    #    print("  to [%s] = '%s' %s" % (i, i.text, i.type))

    #for t in ctx.tokens.getTokens(ctx.startIndex,
    #        ctx.stopIndex, types):
    #                                           bug:stop is not +1 in lib
    for t in toks.getTokens(start, stop+1, types):
        #print( "   %s %s" % (t.text, t.type))
        if t.text in tokreps: t.text = str(tokreps[t.text])


#!!!!! doing recreate parser & token stream
# is it expensive??
def duplicateCtx(ctx, prefix='', postfix=''):
    return parseString(
        prefix + fullText(ctx) + postfix,
        entryName(ctx), type(ctx.parser))

#import parser
#from parser import *
from ..parser.VerexLexer import VerexLexer
from ..parser.VerexParser import VerexParser
from antlr4 import CommonTokenStream,FileStream,InputStream

def createInputStream(filename='', fromstr='', srcName=''):
    if filename:
        istr = FileStream(filename)
        if not srcName:
            import os
            srcName = ("<file: %s>" % os.path.basename(filename))
    elif fromstr:
        istr = InputStream(fromstr)
        if not srcName:
            srcName = "<input_str>"
    else:
        raise Exception("Either filename of fromstr must be specified")   
    istr.name = srcName
    return istr

def parseString(s, entry, srcName='',
                ParserClass=VerexParser,
                LexerClass=VerexLexer):
    istr = createInputStream(fromstr=s, srcName=srcName)
    parser = ParserClass(
        CommonTokenStream(
            LexerClass(istr)
        ))
    parser.buildParseTrees = True
    return getattr(parser, entry)()

def parseFile(filename, entry=VerexParser.vfile,
              ParserClass=VerexParser,
              LexerClass=VerexLexer):
    istr = createInputStream(filename=filename)
    parser = ParserClass(
        CommonTokenStream(
            LexerClass(istr)
        ))
    parser.buildParseTrees = True
    return getattr(parser, entry)()

