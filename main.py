from AnalisadorLexico.AnalisadorLexico import AnalisadorLexico
from .complements import key_words

if __name__ == '__main__':
    analisador = AnalisadorLexico('programa_teste.txt',key_words)
    analisador.has_lexical_error()