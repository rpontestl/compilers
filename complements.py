#token_types <---manter enumerado
AND = 0
ARRAY = 1
BIT_AND = 2
BIT_OR = 3
BIT_XOR = 4
BOOLEAN = 5
BREAK = 6
CHAR = 7
CHARACTER = 8
COLON = 9
COMMA = 10
CONSTANT = 11
CONTINUE = 12
DIVIDE = 13
DO = 14
DOT = 15
ELSE = 16
EOF = 17
EQUALS = 18
EQUAL_EQUAL = 19
FALSE = 20
FLOAT = 21
FUNCTION = 22
GREATER_GREATER = 23
GREATER_OR_EQUAL = 24
GREATER_THAN = 25
IDENTIFIER = 26
IF = 27
INTEGER = 28
LEFT_BRACES = 29
LEFT_PARENTHESIS = 30
LEFT_SQUARE = 31
LESS_LESS = 32
LESS_OR_EQUAL = 33
LESS_THAN = 34
MINUS = 35
MINUS_MINUS = 36
NOT = 37
NOT_EQUAL = 38
OF = 39
OR = 40
PLUS = 41
PLUS_PLUS = 42
RETURN = 43
RIGHT_BRACES = 44
RIGHT_PARENTHESIS = 45
RIGHT_SQUARE = 46
SEMI_COLON = 47
STRING = 48
STRUCT = 49
TEMPORARY = 50
TIMES = 51
TRUE = 52
TYPE = 53
UNKNOWN = 54
WHILE = 55
#end of tokens type <--- manter enumerado

key_words = {
  'and': AND,
  'array': ARRAY,
  'boolean': BOOLEAN,
  'break': BREAK,
  'char': CHAR,
  'character': CHARACTER,
  'colon': COLON,
  'comma': COMMA,
  'continue': CONTINUE,
  'cte': CONSTANT,
  'divide': DIVIDE,
  'do': DO,
  'dot': DOT,
  'eof': EOF,
  'else': ELSE,
  'false': FALSE,
  'float': FLOAT,
  'function': FUNCTION,
  'if': IF,
  'int': INTEGER,
  'not': NOT,
  'of': OF,
  'or': OR,
  'return':RETURN,
  'string': STRING,
  'struct': STRUCT,
  'tmp': TEMPORARY,
  'true': TRUE,
  'type': TYPE,
  'while': WHILE
}

def is_space(character):
  if character in [" ","\f","\v","\t","\n","\r"]:
    return True
  else:
    return False

def is_letter(character):
  ascii_value = ord(character)
  if (ascii_value >= ord('A') and ascii_value <= ord('Z')) or (ascii_value >= ord('a') and ascii_value <= ord('z')):
    return True
  else:
    return False

def is_digit(character):
  if character in "0123456789":
    return True
  else:
    return False

def is_string(character):
    if character == '"': return True
    else: return False



