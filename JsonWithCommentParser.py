# Generated from JsonWithComment.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("B\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\5\2")
        buf.write("\17\n\2\3\3\3\3\3\3\3\3\7\3\25\n\3\f\3\16\3\30\13\3\3")
        buf.write("\3\5\3\33\n\3\3\3\3\3\3\3\3\3\5\3!\n\3\3\4\3\4\3\4\3\4")
        buf.write("\7\4\'\n\4\f\4\16\4*\13\4\3\4\5\4-\n\4\3\4\3\4\3\4\3\4")
        buf.write("\5\4\63\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\5\6@\n\6\3\6\2\2\7\2\4\6\b\n\2\2\2I\2\16\3\2\2\2\4")
        buf.write(" \3\2\2\2\6\62\3\2\2\2\b\64\3\2\2\2\n?\3\2\2\2\f\17\5")
        buf.write("\4\3\2\r\17\5\6\4\2\16\f\3\2\2\2\16\r\3\2\2\2\17\3\3\2")
        buf.write("\2\2\20\21\7\n\2\2\21\26\5\b\5\2\22\23\7\3\2\2\23\25\5")
        buf.write("\b\5\2\24\22\3\2\2\2\25\30\3\2\2\2\26\24\3\2\2\2\26\27")
        buf.write("\3\2\2\2\27\32\3\2\2\2\30\26\3\2\2\2\31\33\7\3\2\2\32")
        buf.write("\31\3\2\2\2\32\33\3\2\2\2\33\34\3\2\2\2\34\35\7\4\2\2")
        buf.write("\35!\3\2\2\2\36\37\7\n\2\2\37!\7\4\2\2 \20\3\2\2\2 \36")
        buf.write("\3\2\2\2!\5\3\2\2\2\"#\7\13\2\2#(\5\n\6\2$%\7\3\2\2%\'")
        buf.write("\5\n\6\2&$\3\2\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2),\3")
        buf.write("\2\2\2*(\3\2\2\2+-\7\3\2\2,+\3\2\2\2,-\3\2\2\2-.\3\2\2")
        buf.write("\2./\7\5\2\2/\63\3\2\2\2\60\61\7\13\2\2\61\63\7\5\2\2")
        buf.write("\62\"\3\2\2\2\62\60\3\2\2\2\63\7\3\2\2\2\64\65\7\f\2\2")
        buf.write("\65\66\7\6\2\2\66\67\5\n\6\2\67\t\3\2\2\28@\7\f\2\29@")
        buf.write("\7\r\2\2:@\5\4\3\2;@\5\6\4\2<@\7\7\2\2=@\7\b\2\2>@\7\t")
        buf.write("\2\2?8\3\2\2\2?9\3\2\2\2?:\3\2\2\2?;\3\2\2\2?<\3\2\2\2")
        buf.write("?=\3\2\2\2?>\3\2\2\2@\13\3\2\2\2\n\16\26\32 (,\62?")
        return buf.getvalue()


