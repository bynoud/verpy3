#
# from __future__ import print_function, absolute_import
# import ast, re
# from .VerilogObject import *
# from ..VerpyError import *
# from ..parser import VerexParser as VP
#
# def verNumber(fromstr):
#     t = re.sub("_", "", fromstr)
#     if ctx.Decimal_number:
#         return int(re.sub(r"^[0-9]*'[sS]?[dD]", "", t))
#     elif ctx.Octal_number:
#         return int(re.sub(r"^[0-9]*'[sS]?[oO]", "", t), 8)
#     elif ctx.Binary_number:
#         return int(re.sub(r"^[0-9]*'[sS]?[bB]", "", t), 2)
#     elif ctx.Hex_number:
#         return int(re.sub(r"^[0-9]*'[sS]?[hH]", "", t), 16)
#     elif ctx.Real_number:
#         return float(t)
#     else:
#         return 0
#
# def analyzeExpr(ctx: VP.ExpressionContext):
#     if ctx.binary_operator:
#         self.op = self.binOp(ctx.binary_operator().getText(),
#                 ctx.op1.text, ctx.op2.text)
#     elif ctx.expression:
#         self.op = self.condOp(ctx.op1.text,
#                 ctx.expression(), ctx.op2.text)
#     else:
#         self.op = self.term(ctx.op1)
#
# class Primary(object):
#     def __init__(self, VP.TermContext ctx=None):
#         self.vctx = ctx
#         self.op = None
#         if ctx: self.analyze(ctx)
#
#     def analyze(self, ctx):
#         if ctx.number:
#             self.op = ast.Num(verNumber(ctx.number().getText()))
#
# class Expression(object):
#     def __init__(self, VP.ExpressionContext ctx, parent=None):
#         assert ctx or parent
#         self.parent = parent
#         self.op = None
#         self.analyze(ctx)
#
#     def analyze(self, VP.ExpressionContext ctx):
#         if ctx.binary_operator:
#             self.op = self.binOp(ctx.binary_operator().getText(),
#                     ctx.op1.text, ctx.op2.text)
#         elif ctx.expression:
#             self.op = self.condOp(ctx.op1.text,
#                     ctx.expression(), ctx.op2.text)
#         else:
#             self.op = self.term(ctx.op1)
#
#     def term(self, VP.TermContext ctx):
#         aa
#
