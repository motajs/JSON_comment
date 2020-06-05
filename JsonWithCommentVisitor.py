# Generated from JsonWithComment.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JsonWithCommentParser import JsonWithCommentParser
else:
    from JsonWithCommentParser import JsonWithCommentParser

# This class defines a complete generic visitor for a parse tree produced by JsonWithCommentParser.

class JsonWithCommentVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JsonWithCommentParser#json.
    def visitJson(self, ctx:JsonWithCommentParser.JsonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonWithCommentParser#AnObject.
    def visitAnObject(self, ctx:JsonWithCommentParser.AnObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonWithCommentParser#EmptyObject.
    def visitEmptyObject(self, ctx:JsonWithCommentParser.EmptyObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonWithCommentParser#ArrayOfValues.
    def visitArrayOfValues(self, ctx:JsonWithCommentParser.ArrayOfValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonWithCommentParser#EmptyArray.
    def visitEmptyArray(self, ctx:JsonWithCommentParser.EmptyArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonWithCommentParser#pair.
    def visitPair(self, ctx:JsonWithCommentParser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonWithCommentParser#String.
    def visitString(self, ctx:JsonWithCommentParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonWithCommentParser#Atom.
    def visitAtom(self, ctx:JsonWithCommentParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonWithCommentParser#ObjectValue.
    def visitObjectValue(self, ctx:JsonWithCommentParser.ObjectValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JsonWithCommentParser#ArrayValue.
    def visitArrayValue(self, ctx:JsonWithCommentParser.ArrayValueContext):
        return self.visitChildren(ctx)



del JsonWithCommentParser