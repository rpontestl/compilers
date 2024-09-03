import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from complements import *

class AnalisadorLexico:
    def __init__(self,target_file_path:str, key_words):
        if self.verify_extension(target_file_path):
            self.file_path = target_file_path
            self.number_of_identifiers = 0
            self.text_code = ""
            self.secundary_token = 0
            self.identifiers = {}
            self.consts_list = []
            self.tokens_list = []
            self.key_words = key_words
        else:
            raise ValueError(f"Invalid file extension for file: {target_file_path}")

    def verify_extension(self,program_name):
        if program_name.split(".")[1] == 'x':
            return True
        else:
            return False

    def get_program_code(self):
        with open(self.file_path, 'r') as select_file:
            self.text_code = select_file.read()

    def get_entry(self) -> str:
        first_element = ""
        if self.text_code:
            first_element = self.text_code[0]
            self.text_code = self.text_code[1:]
        
        return first_element

    def search_for_key_word(self, word:str):
        try:
            token = self.key_words[word]
            return token
        except:
            return IDENTIFIER
            

    def add_to_consts_list(self, word:str) -> int:
        if word not in self.consts_list:
            self.consts_list.append(word)
        return len(self.consts_list) - 1

    def get_identifier_number(self, identifier: str) -> int:
        if identifier not in self.identifiers:
            self.identifiers[identifier] = self.number_of_identifiers
            self.number_of_identifiers+=1
        return self.identifiers[identifier]

    def letter_treatment(self):
        word = self.next_entry
        self.next_entry = self.get_entry()

        while is_letter(self.next_entry) or is_digit(self.next_entry) or self.next_entry == "_":
            word+= self.next_entry
            self.next_entry = self.get_entry()
            self.entry_position+=1

        token = self.search_for_key_word(word)

        if token == IDENTIFIER:
            self.secundary_token = self.get_identifier_number(word)

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
            self.entry_position+=1

        self.secundary_token = self.add_to_consts_list(number)
        
        if already_have_point: 
            return FLOAT
        else:
            return INTEGER


    def string_treatment(self) :
        word = self.next_entry
        self.next_entry = self.get_entry()

        while self.next_entry != "\"":
            word+= self.next_entry
            if self.next_entry == "\n" or self.next_entry == "\r":
                self.line += 1
                self.entry_position = 0
            self.next_entry = self.get_entry()
            self.entry_position+=1

        self.secundary_token = self.add_to_consts_list(word)
        return STRING

    def next_token(self):
        self.secundary_token = 0
        
        while(is_space(self.next_entry)):
            if self.next_entry == "\r" or self.next_entry == "\n":
                self.line+=1
                self.entry_position = 0
            self.next_entry = self.get_entry()
            self.entry_position+=1

        if self.next_entry == "":
            self.token = EOF

        elif is_letter(self.next_entry):
            self.token = self.letter_treatment()

        elif is_digit(self.next_entry):
            self.token = self.number_treatment()

        elif is_string(self.next_entry):
            self.token = self.string_treatment()

        elif (self.next_entry == '+'):
            self.token = PLUS
            self.next_entry = self.get_entry()
            if self.next_entry == "+":
                self.token = PLUS_PLUS
                self.next_entry = self.get_entry()
                
        elif (self.next_entry == "-"):
            self.token = MINUS
            self.next_entry = self.get_entry()
            if self.next_entry == "-":
                self.token = MINUS_MINUS
                self.next_entry = self.get_entry()
                
        elif (self.next_entry == "*"):
            self.token = TIMES
            self.next_entry = self.get_entry()
            
        elif (self.next_entry == "/"):
            self.token = DIVIDE
            self.next_entry = self.get_entry()
            
        elif (self.next_entry == "="):
            self.token = EQUALS
            self.next_entry = self.get_entry()
            if self.next_entry == "=":
                self.token = EQUAL_EQUAL
                self.next_entry = self.get_entry()
                
        elif (self.next_entry == "<"):
            self.token = LESS_THAN
            self.next_entry = self.get_entry()
            if self.next_entry == "=":
                self.token = LESS_OR_EQUAL
                self.next_entry = self.get_entry()
            elif self.next_entry == "<":
                self.token = LESS_LESS
                self.next_entry = self.get_entry()
                
        elif (self.next_entry == ">"):
            self.token = GREATER_THAN
            self.next_entry = self.get_entry()
            if self.next_entry == "=":
                self.token = GREATER_OR_EQUAL
                self.next_entry = self.get_entry()
            elif self.next_entry == ">":
                self.token = GREATER_GREATER
                self.next_entry = self.get_entry()
                
        elif (self.next_entry == "!"):
            self.token = NOT
            self.next_entry = self.get_entry()
            if self.next_entry == "=":
                self.token = NOT_EQUAL
                self.next_entry = self.get_entry()
                
        elif (self.next_entry == ":"):
            self.token = COLON
            self.next_entry = self.get_entry()
        
        elif (self.next_entry == ","):
            self.token = COMMA
            self.next_entry = self.get_entry()
        
        elif (self.next_entry == ";"):
            self.token = SEMI_COLON
            self.next_entry = self.get_entry()
        
        elif (self.next_entry == "("):
            self.token = LEFT_PARENTHESIS
            self.next_entry = self.get_entry()
        
        elif (self.next_entry == ")"):
            self.token = RIGHT_PARENTHESIS
            self.next_entry = self.get_entry()
        
        elif (self.next_entry == "["):
            self.token = LEFT_SQUARE
            self.next_entry = self.get_entry()
        
        elif (self.next_entry == "]"):
            self.token = RIGHT_SQUARE
            self.next_entry = self.get_entry()
        
        elif (self.next_entry == "{"):
            self.token = LEFT_BRACES
            self.next_entry = self.get_entry()
        
        elif (self.next_entry == "}"):
            self.token = RIGHT_BRACES
            self.next_entry = self.get_entry()
        
        elif (self.next_entry == "|"):
            self.token = BIT_OR
            self.next_entry = self.get_entry()
            if self.next_entry == "|":
                self.token = OR
                self.next_entry = self.get_entry()
        
        elif (self.next_entry == "&"):
            self.token = BIT_AND
            self.next_entry = self.get_entry()
            if self.next_entry == "&":
                self.token = AND
                self.next_entry = self.get_entry()
        
        elif (self.next_entry == "."):
            self.token = DOT
            self.next_entry = self.get_entry()
        
        elif (self.next_entry == "^"):
            self.token = BIT_XOR
            self.next_entry = self.get_entry()

        else:
            self.token = UNKNOWN
            self.next_entry = self.get_entry()

        return self.token

    def reset_analysis(self):
        self.lexicalError = False
        self.entry_position = 0
        self.line = 1
        self.get_program_code()
        self.next_entry = self.get_entry()

    def analyze_token(self,token):
        if token == UNKNOWN:
            print(f"Error: character {self.entry_position} in line:{self.line}")
            self.lexicalError = True


    def has_lexical_error(self):
        self.reset_analysis()
        token_aux = self.next_token()

        while token_aux!= EOF:
            self.analyze_token(token_aux)
            self.tokens_list.append([token_aux,self.secundary_token])
            token_aux = self.next_token()

        print(self.tokens_list)
        return self.lexicalError