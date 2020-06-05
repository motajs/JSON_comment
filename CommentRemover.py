import sys
from antlr4 import *
from antlr4.InputStream import InputStream

if __name__ is not None and "." in __name__:
    from .JsonWithCommentLexer import JsonWithCommentLexer
    from .JsonWithCommentParser import JsonWithCommentParser
    from .JsonWithCommentListener import JsonWithCommentListener
else:
    from JsonWithCommentLexer import JsonWithCommentLexer
    from JsonWithCommentParser import JsonWithCommentParser
    from JsonWithCommentListener import JsonWithCommentListener

import json
import re

class CommentRemover(JsonWithCommentListener):
    def __init__(self):
        self.content = {}
        self.index = []

    def getContent(self, ctx):
        return self.content[ctx]

    def setContent(self, ctx, value):
        self.content[ctx] = value
    
    def setIndex(self, ctx):
        self.index.append([ctx.start.start,ctx.stop.stop+1])

    def exitAtom(self, ctx):
        self.setContent(ctx, ctx.getText())
        self.setIndex(ctx)

    def exitString(self, ctx):
        self.setContent(ctx, self.strip(ctx.getText()))
        self.setIndex(ctx)

    def exitObjectValue(self, ctx: JsonWithCommentParser.ObjectValueContext):
        self.setContent(ctx, self.getContent(ctx.obj()))

    def exitPair(self, ctx: JsonWithCommentParser.PairContext):
        tag = self.strip(ctx.STRING().getText())
        val = self.getContent(ctx.value())
        x = '%s:%s' % (tag, val)
        self.setContent(ctx, x)

    def exitAnObject(self, ctx: JsonWithCommentParser.AnObjectContext):
        buf = '{' + ','.join([self.getContent(pctx) for pctx in ctx.pair()]) + '}'
        self.setContent(ctx, buf)

    def exitArrayOfValues(self, ctx: JsonWithCommentParser.ArrayOfValuesContext):
        buf = '[' + ','.join([self.getContent(vctx) for vctx in ctx.value()]) + ']'
        self.setContent(ctx, buf)

    def exitArrayValue(self, ctx: JsonWithCommentParser.ArrayValueContext):
        self.setContent(ctx, self.getContent(ctx.array()))

    def exitEmptyArray(self, ctx: JsonWithCommentParser.EmptyArrayContext):
        self.setContent(ctx, "[]")
        self.setIndex(ctx)
    
    def exitEmptyObject(self, ctx:JsonWithCommentParser.EmptyObjectContext):
        self.setContent(ctx, "{}")
        self.setIndex(ctx)

    def exitJson(self, ctx: JsonWithCommentParser.JsonContext):
        self.setContent(ctx, self.getContent(ctx.getChild(0)))

    def strip(self, string: str):
        if string[0] in '\'"`':
            if string[0] == '`':
                string=eval('"""'+string[1:-1].replace('\\"','"').replace('"','\\"')+'"""')
            else:
                string=eval(string)
            string=json.dumps(string)
        return string

# ctx.parser.getTokenStream().tokenSource.inputStream.getText(0,10)

def main(input,output=None):
    if input == None:
        input_stream = InputStream(sys.stdin.read())
    else:
        if ':' in input:
            input_stream = InputStream(input)
        else:
            input_stream = FileStream(input,encoding='utf-8')
        ''' with open(input,encoding='utf-8') as fid:
            sourceStr=fid.read()
            input_stream = InputStream(sourceStr) '''

    lexer = JsonWithCommentLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = JsonWithCommentParser(token_stream)
    tree = parser.json()

    #lisp_tree_str = tree.toStringTree(recog=parser)
    #print(lisp_tree_str)

    # listener
    print('Start Walking...')
    listener = CommentRemover()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    #print(listener.getContent(tree))
    content = json.loads(listener.getContent(tree))
    print(content)

    allTokenIndex = [[token.start,token.stop+1] for token in token_stream.tokens]
    leafIndex = listener.index

    sourceStr=input_stream.strdata
    strdata=sourceStr
    strdatalist=[]
    stop_=0
    for start,stop in leafIndex:
        strdatalist+=[strdata[stop_:start],str([start,stop])]
        stop_=stop
    strdatalist+=[strdata[stop_:]]
    strdata=''.join(strdatalist)
    
    input_stream = InputStream(strdata)
    lexer = JsonWithCommentLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = JsonWithCommentParser(token_stream)
    tree = parser.json()
    listener = CommentRemover()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    #print(listener.getContent(tree))
    index = json.loads(listener.getContent(tree))
    print(index)

    ii_ = 0
    t_=0
    comments_=[]
    for a,b in leafIndex[1:]+[[len(sourceStr),len(sourceStr)]]:
        newComment=[]
        for ii in range(ii_,len(allTokenIndex)):
            s,t = allTokenIndex[ii]
            sourceStr_ = re.sub(r'\s+',' ',sourceStr[t_:s])
            if len(sourceStr_.replace(' ','')) >2 :
                newComment.append(sourceStr_)
            t_=t
            if s >= a :
                ii_=ii+1
                break
        comments_.append('\n'.join(newComment))
    
    comments=json.loads(json.dumps(index))
    def foreachInObj(obj):
        for ii in (obj if type(obj)==dict else range(len(obj))):
            if type(obj[ii]) != list or type(obj[ii][0]) != int :
                foreachInObj(obj[ii])
            else :
                for jj,value in enumerate(leafIndex):
                    if value==obj[ii]:
                        obj[ii]=comments_[jj]
                        break
    foreachInObj(comments)

    if output==None:
        fid=sys.stdout
    else:
        fid =open(output,'w',encoding='utf-8')
    print('content=',file=fid,end='')
    print(content,file=fid)
    print('comments=',file=fid,end='')
    print(comments,file=fid)
    print('index=',file=fid,end='')
    print(index,file=fid)
    print('allTokenIndex=',file=fid,end='')
    print(allTokenIndex,file=fid)
    print('leafIndex=',file=fid,end='')
    print(leafIndex,file=fid)
    if output!=None:
        fid.close()
    return (content,comments,index,allTokenIndex,leafIndex)

if __name__ == '__main__':

    sys.argv=['','t.js','_a.js']
    
    if len(sys.argv) > 1:
        input = sys.argv[1]
        if len(sys.argv) > 2:
            output = sys.argv[2]
        else:
            output = None
    else:
        input = None
        output = None

    main(input,output)

'''
True=true;
False=false;

console.log(JSON.stringify(comments,null,4))
'''