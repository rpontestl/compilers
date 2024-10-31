import sys
from antlr4 import *
from Analisadores.XamaLexicAnalyser import XamaLexicAnalyser
from Analisadores.XamaSyntaticAnalyser import XamaSyntaticAnalyser
from Analisadores.XamaSemanticAnalyser import XamaSemanticAnalyser
from compiler import compile_program
def main(argv):
    program_file = argv[1]
    input_stream = FileStream(program_file)
    lexer = XamaLexicAnalyser(input_stream)
    stream = CommonTokenStream(lexer)
    parser = XamaSyntaticAnalyser(stream)
    
    tree = parser.program()
   
    listener = XamaSemanticAnalyser()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    
    compile_program(program_file,listener.get_assembly_code())
    
if __name__ == '__main__':
    main(sys.argv)