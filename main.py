import sys
from antlr4 import *
from Analisadores.XamaLexicAnalyser import XamaLexicAnalyser
from Analisadores.XamaSyntaticAnalyser import XamaSyntaticAnalyser
from Analisadores.XamaSemanticAnalyser import XamaSemanticAnalyser

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = XamaLexicAnalyser(input_stream)
    stream = CommonTokenStream(lexer)
    parser = XamaSyntaticAnalyser(stream)
    
    tree = parser.program()
   
    listener = XamaSemanticAnalyser()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)