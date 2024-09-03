from ..complements import *

class AnalisadorLexico:
  def __init__(self,target_file_path:str, key_words):
    self.file_path = target_file_path
    self.number_of_identifiers = 0
    self.identifiers = {}
    self.consts_list = []
    self.key_words = key_words
    self.text_code = ""

  def get_program_code(self):
    with open(self.file_path, 'r') as select_file:
      self.text_code = select_file.read()

  def get_entry(self) -> str:
    first_element = self.text_code[0]
    self.text_code = self.text_code[1:]
    return first_element

  def search_for_key_word(self, word:str):
    begin = 0
    end = len(self.key_words) - 1

    while begin <= end:
      middle = (begin+end)/2
      middle_key = self.key_words[middle]

      if middle_key == word:
        return middle
      elif middle_key < word:
        begin = middle + 1
      else:
        end = middle - 1

    return 'identifier'

  def add_to_consts_list(self, word:str) -> int:
    if word not in self.consts_list:
      self.const_list.append(word)

    return len(self.const_list) - 1

  def get_identifier_number(self, identifier: str) -> int:
    if identifier not in self.identifiers:
      self.identifiers[identifier] = self.number_of_identifiers
      self.number_of_identifiers+=1
    return self.identifiers[identifier]

  def letter_treatment(self):
    word = self.next_entry
    self.next_entry = self.get_entry()

    while self.is_letter(self.next_entry) or self.is_digit(self.next_entry) or self.next_entry == "_":
      word+= self.next_entry
      self.next_entry = self.get_entry()
      self.entry+=1

    token = self.search_for_key_word(word)

    if token == 'identifier':
      self.secundaryToken = self.get_identifier_number(word)

    return token

  def number_treatment(self):
    number = self.next_entry
    self.next_entry = self.get_entry()
    already_have_point = False

    while is_digit(self.next_entry) or self.next_entry == "." :
      if self.next_entry == "." and already_have_point:
        break
      elif self.next_entry == "." and not already_have_point:
        already_have_point = True

      number += self.next_entry
      self.next_entry = self.get_entry()
      self.entry+=1

    self.secundary_token = self.add_to_consts_list(number)
    return 'number'


  def string_treatment(self) :
    word = self.next_entry
    self.next_entry = self.get_entry()

    while self.next_entry != "\"":
      word+= self.next_entry
      if self.next_entry == "\n" or self.next_entry == "\r":
        self.line += 1
        self.entry = 0
      self.next_entry = self.get_entry()
      self.entry+=1

    self.secundaryToken = self.add_to_consts_list(word)
    return 'string'

  def nextToken(self):
    while(is_space(self.next_entry)):
      if self.next_entry == "\r" or self.next_entry == "\n":
        self.line+=1
        self.entry = 0
      self.next_entry = self.get_entry()
      self.entry+=1

    if self.next_char == "":
      self.token = 'eof'

    if is_letter(self.next_entry):
      self.token = self.letter_treatment()

    elif is_digit(self.next_entry):
      self.token = self.number_treatment()

    elif is_string(self.next_entry):
      self.token = self.string_treatment()

    elif (self.next_entry == "+"):
        self.token = 'plus'
        self.next_entry = self.get_entry()
        if self.next_entry == "+":
            self.token = 'plus_plus'
            self.next_entry = self.get_entry()
    elif (self.next_entry == "-"):
        self.token = 'minus'
        self.next_entry = self.get_entry()
        if self.next_entry == "-":
            self.token = 'minus_minus'
            self.next_entry = self.get_entry()
    elif (self.next_entry == "*"):
        self.token = 'times'
        self.next_entry = self.get_entry()
    elif (self.next_entry == "/"):
        self.token = 'divide'
        self.next_entry = self.get_entry()
    elif (self.next_entry == "="):
        self.token = 'equals'
        self.next_entry = self.get_entry()
        if self.next_entry == "=":
            self.token = 'equal_equal'
            self.next_entry = self.get_entry()
    elif (self.next_entry == "<"):
        self.token = 'less_than'
        self.next_entry = self.get_entry()
        if self.next_entry == "=":
            self.token = 'less_or_equal'
            self.next_entry = self.get_entry()
        elif self.next_entry == "<":
            self.token = 'less_less'
            self.next_entry = self.get_entry()
    elif (self.next_entry == ">"):
        self.token = 'greater_than'
        self.next_entry = self.get_entry()
        if self.next_entry == "=":
            self.token = 'greater_or_equal'
            self.next_entry = self.get_entry()
        elif self.next_entry == ">":
            self.token = 'greater_greater'
            self.next_entry = self.get_entry()
    elif (self.next_entry == "!"):
        self.token = 'not'
        self.next_entry = self.get_entry()
        if self.next_entry == "=":
            self.token = 'not_equal'
            self.next_entry = self.get_entry()
    elif (self.next_entry == ":"):
        self.token = 'colon'
        self.next_entry = self.get_entry()
    elif (self.next_entry == ","):
        self.token = 'comma'
        self.next_entry = self.get_entry()
    elif (self.next_entry == ";"):
        self.token = 'semi_colon'
        self.next_entry = self.get_entry()
    elif (self.next_entry == "("):
        self.token = 'left_parenthesis'
        self.next_entry = self.get_entry()
    elif (self.next_entry == ")"):
        self.token = 'right_parenthesis'
        self.next_entry = self.get_entry()
    elif (self.next_entry == "["):
        self.token = 'left_square'
        self.next_entry = self.get_entry()
    elif (self.next_entry == ""):
        self.token = 'right_square'
        self.next_entry = self.get_entry()
    elif (self.next_entry == "{"):
        self.token = 'left_braces'
        self.next_entry = self.get_entry()
    elif (self.next_entry == "}"):
        self.token = 'right_braces'
        self.next_entry = self.get_entry()
    elif (self.next_entry == "|"):
        self.token = 'bit_or'
        self.next_entry = self.get_entry()
        if self.next_entry == "|":
            self.token = 'or'
            self.next_entry = self.get_entry()
    elif (self.next_entry == "&"):
        self.token = 'bit_and'
        self.next_entry = self.get_entry()
        if self.next_entry == "&":
            self.token = 'and'
            self.next_entry = self.get_entry()
    elif (self.next_entry == "."):
        self.token = 'dot'
        self.next_entry = self.get_entry()
    elif (self.next_entry == "^"):
        self.token = 'bit_xor'
        self.next_entry = self.get_entry()

    else:
        self.token = 'unknown'
        self.next_entry = self.get_entry()

    return self.token

  def reset_analysis(self):
    self.lexicalError = False
    self.entry = 0
    self.line = 1
    self.get_program_code()
    self.next_entry = self.get_entry()

  def analyse_token(self,token):
    if token == 'unknown':
      print(f"Error: character {self.entry} in line:{self.line}")
      self.lexicalError = True


  def has_lexical_error(self):
    self.reset_analysis()
    token_aux = self.next_token()

    while token_aux!= 'eof':
      self.analyze_token(token_aux)
      token_aux = self.next_token()

    return self.lexicalError