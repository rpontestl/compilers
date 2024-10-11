from antlr4 import *
from collections import defaultdict

if "." in __name__:
    from .xamaParser import xamaParser
else:
    from xamaParser import xamaParser

# Classe para gerenciar escopos
class SymbolTable:
    def __init__(self):
        self.scopes = [{}]  # Começamos com o escopo global

    def enter_scope(self):
        self.scopes.append({})  # Adiciona um novo escopo

    def exit_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()  # Remove o escopo atual

    def add_symbol(self, name, type_):
        # Adiciona o símbolo no escopo atual (último na pilha)
        if name in self.scopes[-1]:
            return False  # Retorna False se já existe no escopo atual
        self.scopes[-1][name] = type_
        return True

    def lookup(self, name):
        # Procura pelo símbolo do escopo mais interno até o mais externo
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None  # Retorna None se o símbolo não for encontrado
    
    def check_type(self, type1, type2):
        # Regras de compatibilidade de tipos
        if type1 == type2:
            return True
        if type1 == 'integer' and type2 == 'float' or type1 == 'float' and type2 == 'integer':
            return True
        # Adicione mais regras conforme necessário
        return False

symbol_table = SymbolTable()

# Listener personalizado para análise de escopo e tipo
class xamaListener(ParseTreeListener):
    def enterVar_decl(self, ctx:xamaParser.Var_declContext):
        type_ = ctx.type_().getText()  # Obtém o tipo da variável
        ids = ctx.id_list().getText().split(',')  # Lista de IDs
        for id_ in ids:
            if not symbol_table.add_symbol(id_, type_):
                print(f"Erro: Variável '{id_}' já declarada no escopo atual")
            else:
                print(f"Declaração de variável: {id_} do tipo {type_}")

    def enterConst_decl(self, ctx:xamaParser.Const_declContext):
        type_ = ctx.type_().getText()  # Obtém o tipo da constante
        id_ = ctx.ID().getText()  # Nome da constante
        if not symbol_table.add_symbol(id_, type_):
            print(f"Erro: Constante '{id_}' já declarada no escopo atual")
        else:
            print(f"Declaração de constante: {id_} do tipo {type_}")

    def enterFunc_decl(self, ctx:xamaParser.Func_declContext):
        id_ = ctx.ID().getText()  # Nome da função
        return_type = ctx.type_().getText()  # Tipo de retorno da função
        param_list = ctx.param_list().getText()  # Parâmetros da função
        if not symbol_table.add_symbol(id_, f"function({param_list}): {return_type}"):
            print(f"Erro: Função '{id_}' já declarada no escopo atual")
        else:
            print(f"Declaração de função: {id_} retornando {return_type} com parâmetros {param_list}")
        symbol_table.enter_scope()  # Entra em um novo escopo para os parâmetros da função

    def exitFunc_decl(self, ctx:xamaParser.Func_declContext):
        symbol_table.exit_scope()  # Sai do escopo da função

    def enterPrint_stmt(self, ctx:xamaParser.Print_stmtContext):
        print("Comando de impressão")

    def enterLv(self, ctx:xamaParser.LvContext):
        id_ = ctx.ID().getText()
        if not symbol_table.lookup(id_):
            print(f"Erro: Variável ou função '{id_}' não declarada")
        else:
            print(f"Uso de '{id_}'")

del xamaParser
