# Generated from xama.g4 by ANTLR 4.13.2
from antlr4 import *
from collections import defaultdict

if "." in __name__:
    from .xamaParser import xamaParser
else:
    from xamaParser import xamaParser

class SymbolTable:
    def __init__(self):
        self.symbols = defaultdict(dict)
        self.current_scope = None

    def enter_scope(self, name):
        self.current_scope = name

    def exit_scope(self):
        self.current_scope = None

    def add_symbol(self, name, type_):
        if self.current_scope:
            self.symbols[self.current_scope][name] = type_
        else:
            self.symbols[name] = type_

    def lookup(self, name):
        if self.current_scope and name in self.symbols[self.current_scope]:
            return self.symbols[self.current_scope][name]
        return self.symbols.get(name)

symbol_table = SymbolTable()

class xamaListener(ParseTreeListener):
    def enterVar_decl(self, ctx:xamaParser.Var_declContext):
        type_ = ctx.type_().getText()
        ids = ctx.id_list().getText().split(',')
        for id_ in ids:
            if symbol_table.lookup(id_):
                print(f"Erro: Variável '{id_}' já declarada")
            else:
                symbol_table.add_symbol(id_, type_)
                print(f"Declaração de variável: {id_} do tipo {type_}")

    def enterConst_decl(self, ctx:xamaParser.Const_declContext):
        type_ = ctx.type_().getText()
        id_ = ctx.ID().getText()
        if symbol_table.lookup(id_):
            print(f"Erro: Constante '{id_}' já declarada")
        else:
            symbol_table.add_symbol(id_, type_)
            print(f"Declaração de constante: {id_} do tipo {type_}")

    def enterFunc_decl(self, ctx:xamaParser.Func_declContext):
        id_ = ctx.ID().getText()
        return_type = ctx.type_().getText()
        param_list = ctx.param_list().getText()
        # Para simplificação, estamos apenas adicionando a função sem verificar os parâmetros agora.
        if symbol_table.lookup(id_):
            print(f"Erro: Função '{id_}' já declarada")
        else:
            symbol_table.add_symbol(id_, f"function({param_list}): {return_type}")
            print(f"Declaração de função: {id_} retornando {return_type} com parâmetros {param_list}")

    def enterPrint_stmt(self, ctx:xamaParser.Print_stmtContext):
        print("Comando de impressão")

    def enterLv(self, ctx:xamaParser.LvContext):
        id_ = ctx.ID().getText()
        if not symbol_table.lookup(id_):
            print(f"Erro: Variável ou função '{id_}' não declarada")

del xamaParser