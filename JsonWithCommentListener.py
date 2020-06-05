# Generated from JsonWithComment.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JsonWithCommentParser import JsonWithCommentParser
else:
    from JsonWithCommentParser import JsonWithCommentParser

# This class defines a complete listener for a parse tree produced by JsonWithCommentParser.
class JsonWithCommentListener(ParseTreeListener):

    # Enter a parse tree produced by JsonWithCommentParser#json.
    def enterJson(self, ctx:JsonWithCommentParser.JsonContext):
        pass

    # Exit a parse tree produced by JsonWithCommentParser#json.
    def exitJson(self, ctx:JsonWithCommentParser.JsonContext):
        pass


    # Enter a parse tree produced by JsonWithCommentParser#AnObject.
    def enterAnObject(self, ctx:JsonWithCommentParser.AnObjectContext):
        pass

    # Exit a parse tree produced by JsonWithCommentParser#AnObject.
    def exitAnObject(self, ctx:JsonWithCommentParser.AnObjectContext):
        pass


    # Enter a parse tree produced by JsonWithCommentParser#EmptyObject.
    def enterEmptyObject(self, ctx:JsonWithCommentParser.EmptyObjectContext):
        pass

    # Exit a parse tree produced by JsonWithCommentParser#EmptyObject.
    def exitEmptyObject(self, ctx:JsonWithCommentParser.EmptyObjectContext):
        pass


    # Enter a parse tree produced by JsonWithCommentParser#ArrayOfValues.
    def enterArrayOfValues(self, ctx:JsonWithCommentParser.ArrayOfValuesContext):
        pass

    # Exit a parse tree produced by JsonWithCommentParser#ArrayOfValues.
    def exitArrayOfValues(self, ctx:JsonWithCommentParser.ArrayOfValuesContext):
        pass


    # Enter a parse tree produced by JsonWithCommentParser#EmptyArray.
    def enterEmptyArray(self, ctx:JsonWithCommentParser.EmptyArrayContext):
        pass

    # Exit a parse tree produced by JsonWithCommentParser#EmptyArray.
    def exitEmptyArray(self, ctx:JsonWithCommentParser.EmptyArrayContext):
        pass


    # Enter a parse tree produced by JsonWithCommentParser#pair.
    def enterPair(self, ctx:JsonWithCommentParser.PairContext):
        pass

    # Exit a parse tree produced by JsonWithCommentParser#pair.
    def exitPair(self, ctx:JsonWithCommentParser.PairContext):
        pass


    # Enter a parse tree produced by JsonWithCommentParser#String.
    def enterString(self, ctx:JsonWithCommentParser.StringContext):
        pass

    # Exit a parse tree produced by JsonWithCommentParser#String.
    def exitString(self, ctx:JsonWithCommentParser.StringContext):
        pass


    # Enter a parse tree produced by JsonWithCommentParser#Atom.
    def enterAtom(self, ctx:JsonWithCommentParser.AtomContext):
        pass

    # Exit a parse tree produced by JsonWithCommentParser#Atom.
    def exitAtom(self, ctx:JsonWithCommentParser.AtomContext):
        pass


    # Enter a parse tree produced by JsonWithCommentParser#ObjectValue.
    def enterObjectValue(self, ctx:JsonWithCommentParser.ObjectValueContext):
        pass

    # Exit a parse tree produced by JsonWithCommentParser#ObjectValue.
    def exitObjectValue(self, ctx:JsonWithCommentParser.ObjectValueContext):
        pass


    # Enter a parse tree produced by JsonWithCommentParser#ArrayValue.
    def enterArrayValue(self, ctx:JsonWithCommentParser.ArrayValueContext):
        pass

    # Exit a parse tree produced by JsonWithCommentParser#ArrayValue.
    def exitArrayValue(self, ctx:JsonWithCommentParser.ArrayValueContext):
        pass


