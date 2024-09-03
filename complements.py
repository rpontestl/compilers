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
    if character == "\"": return True
    else: return False

key_words = [
    'and',
    'array',
    'boolean',
    'break',
    'char',
    'character',
    'colon',
    'comma',
    'continue',
    'divide',
    'do',
    'dot',
    'equal_equal',
    'equals',
    'eof',
    'else',
    'false',
    'function',
    'greater_greater',
    'greater_or_equal',
    'greater_than',
    'if',
    'left_braces',
    'left_parenthesis',
    'left_square',
    'less_less',
    'less_or_equal',
    'less_than',
    'minus',
    'minus_minus',
    'not',
    'not_equal',
    'number',
    'of',
    'or',
    'plus',
    'plus_plus',
    'right_braces',
    'right_parenthesis',
    'right_square',
    'semi_colon',
    'string',
    'struct',
    'true',
    'type',
    'while'
]
