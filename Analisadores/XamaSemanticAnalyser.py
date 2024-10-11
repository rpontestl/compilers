from antlr4 import *

if "." in __name__:
    from .XamaSyntaticAnalyser import XamaSyntaticAnalyser
else:
    from Analisadores.XamaSyntaticAnalyser import XamaSyntaticAnalyser

class SymbolTable:
    def __init__(self):
        self.scopes = [{}]  
    def enter_scope(self):
        self.scopes.append({}) 
    def exit_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()  
    def add_symbol(self, name, type_):
        if name in self.scopes[-1]:
            return False  
        self.scopes[-1][name] = type_
        return True

    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None  
    
    def check_type(self, type1, type2):
        if type1 == type2:
            return True
        if type1 == 'integer' and type2 == 'float' or type1 == 'float' and type2 == 'integer':
            return True
        return False

symbol_table = SymbolTable()

class XamaSemanticAnalyser(ParseTreeListener):
    def enterVar_decl(self, ctx:XamaSyntaticAnalyser.Var_declContext):
        type_ = ctx.type_().getText()  
        ids = ctx.id_list().getText().split(',') 
        for id_ in ids:
            if not symbol_table.add_symbol(id_, type_):
                print(f"Erro: Variável '{id_}' já declarada no escopo atual")

    def enterConst_decl(self, ctx:XamaSyntaticAnalyser.Const_declContext):
        type_ = ctx.type_().getText()  
        id_ = ctx.ID().getText()  
        if not symbol_table.add_symbol(id_, type_):
            print(f"Erro: Constante '{id_}' já declarada no escopo atual")

    def enterFunc_decl(self, ctx:XamaSyntaticAnalyser.Func_declContext):
        id_ = ctx.ID().getText()  
        return_type = ctx.type_().getText() 
        param_list = ctx.param_list().getText()  
        if not symbol_table.add_symbol(id_, f"function({param_list}): {return_type}"):
            print(f"Erro: Função '{id_}' já declarada no escopo atual")

        symbol_table.enter_scope()  
        param_list.strip(' ')
        typed_params = param_list.split(',')
        for param in typed_params:
            splitted_param = param.split(':')
            param_id = splitted_param[0]
            param_type = splitted_param[1]
            symbol_table.add_symbol(param_id, param_type)
        
            

    def exitFunc_decl(self, ctx:XamaSyntaticAnalyser.Func_declContext):
        symbol_table.exit_scope()  
    def enterPrint_stmt(self, ctx:XamaSyntaticAnalyser.Print_stmtContext):
        pass
    def enterLv(self, ctx:XamaSyntaticAnalyser.LvContext):
        id_ = ctx.ID().getText()
        if not symbol_table.lookup(id_):
            print(f"Erro: Variável ou função '{id_}' não declarada")

del XamaSyntaticAnalyser
