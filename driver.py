import sys
from antlr4 import *
from AnalisadorSintatico.XamaLexer import xamaLexer
from AnalisadorSintatico.xamaParser import xamaParser
from AnalisadorSintatico.xamaListener import xamaListener

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = xamaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = xamaParser(stream)
    
    tree = parser.program()
    #print(tree.toStringTree(recog=parser))
    
    listener = xamaListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)