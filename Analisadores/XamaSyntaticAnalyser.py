from antlr4 import *
import sys
from typing import TextIO

def serializedATN():
    return [
        4,1,58,377,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,5,1,57,8,1,10,1,12,1,60,9,1,1,2,1,2,1,2,1,2,3,2,66,8,2,1,3,1,3,
        1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,
        1,6,1,6,5,6,88,8,6,10,6,12,6,91,9,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,114,
        8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,5,9,135,8,9,10,9,12,9,138,9,9,1,10,1,10,1,10,1,10,
        1,10,1,11,1,11,1,11,3,11,148,8,11,1,11,1,11,1,11,1,11,5,11,154,8,
        11,10,11,12,11,157,9,11,1,12,1,12,1,12,1,12,1,12,5,12,164,8,12,10,
        12,12,12,167,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,212,8,13,1,14,1,14,1,
        14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,
        15,229,8,15,10,15,12,15,232,9,15,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,5,16,246,8,16,10,16,12,16,249,9,16,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,5,17,272,8,17,10,17,12,17,
        275,9,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,286,8,
        18,10,18,12,18,289,9,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,5,19,300,8,19,10,19,12,19,303,9,19,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,5,20,314,8,20,10,20,12,20,317,9,20,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,3,21,348,8,21,1,22,1,22,1,22,1,22,1,22,1,22,5,22,356,8,22,10,
        22,12,22,359,9,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,
        23,1,23,5,23,372,8,23,10,23,12,23,375,9,23,1,23,0,13,2,12,18,22,
        24,30,32,34,36,38,40,44,46,24,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,0,1,2,0,5,9,52,52,406,0,48,1,0,
        0,0,2,51,1,0,0,0,4,65,1,0,0,0,6,67,1,0,0,0,8,72,1,0,0,0,10,79,1,
        0,0,0,12,81,1,0,0,0,14,113,1,0,0,0,16,115,1,0,0,0,18,124,1,0,0,0,
        20,139,1,0,0,0,22,147,1,0,0,0,24,158,1,0,0,0,26,211,1,0,0,0,28,213,
        1,0,0,0,30,219,1,0,0,0,32,233,1,0,0,0,34,250,1,0,0,0,36,276,1,0,
        0,0,38,290,1,0,0,0,40,304,1,0,0,0,42,347,1,0,0,0,44,349,1,0,0,0,
        46,360,1,0,0,0,48,49,3,2,1,0,49,50,5,0,0,1,50,1,1,0,0,0,51,52,6,
        1,-1,0,52,53,3,4,2,0,53,58,1,0,0,0,54,55,10,2,0,0,55,57,3,4,2,0,
        56,54,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,3,1,0,
        0,0,60,58,1,0,0,0,61,66,3,6,3,0,62,66,3,8,4,0,63,66,3,14,7,0,64,
        66,3,16,8,0,65,61,1,0,0,0,65,62,1,0,0,0,65,63,1,0,0,0,65,64,1,0,
        0,0,66,5,1,0,0,0,67,68,5,1,0,0,68,69,3,10,5,0,69,70,3,12,6,0,70,
        71,5,2,0,0,71,7,1,0,0,0,72,73,5,3,0,0,73,74,3,10,5,0,74,75,5,52,
        0,0,75,76,5,4,0,0,76,77,3,30,15,0,77,78,5,2,0,0,78,9,1,0,0,0,79,
        80,7,0,0,0,80,11,1,0,0,0,81,82,6,6,-1,0,82,83,5,52,0,0,83,89,1,0,
        0,0,84,85,10,2,0,0,85,86,5,10,0,0,86,88,5,52,0,0,87,84,1,0,0,0,88,
        91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,13,1,0,0,0,91,89,1,0,0,
        0,92,93,5,11,0,0,93,94,5,52,0,0,94,95,5,4,0,0,95,96,5,12,0,0,96,
        97,5,13,0,0,97,98,5,57,0,0,98,99,5,14,0,0,99,100,5,15,0,0,100,114,
        3,10,5,0,101,102,5,11,0,0,102,103,5,52,0,0,103,104,5,4,0,0,104,105,
        5,16,0,0,105,106,5,17,0,0,106,107,3,8,4,0,107,108,5,18,0,0,108,114,
        1,0,0,0,109,110,5,11,0,0,110,111,5,52,0,0,111,112,5,4,0,0,112,114,
        3,10,5,0,113,92,1,0,0,0,113,101,1,0,0,0,113,109,1,0,0,0,114,15,1,
        0,0,0,115,116,5,19,0,0,116,117,5,52,0,0,117,118,5,20,0,0,118,119,
        3,18,9,0,119,120,5,21,0,0,120,121,5,22,0,0,121,122,3,10,5,0,122,
        123,3,20,10,0,123,17,1,0,0,0,124,125,6,9,-1,0,125,126,5,52,0,0,126,
        127,5,22,0,0,127,128,3,10,5,0,128,136,1,0,0,0,129,130,10,2,0,0,130,
        131,5,10,0,0,131,132,5,52,0,0,132,133,5,22,0,0,133,135,3,10,5,0,
        134,129,1,0,0,0,135,138,1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,
        137,19,1,0,0,0,138,136,1,0,0,0,139,140,5,17,0,0,140,141,3,22,11,
        0,141,142,3,24,12,0,142,143,5,18,0,0,143,21,1,0,0,0,144,145,6,11,
        -1,0,145,148,3,6,3,0,146,148,3,8,4,0,147,144,1,0,0,0,147,146,1,0,
        0,0,148,155,1,0,0,0,149,150,10,4,0,0,150,154,3,6,3,0,151,152,10,
        3,0,0,152,154,3,8,4,0,153,149,1,0,0,0,153,151,1,0,0,0,154,157,1,
        0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,23,1,0,0,0,157,155,1,0,
        0,0,158,159,6,12,-1,0,159,160,3,26,13,0,160,165,1,0,0,0,161,162,
        10,2,0,0,162,164,3,26,13,0,163,161,1,0,0,0,164,167,1,0,0,0,165,163,
        1,0,0,0,165,166,1,0,0,0,166,25,1,0,0,0,167,165,1,0,0,0,168,169,5,
        23,0,0,169,170,5,20,0,0,170,171,3,30,15,0,171,172,5,21,0,0,172,173,
        3,26,13,0,173,212,1,0,0,0,174,175,5,23,0,0,175,176,5,20,0,0,176,
        177,3,30,15,0,177,178,5,21,0,0,178,179,3,26,13,0,179,180,5,24,0,
        0,180,181,3,26,13,0,181,212,1,0,0,0,182,183,5,25,0,0,183,184,5,20,
        0,0,184,185,3,30,15,0,185,186,5,21,0,0,186,187,3,26,13,0,187,212,
        1,0,0,0,188,189,5,26,0,0,189,190,3,26,13,0,190,191,5,25,0,0,191,
        192,5,20,0,0,192,193,3,30,15,0,193,194,5,21,0,0,194,195,5,2,0,0,
        195,212,1,0,0,0,196,212,3,20,10,0,197,198,3,46,23,0,198,199,5,4,
        0,0,199,200,3,30,15,0,200,201,5,2,0,0,201,212,1,0,0,0,202,203,5,
        27,0,0,203,212,5,2,0,0,204,205,5,28,0,0,205,212,5,2,0,0,206,207,
        5,29,0,0,207,208,3,30,15,0,208,209,5,2,0,0,209,212,1,0,0,0,210,212,
        3,28,14,0,211,168,1,0,0,0,211,174,1,0,0,0,211,182,1,0,0,0,211,188,
        1,0,0,0,211,196,1,0,0,0,211,197,1,0,0,0,211,202,1,0,0,0,211,204,
        1,0,0,0,211,206,1,0,0,0,211,210,1,0,0,0,212,27,1,0,0,0,213,214,5,
        30,0,0,214,215,5,20,0,0,215,216,3,44,22,0,216,217,5,21,0,0,217,218,
        5,2,0,0,218,29,1,0,0,0,219,220,6,15,-1,0,220,221,3,32,16,0,221,230,
        1,0,0,0,222,223,10,3,0,0,223,224,5,31,0,0,224,229,3,32,16,0,225,
        226,10,2,0,0,226,227,5,32,0,0,227,229,3,32,16,0,228,222,1,0,0,0,
        228,225,1,0,0,0,229,232,1,0,0,0,230,228,1,0,0,0,230,231,1,0,0,0,
        231,31,1,0,0,0,232,230,1,0,0,0,233,234,6,16,-1,0,234,235,3,34,17,
        0,235,247,1,0,0,0,236,237,10,4,0,0,237,238,5,33,0,0,238,246,3,34,
        17,0,239,240,10,3,0,0,240,241,5,34,0,0,241,246,3,34,17,0,242,243,
        10,2,0,0,243,244,5,35,0,0,244,246,3,34,17,0,245,236,1,0,0,0,245,
        239,1,0,0,0,245,242,1,0,0,0,246,249,1,0,0,0,247,245,1,0,0,0,247,
        248,1,0,0,0,248,33,1,0,0,0,249,247,1,0,0,0,250,251,6,17,-1,0,251,
        252,3,36,18,0,252,273,1,0,0,0,253,254,10,7,0,0,254,255,5,36,0,0,
        255,272,3,36,18,0,256,257,10,6,0,0,257,258,5,37,0,0,258,272,3,36,
        18,0,259,260,10,5,0,0,260,261,5,38,0,0,261,272,3,36,18,0,262,263,
        10,4,0,0,263,264,5,39,0,0,264,272,3,36,18,0,265,266,10,3,0,0,266,
        267,5,40,0,0,267,272,3,36,18,0,268,269,10,2,0,0,269,270,5,41,0,0,
        270,272,3,36,18,0,271,253,1,0,0,0,271,256,1,0,0,0,271,259,1,0,0,
        0,271,262,1,0,0,0,271,265,1,0,0,0,271,268,1,0,0,0,272,275,1,0,0,
        0,273,271,1,0,0,0,273,274,1,0,0,0,274,35,1,0,0,0,275,273,1,0,0,0,
        276,277,6,18,-1,0,277,278,3,38,19,0,278,287,1,0,0,0,279,280,10,3,
        0,0,280,281,5,42,0,0,281,286,3,38,19,0,282,283,10,2,0,0,283,284,
        5,43,0,0,284,286,3,38,19,0,285,279,1,0,0,0,285,282,1,0,0,0,286,289,
        1,0,0,0,287,285,1,0,0,0,287,288,1,0,0,0,288,37,1,0,0,0,289,287,1,
        0,0,0,290,291,6,19,-1,0,291,292,3,40,20,0,292,301,1,0,0,0,293,294,
        10,3,0,0,294,295,5,44,0,0,295,300,3,40,20,0,296,297,10,2,0,0,297,
        298,5,45,0,0,298,300,3,40,20,0,299,293,1,0,0,0,299,296,1,0,0,0,300,
        303,1,0,0,0,301,299,1,0,0,0,301,302,1,0,0,0,302,39,1,0,0,0,303,301,
        1,0,0,0,304,305,6,20,-1,0,305,306,3,42,21,0,306,315,1,0,0,0,307,
        308,10,3,0,0,308,309,5,46,0,0,309,314,3,42,21,0,310,311,10,2,0,0,
        311,312,5,47,0,0,312,314,3,42,21,0,313,307,1,0,0,0,313,310,1,0,0,
        0,314,317,1,0,0,0,315,313,1,0,0,0,315,316,1,0,0,0,316,41,1,0,0,0,
        317,315,1,0,0,0,318,348,3,46,23,0,319,320,5,48,0,0,320,348,3,46,
        23,0,321,322,5,49,0,0,322,348,3,46,23,0,323,324,3,46,23,0,324,325,
        5,48,0,0,325,348,1,0,0,0,326,327,3,46,23,0,327,328,5,49,0,0,328,
        348,1,0,0,0,329,330,5,20,0,0,330,331,3,30,15,0,331,332,5,21,0,0,
        332,348,1,0,0,0,333,334,5,52,0,0,334,335,5,20,0,0,335,336,3,44,22,
        0,336,337,5,21,0,0,337,348,1,0,0,0,338,339,5,45,0,0,339,348,3,42,
        21,0,340,341,5,50,0,0,341,348,3,42,21,0,342,348,5,53,0,0,343,348,
        5,54,0,0,344,348,5,55,0,0,345,348,5,56,0,0,346,348,5,57,0,0,347,
        318,1,0,0,0,347,319,1,0,0,0,347,321,1,0,0,0,347,323,1,0,0,0,347,
        326,1,0,0,0,347,329,1,0,0,0,347,333,1,0,0,0,347,338,1,0,0,0,347,
        340,1,0,0,0,347,342,1,0,0,0,347,343,1,0,0,0,347,344,1,0,0,0,347,
        345,1,0,0,0,347,346,1,0,0,0,348,43,1,0,0,0,349,350,6,22,-1,0,350,
        351,3,30,15,0,351,357,1,0,0,0,352,353,10,2,0,0,353,354,5,10,0,0,
        354,356,3,30,15,0,355,352,1,0,0,0,356,359,1,0,0,0,357,355,1,0,0,
        0,357,358,1,0,0,0,358,45,1,0,0,0,359,357,1,0,0,0,360,361,6,23,-1,
        0,361,362,5,52,0,0,362,373,1,0,0,0,363,364,10,3,0,0,364,365,5,51,
        0,0,365,372,5,52,0,0,366,367,10,2,0,0,367,368,5,13,0,0,368,369,3,
        30,15,0,369,370,5,14,0,0,370,372,1,0,0,0,371,363,1,0,0,0,371,366,
        1,0,0,0,372,375,1,0,0,0,373,371,1,0,0,0,373,374,1,0,0,0,374,47,1,
        0,0,0,375,373,1,0,0,0,26,58,65,89,113,136,147,153,155,165,211,228,
        230,245,247,271,273,285,287,299,301,313,315,347,357,371,373
    ]