class JsonWithCommentParser ( Parser ):

    grammarFileName = "JsonWithComment.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'}'", "']'", "':'", "'true'", 
                     "'false'", "'null'", "'{'", "'['" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "LCURLY", "LBRACK", "STRING", "NUMBER", "WhiteSpace", 
                      "Newline", "BlockComment", "CLineComment", "PyLineComment" ]

    RULE_json = 0
    RULE_obj = 1
    RULE_array = 2
    RULE_pair = 3
    RULE_value = 4

    ruleNames =  [ "json", "obj", "array", "pair", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    LCURLY=8
    LBRACK=9
    STRING=10
    NUMBER=11
    WhiteSpace=12
    Newline=13
    BlockComment=14
    CLineComment=15
    PyLineComment=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class JsonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def obj(self):
            return self.getTypedRuleContext(JsonWithCommentParser.ObjContext,0)


        def array(self):
            return self.getTypedRuleContext(JsonWithCommentParser.ArrayContext,0)


        def getRuleIndex(self):
            return JsonWithCommentParser.RULE_json

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson" ):
                listener.enterJson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson" ):
                listener.exitJson(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJson" ):
                return visitor.visitJson(self)
            else:
                return visitor.visitChildren(self)




    def json(self):

        localctx = JsonWithCommentParser.JsonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_json)
        try:
            self.state = 12
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JsonWithCommentParser.LCURLY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.obj()
                pass
            elif token in [JsonWithCommentParser.LBRACK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ObjContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JsonWithCommentParser.RULE_obj

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AnObjectContext(ObjContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JsonWithCommentParser.ObjContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JsonWithCommentParser.PairContext)
            else:
                return self.getTypedRuleContext(JsonWithCommentParser.PairContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnObject" ):
                listener.enterAnObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnObject" ):
                listener.exitAnObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnObject" ):
                return visitor.visitAnObject(self)
            else:
                return visitor.visitChildren(self)


    class EmptyObjectContext(ObjContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JsonWithCommentParser.ObjContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyObject" ):
                listener.enterEmptyObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyObject" ):
                listener.exitEmptyObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyObject" ):
                return visitor.visitEmptyObject(self)
            else:
                return visitor.visitChildren(self)



    def obj(self):

        localctx = JsonWithCommentParser.ObjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_obj)
        self._la = 0 # Token type
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = JsonWithCommentParser.AnObjectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.match(JsonWithCommentParser.LCURLY)
                self.state = 15
                self.pair()
                self.state = 20
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 16
                        self.match(JsonWithCommentParser.T__0)
                        self.state = 17
                        self.pair() 
                    self.state = 22
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JsonWithCommentParser.T__0:
                    self.state = 23
                    self.match(JsonWithCommentParser.T__0)


                self.state = 26
                self.match(JsonWithCommentParser.T__1)
                pass

            elif la_ == 2:
                localctx = JsonWithCommentParser.EmptyObjectContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.match(JsonWithCommentParser.LCURLY)
                self.state = 29
                self.match(JsonWithCommentParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JsonWithCommentParser.RULE_array

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArrayOfValuesContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JsonWithCommentParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JsonWithCommentParser.ValueContext)
            else:
                return self.getTypedRuleContext(JsonWithCommentParser.ValueContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayOfValues" ):
                listener.enterArrayOfValues(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayOfValues" ):
                listener.exitArrayOfValues(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayOfValues" ):
                return visitor.visitArrayOfValues(self)
            else:
                return visitor.visitChildren(self)


    class EmptyArrayContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JsonWithCommentParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyArray" ):
                listener.enterEmptyArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyArray" ):
                listener.exitEmptyArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyArray" ):
                return visitor.visitEmptyArray(self)
            else:
                return visitor.visitChildren(self)



    def array(self):

        localctx = JsonWithCommentParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = JsonWithCommentParser.ArrayOfValuesContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.match(JsonWithCommentParser.LBRACK)
                self.state = 33
                self.value()
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 34
                        self.match(JsonWithCommentParser.T__0)
                        self.state = 35
                        self.value() 
                    self.state = 40
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JsonWithCommentParser.T__0:
                    self.state = 41
                    self.match(JsonWithCommentParser.T__0)


                self.state = 44
                self.match(JsonWithCommentParser.T__2)
                pass

            elif la_ == 2:
                localctx = JsonWithCommentParser.EmptyArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.match(JsonWithCommentParser.LBRACK)
                self.state = 47
                self.match(JsonWithCommentParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(JsonWithCommentParser.STRING, 0)

        def value(self):
            return self.getTypedRuleContext(JsonWithCommentParser.ValueContext,0)


        def getRuleIndex(self):
            return JsonWithCommentParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair" ):
                return visitor.visitPair(self)
            else:
                return visitor.visitChildren(self)




    def pair(self):

        localctx = JsonWithCommentParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(JsonWithCommentParser.STRING)
            self.state = 51
            self.match(JsonWithCommentParser.T__3)
            self.state = 52
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JsonWithCommentParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArrayValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JsonWithCommentParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def array(self):
            return self.getTypedRuleContext(JsonWithCommentParser.ArrayContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayValue" ):
                listener.enterArrayValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayValue" ):
                listener.exitArrayValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayValue" ):
                return visitor.visitArrayValue(self)
            else:
                return visitor.visitChildren(self)


    class ObjectValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JsonWithCommentParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def obj(self):
            return self.getTypedRuleContext(JsonWithCommentParser.ObjContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectValue" ):
                listener.enterObjectValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectValue" ):
                listener.exitObjectValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectValue" ):
                return visitor.visitObjectValue(self)
            else:
                return visitor.visitChildren(self)


    class AtomContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JsonWithCommentParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(JsonWithCommentParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JsonWithCommentParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(JsonWithCommentParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = JsonWithCommentParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JsonWithCommentParser.STRING]:
                localctx = JsonWithCommentParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(JsonWithCommentParser.STRING)
                pass
            elif token in [JsonWithCommentParser.NUMBER]:
                localctx = JsonWithCommentParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(JsonWithCommentParser.NUMBER)
                pass
            elif token in [JsonWithCommentParser.LCURLY]:
                localctx = JsonWithCommentParser.ObjectValueContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.obj()
                pass
            elif token in [JsonWithCommentParser.LBRACK]:
                localctx = JsonWithCommentParser.ArrayValueContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.array()
                pass
            elif token in [JsonWithCommentParser.T__4]:
                localctx = JsonWithCommentParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 58
                self.match(JsonWithCommentParser.T__4)
                pass
            elif token in [JsonWithCommentParser.T__5]:
                localctx = JsonWithCommentParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 59
                self.match(JsonWithCommentParser.T__5)
                pass
            elif token in [JsonWithCommentParser.T__6]:
                localctx = JsonWithCommentParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 60
                self.match(JsonWithCommentParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