class XamaSyntaticAnalyser ( Parser ):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'tmp'", "';'", "'cte'", "'='", "'integer'", 
                     "'char'", "'boolean'", "'string'", "'float'", "','", 
                     "'type'", "'array'", "'['", "']'", "'of'", "'struct'", 
                     "'{'", "'}'", "'function'", "'('", "')'", "':'", "'if'", 
                     "'else'", "'while'", "'do'", "'break'", "'continue'", 
                     "'return'", "'print'", "'&&'", "'||'", "'&'", "'|'", 
                     "'^'", "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", 
                     "'>>'", "'<<'", "'+'", "'-'", "'*'", "'/'", "'++'", 
                     "'--'", "'!'", "'.'", "<INVALID>", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "TRUE", "FALSE", "CHR", "STR", "NUM", "WS" ]

    RULE_program = 0
    RULE_decl_list = 1
    RULE_decl = 2
    RULE_var_decl = 3
    RULE_const_decl = 4
    RULE_type = 5
    RULE_id_list = 6
    RULE_type_decl = 7
    RULE_func_decl = 8
    RULE_param_list = 9
    RULE_block = 10
    RULE_var_const_list = 11
    RULE_stmt_list = 12
    RULE_stmt = 13
    RULE_print_stmt = 14
    RULE_expr = 15
    RULE_cond = 16
    RULE_bitwise = 17
    RULE_relational = 18
    RULE_shift = 19
    RULE_add_sub = 20
    RULE_mul_div = 21
    RULE_expr_list = 22
    RULE_lv = 23

    ruleNames =  [ "program", "decl_list", "decl", "var_decl", "const_decl", 
                   "type", "id_list", "type_decl", "func_decl", "param_list", 
                   "block", "var_const_list", "stmt_list", "stmt", "print_stmt", 
                   "expr", "cond", "bitwise", "relational", "shift", "add_sub", 
                   "mul_div", "expr_list", "lv" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    ID=52
    TRUE=53
    FALSE=54
    CHR=55
    STR=56
    NUM=57
    WS=58

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_list(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Decl_listContext,0)


        def EOF(self):
            return self.getToken(XamaSyntaticAnalyser.EOF, 0)

        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = XamaSyntaticAnalyser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.decl_list(0)
            self.state = 49
            self.match(XamaSyntaticAnalyser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.DeclContext,0)


        def decl_list(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Decl_listContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_decl_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_list" ):
                listener.enterDecl_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_list" ):
                listener.exitDecl_list(self)



    def decl_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = XamaSyntaticAnalyser.Decl_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_decl_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.decl()
            self._ctx.stop = self._input.LT(-1)
            self.state = 58
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = XamaSyntaticAnalyser.Decl_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_decl_list)
                    self.state = 54
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 55
                    self.decl() 
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Const_declContext,0)


        def type_decl(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Type_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Func_declContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)




    def decl(self):

        localctx = XamaSyntaticAnalyser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.var_decl()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.const_decl()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.type_decl()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 64
                self.func_decl()
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


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.TypeContext,0)


        def id_list(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Id_listContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)




    def var_decl(self):

        localctx = XamaSyntaticAnalyser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(XamaSyntaticAnalyser.T__0)
            self.state = 68
            self.type_()
            self.state = 69
            self.id_list(0)
            self.state = 70
            self.match(XamaSyntaticAnalyser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.TypeContext,0)


        def ID(self):
            return self.getToken(XamaSyntaticAnalyser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.ExprContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_const_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConst_decl" ):
                listener.enterConst_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConst_decl" ):
                listener.exitConst_decl(self)




    def const_decl(self):

        localctx = XamaSyntaticAnalyser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(XamaSyntaticAnalyser.T__2)
            self.state = 73
            self.type_()
            self.state = 74
            self.match(XamaSyntaticAnalyser.ID)
            self.state = 75
            self.match(XamaSyntaticAnalyser.T__3)
            self.state = 76
            self.expr(0)
            self.state = 77
            self.match(XamaSyntaticAnalyser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(XamaSyntaticAnalyser.ID, 0)

        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = XamaSyntaticAnalyser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627371488) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(XamaSyntaticAnalyser.ID, 0)

        def id_list(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Id_listContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_id_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_list" ):
                listener.enterId_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_list" ):
                listener.exitId_list(self)



    def id_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = XamaSyntaticAnalyser.Id_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_id_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(XamaSyntaticAnalyser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = XamaSyntaticAnalyser.Id_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_id_list)
                    self.state = 84
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 85
                    self.match(XamaSyntaticAnalyser.T__9)
                    self.state = 86
                    self.match(XamaSyntaticAnalyser.ID) 
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Type_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(XamaSyntaticAnalyser.ID, 0)

        def NUM(self):
            return self.getToken(XamaSyntaticAnalyser.NUM, 0)

        def type_(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.TypeContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Const_declContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_type_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_decl" ):
                listener.enterType_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_decl" ):
                listener.exitType_decl(self)




    def type_decl(self):

        localctx = XamaSyntaticAnalyser.Type_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type_decl)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(XamaSyntaticAnalyser.T__10)
                self.state = 93
                self.match(XamaSyntaticAnalyser.ID)
                self.state = 94
                self.match(XamaSyntaticAnalyser.T__3)
                self.state = 95
                self.match(XamaSyntaticAnalyser.T__11)
                self.state = 96
                self.match(XamaSyntaticAnalyser.T__12)
                self.state = 97
                self.match(XamaSyntaticAnalyser.NUM)
                self.state = 98
                self.match(XamaSyntaticAnalyser.T__13)
                self.state = 99
                self.match(XamaSyntaticAnalyser.T__14)
                self.state = 100
                self.type_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.match(XamaSyntaticAnalyser.T__10)
                self.state = 102
                self.match(XamaSyntaticAnalyser.ID)
                self.state = 103
                self.match(XamaSyntaticAnalyser.T__3)
                self.state = 104
                self.match(XamaSyntaticAnalyser.T__15)
                self.state = 105
                self.match(XamaSyntaticAnalyser.T__16)
                self.state = 106
                self.const_decl()
                self.state = 107
                self.match(XamaSyntaticAnalyser.T__17)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.match(XamaSyntaticAnalyser.T__10)
                self.state = 110
                self.match(XamaSyntaticAnalyser.ID)
                self.state = 111
                self.match(XamaSyntaticAnalyser.T__3)
                self.state = 112
                self.type_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(XamaSyntaticAnalyser.ID, 0)

        def param_list(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Param_listContext,0)


        def type_(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.TypeContext,0)


        def block(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.BlockContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_func_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_decl" ):
                listener.enterFunc_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_decl" ):
                listener.exitFunc_decl(self)




    def func_decl(self):

        localctx = XamaSyntaticAnalyser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(XamaSyntaticAnalyser.T__18)
            self.state = 116
            self.match(XamaSyntaticAnalyser.ID)
            self.state = 117
            self.match(XamaSyntaticAnalyser.T__19)
            self.state = 118
            self.param_list(0)
            self.state = 119
            self.match(XamaSyntaticAnalyser.T__20)
            self.state = 120
            self.match(XamaSyntaticAnalyser.T__21)
            self.state = 121
            self.type_()
            self.state = 122
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(XamaSyntaticAnalyser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.TypeContext,0)


        def param_list(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Param_listContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_param_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_list" ):
                listener.enterParam_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_list" ):
                listener.exitParam_list(self)



    def param_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = XamaSyntaticAnalyser.Param_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_param_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(XamaSyntaticAnalyser.ID)
            self.state = 126
            self.match(XamaSyntaticAnalyser.T__21)
            self.state = 127
            self.type_()
            self._ctx.stop = self._input.LT(-1)
            self.state = 136
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = XamaSyntaticAnalyser.Param_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_param_list)
                    self.state = 129
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 130
                    self.match(XamaSyntaticAnalyser.T__9)
                    self.state = 131
                    self.match(XamaSyntaticAnalyser.ID)
                    self.state = 132
                    self.match(XamaSyntaticAnalyser.T__21)
                    self.state = 133
                    self.type_() 
                self.state = 138
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_const_list(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Var_const_listContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Stmt_listContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = XamaSyntaticAnalyser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(XamaSyntaticAnalyser.T__16)
            self.state = 140
            self.var_const_list(0)
            self.state = 141
            self.stmt_list(0)
            self.state = 142
            self.match(XamaSyntaticAnalyser.T__17)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_const_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Const_declContext,0)


        def var_const_list(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Var_const_listContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_var_const_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_const_list" ):
                listener.enterVar_const_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_const_list" ):
                listener.exitVar_const_list(self)



    def var_const_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = XamaSyntaticAnalyser.Var_const_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_var_const_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 145
                self.var_decl()
                pass
            elif token in [3]:
                self.state = 146
                self.const_decl()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 155
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 153
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = XamaSyntaticAnalyser.Var_const_listContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_var_const_list)
                        self.state = 149
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 150
                        self.var_decl()
                        pass

                    elif la_ == 2:
                        localctx = XamaSyntaticAnalyser.Var_const_listContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_var_const_list)
                        self.state = 151
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 152
                        self.const_decl()
                        pass

             
                self.state = 157
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.StmtContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Stmt_listContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_stmt_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_list" ):
                listener.enterStmt_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_list" ):
                listener.exitStmt_list(self)



    def stmt_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = XamaSyntaticAnalyser.Stmt_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_stmt_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.stmt()
            self._ctx.stop = self._input.LT(-1)
            self.state = 165
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = XamaSyntaticAnalyser.Stmt_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_stmt_list)
                    self.state = 161
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 162
                    self.stmt() 
                self.state = 167
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.ExprContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XamaSyntaticAnalyser.StmtContext)
            else:
                return self.getTypedRuleContext(XamaSyntaticAnalyser.StmtContext,i)


        def block(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.BlockContext,0)


        def lv(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.LvContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Print_stmtContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = XamaSyntaticAnalyser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stmt)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(XamaSyntaticAnalyser.T__22)
                self.state = 169
                self.match(XamaSyntaticAnalyser.T__19)
                self.state = 170
                self.expr(0)
                self.state = 171
                self.match(XamaSyntaticAnalyser.T__20)
                self.state = 172
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.match(XamaSyntaticAnalyser.T__22)
                self.state = 175
                self.match(XamaSyntaticAnalyser.T__19)
                self.state = 176
                self.expr(0)
                self.state = 177
                self.match(XamaSyntaticAnalyser.T__20)
                self.state = 178
                self.stmt()
                self.state = 179
                self.match(XamaSyntaticAnalyser.T__23)
                self.state = 180
                self.stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.match(XamaSyntaticAnalyser.T__24)
                self.state = 183
                self.match(XamaSyntaticAnalyser.T__19)
                self.state = 184
                self.expr(0)
                self.state = 185
                self.match(XamaSyntaticAnalyser.T__20)
                self.state = 186
                self.stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 188
                self.match(XamaSyntaticAnalyser.T__25)
                self.state = 189
                self.stmt()
                self.state = 190
                self.match(XamaSyntaticAnalyser.T__24)
                self.state = 191
                self.match(XamaSyntaticAnalyser.T__19)
                self.state = 192
                self.expr(0)
                self.state = 193
                self.match(XamaSyntaticAnalyser.T__20)
                self.state = 194
                self.match(XamaSyntaticAnalyser.T__1)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 196
                self.block()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 197
                self.lv(0)
                self.state = 198
                self.match(XamaSyntaticAnalyser.T__3)
                self.state = 199
                self.expr(0)
                self.state = 200
                self.match(XamaSyntaticAnalyser.T__1)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 202
                self.match(XamaSyntaticAnalyser.T__26)
                self.state = 203
                self.match(XamaSyntaticAnalyser.T__1)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 204
                self.match(XamaSyntaticAnalyser.T__27)
                self.state = 205
                self.match(XamaSyntaticAnalyser.T__1)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 206
                self.match(XamaSyntaticAnalyser.T__28)
                self.state = 207
                self.expr(0)
                self.state = 208
                self.match(XamaSyntaticAnalyser.T__1)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 210
                self.print_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_list(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Expr_listContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_print_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stmt" ):
                listener.enterPrint_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stmt" ):
                listener.exitPrint_stmt(self)




    def print_stmt(self):

        localctx = XamaSyntaticAnalyser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_print_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(XamaSyntaticAnalyser.T__29)
            self.state = 214
            self.match(XamaSyntaticAnalyser.T__19)
            self.state = 215
            self.expr_list(0)
            self.state = 216
            self.match(XamaSyntaticAnalyser.T__20)
            self.state = 217
            self.match(XamaSyntaticAnalyser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cond(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.CondContext,0)


        def expr(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.ExprContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = XamaSyntaticAnalyser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.cond(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 230
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 228
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = XamaSyntaticAnalyser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 222
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 223
                        self.match(XamaSyntaticAnalyser.T__30)
                        self.state = 224
                        self.cond(0)
                        pass

                    elif la_ == 2:
                        localctx = XamaSyntaticAnalyser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 225
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 226
                        self.match(XamaSyntaticAnalyser.T__31)
                        self.state = 227
                        self.cond(0)
                        pass

             
                self.state = 232
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bitwise(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.BitwiseContext,0)


        def cond(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.CondContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)



    def cond(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = XamaSyntaticAnalyser.CondContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_cond, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.bitwise(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 245
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = XamaSyntaticAnalyser.CondContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_cond)
                        self.state = 236
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 237
                        self.match(XamaSyntaticAnalyser.T__32)
                        self.state = 238
                        self.bitwise(0)
                        pass

                    elif la_ == 2:
                        localctx = XamaSyntaticAnalyser.CondContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_cond)
                        self.state = 239
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 240
                        self.match(XamaSyntaticAnalyser.T__33)
                        self.state = 241
                        self.bitwise(0)
                        pass

                    elif la_ == 3:
                        localctx = XamaSyntaticAnalyser.CondContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_cond)
                        self.state = 242
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 243
                        self.match(XamaSyntaticAnalyser.T__34)
                        self.state = 244
                        self.bitwise(0)
                        pass

             
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BitwiseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.RelationalContext,0)


        def bitwise(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.BitwiseContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_bitwise

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitwise" ):
                listener.enterBitwise(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitwise" ):
                listener.exitBitwise(self)



    def bitwise(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = XamaSyntaticAnalyser.BitwiseContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_bitwise, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.relational(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 271
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = XamaSyntaticAnalyser.BitwiseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwise)
                        self.state = 253
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 254
                        self.match(XamaSyntaticAnalyser.T__35)
                        self.state = 255
                        self.relational(0)
                        pass

                    elif la_ == 2:
                        localctx = XamaSyntaticAnalyser.BitwiseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwise)
                        self.state = 256
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 257
                        self.match(XamaSyntaticAnalyser.T__36)
                        self.state = 258
                        self.relational(0)
                        pass

                    elif la_ == 3:
                        localctx = XamaSyntaticAnalyser.BitwiseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwise)
                        self.state = 259
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 260
                        self.match(XamaSyntaticAnalyser.T__37)
                        self.state = 261
                        self.relational(0)
                        pass

                    elif la_ == 4:
                        localctx = XamaSyntaticAnalyser.BitwiseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwise)
                        self.state = 262
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 263
                        self.match(XamaSyntaticAnalyser.T__38)
                        self.state = 264
                        self.relational(0)
                        pass

                    elif la_ == 5:
                        localctx = XamaSyntaticAnalyser.BitwiseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwise)
                        self.state = 265
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 266
                        self.match(XamaSyntaticAnalyser.T__39)
                        self.state = 267
                        self.relational(0)
                        pass

                    elif la_ == 6:
                        localctx = XamaSyntaticAnalyser.BitwiseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwise)
                        self.state = 268
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 269
                        self.match(XamaSyntaticAnalyser.T__40)
                        self.state = 270
                        self.relational(0)
                        pass

             
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shift(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.ShiftContext,0)


        def relational(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.RelationalContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_relational

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational" ):
                listener.enterRelational(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational" ):
                listener.exitRelational(self)



    def relational(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = XamaSyntaticAnalyser.RelationalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_relational, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.shift(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 287
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 285
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = XamaSyntaticAnalyser.RelationalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relational)
                        self.state = 279
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 280
                        self.match(XamaSyntaticAnalyser.T__41)
                        self.state = 281
                        self.shift(0)
                        pass

                    elif la_ == 2:
                        localctx = XamaSyntaticAnalyser.RelationalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relational)
                        self.state = 282
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 283
                        self.match(XamaSyntaticAnalyser.T__42)
                        self.state = 284
                        self.shift(0)
                        pass

             
                self.state = 289
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ShiftContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_sub(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Add_subContext,0)


        def shift(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.ShiftContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_shift

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShift" ):
                listener.enterShift(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShift" ):
                listener.exitShift(self)



    def shift(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = XamaSyntaticAnalyser.ShiftContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_shift, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.add_sub(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 301
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 299
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = XamaSyntaticAnalyser.ShiftContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_shift)
                        self.state = 293
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 294
                        self.match(XamaSyntaticAnalyser.T__43)
                        self.state = 295
                        self.add_sub(0)
                        pass

                    elif la_ == 2:
                        localctx = XamaSyntaticAnalyser.ShiftContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_shift)
                        self.state = 296
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 297
                        self.match(XamaSyntaticAnalyser.T__44)
                        self.state = 298
                        self.add_sub(0)
                        pass

             
                self.state = 303
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Add_subContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_div(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Mul_divContext,0)


        def add_sub(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Add_subContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_add_sub

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_sub" ):
                listener.enterAdd_sub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_sub" ):
                listener.exitAdd_sub(self)



    def add_sub(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = XamaSyntaticAnalyser.Add_subContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_add_sub, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.mul_div()
            self._ctx.stop = self._input.LT(-1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 313
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = XamaSyntaticAnalyser.Add_subContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_add_sub)
                        self.state = 307
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 308
                        self.match(XamaSyntaticAnalyser.T__45)
                        self.state = 309
                        self.mul_div()
                        pass

                    elif la_ == 2:
                        localctx = XamaSyntaticAnalyser.Add_subContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_add_sub)
                        self.state = 310
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 311
                        self.match(XamaSyntaticAnalyser.T__46)
                        self.state = 312
                        self.mul_div()
                        pass

             
                self.state = 317
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Mul_divContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lv(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.LvContext,0)


        def expr(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.ExprContext,0)


        def ID(self):
            return self.getToken(XamaSyntaticAnalyser.ID, 0)

        def expr_list(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Expr_listContext,0)


        def mul_div(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Mul_divContext,0)


        def TRUE(self):
            return self.getToken(XamaSyntaticAnalyser.TRUE, 0)

        def FALSE(self):
            return self.getToken(XamaSyntaticAnalyser.FALSE, 0)

        def CHR(self):
            return self.getToken(XamaSyntaticAnalyser.CHR, 0)

        def STR(self):
            return self.getToken(XamaSyntaticAnalyser.STR, 0)

        def NUM(self):
            return self.getToken(XamaSyntaticAnalyser.NUM, 0)

        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_mul_div

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul_div" ):
                listener.enterMul_div(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul_div" ):
                listener.exitMul_div(self)




    def mul_div(self):

        localctx = XamaSyntaticAnalyser.Mul_divContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_mul_div)
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.lv(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.match(XamaSyntaticAnalyser.T__47)
                self.state = 320
                self.lv(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 321
                self.match(XamaSyntaticAnalyser.T__48)
                self.state = 322
                self.lv(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 323
                self.lv(0)
                self.state = 324
                self.match(XamaSyntaticAnalyser.T__47)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 326
                self.lv(0)
                self.state = 327
                self.match(XamaSyntaticAnalyser.T__48)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 329
                self.match(XamaSyntaticAnalyser.T__19)
                self.state = 330
                self.expr(0)
                self.state = 331
                self.match(XamaSyntaticAnalyser.T__20)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 333
                self.match(XamaSyntaticAnalyser.ID)
                self.state = 334
                self.match(XamaSyntaticAnalyser.T__19)
                self.state = 335
                self.expr_list(0)
                self.state = 336
                self.match(XamaSyntaticAnalyser.T__20)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 338
                self.match(XamaSyntaticAnalyser.T__44)
                self.state = 339
                self.mul_div()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 340
                self.match(XamaSyntaticAnalyser.T__49)
                self.state = 341
                self.mul_div()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 342
                self.match(XamaSyntaticAnalyser.TRUE)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 343
                self.match(XamaSyntaticAnalyser.FALSE)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 344
                self.match(XamaSyntaticAnalyser.CHR)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 345
                self.match(XamaSyntaticAnalyser.STR)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 346
                self.match(XamaSyntaticAnalyser.NUM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.ExprContext,0)


        def expr_list(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.Expr_listContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_expr_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_list" ):
                listener.enterExpr_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_list" ):
                listener.exitExpr_list(self)



    def expr_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = XamaSyntaticAnalyser.Expr_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 357
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = XamaSyntaticAnalyser.Expr_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_list)
                    self.state = 352
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 353
                    self.match(XamaSyntaticAnalyser.T__9)
                    self.state = 354
                    self.expr(0) 
                self.state = 359
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LvContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(XamaSyntaticAnalyser.ID, 0)

        def lv(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.LvContext,0)


        def expr(self):
            return self.getTypedRuleContext(XamaSyntaticAnalyser.ExprContext,0)


        def getRuleIndex(self):
            return XamaSyntaticAnalyser.RULE_lv

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLv" ):
                listener.enterLv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLv" ):
                listener.exitLv(self)



    def lv(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = XamaSyntaticAnalyser.LvContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_lv, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(XamaSyntaticAnalyser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 373
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 371
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = XamaSyntaticAnalyser.LvContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lv)
                        self.state = 363
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 364
                        self.match(XamaSyntaticAnalyser.T__50)
                        self.state = 365
                        self.match(XamaSyntaticAnalyser.ID)
                        pass

                    elif la_ == 2:
                        localctx = XamaSyntaticAnalyser.LvContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lv)
                        self.state = 366
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 367
                        self.match(XamaSyntaticAnalyser.T__12)
                        self.state = 368
                        self.expr(0)
                        self.state = 369
                        self.match(XamaSyntaticAnalyser.T__13)
                        pass

             
                self.state = 375
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.decl_list_sempred
        self._predicates[6] = self.id_list_sempred
        self._predicates[9] = self.param_list_sempred
        self._predicates[11] = self.var_const_list_sempred
        self._predicates[12] = self.stmt_list_sempred
        self._predicates[15] = self.expr_sempred
        self._predicates[16] = self.cond_sempred
        self._predicates[17] = self.bitwise_sempred
        self._predicates[18] = self.relational_sempred
        self._predicates[19] = self.shift_sempred
        self._predicates[20] = self.add_sub_sempred
        self._predicates[22] = self.expr_list_sempred
        self._predicates[23] = self.lv_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def decl_list_sempred(self, localctx:Decl_listContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def id_list_sempred(self, localctx:Id_listContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def param_list_sempred(self, localctx:Param_listContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def var_const_list_sempred(self, localctx:Var_const_listContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

    def stmt_list_sempred(self, localctx:Stmt_listContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def cond_sempred(self, localctx:CondContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         

    def bitwise_sempred(self, localctx:BitwiseContext, predIndex:int):
            if predIndex == 11:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 2)
         

    def relational_sempred(self, localctx:RelationalContext, predIndex:int):
            if predIndex == 17:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 2)
         

    def shift_sempred(self, localctx:ShiftContext, predIndex:int):
            if predIndex == 19:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 2)
         

    def add_sub_sempred(self, localctx:Add_subContext, predIndex:int):
            if predIndex == 21:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 2)
         

    def expr_list_sempred(self, localctx:Expr_listContext, predIndex:int):
            if predIndex == 23:
                return self.precpred(self._ctx, 2)
         

    def lv_sempred(self, localctx:LvContext, predIndex:int):
            if predIndex == 24:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 2)
         




