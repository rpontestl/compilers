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
    def __init__(self):
        self.assembly_code = []
        self.label_count = 0

    def emit(self, instruction):
        self.assembly_code.append(instruction)
        
    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"


    def enterVar_decl(self, ctx:XamaSyntaticAnalyser.Var_declContext):
        type_ = ctx.type_().getText()  
        ids = ctx.id_list().getText().split(',') 
        for id_ in ids:
            if not symbol_table.add_symbol(id_, type_):
                print(f"Erro: Variável '{id_}' já declarada no escopo atual")
            else:
                self.emit(f"{id_} dd 0") 

    def enterConst_decl(self, ctx:XamaSyntaticAnalyser.Const_declContext):
        type_ = ctx.type_().getText()  
        id_ = ctx.ID().getText()  
        value = ctx.expr().getText()
        if not symbol_table.add_symbol(id_, type_):
            print(f"Erro: Constante '{id_}' já declarada no escopo atual")
        else:
            self.emit(f"{id_} equ {value}")  

    def enterFunc_decl(self, ctx:XamaSyntaticAnalyser.Func_declContext):
        id_ = ctx.ID().getText()  
        return_type = ctx.type_().getText() 
        param_list = ctx.param_list().getText()  
        is_symbol_already_included = not symbol_table.add_symbol(id_, f"function({param_list}): {return_type}")
        if is_symbol_already_included:
            print(f"Erro: Função '{id_}' já declarada no escopo atual")
        else:
            self.emit(f"{id_}:") 

        symbol_table.enter_scope()  
        if not is_symbol_already_included:
            typed_params = param_list.replace(" ", "").split(',')
            for param in typed_params:
                splitted_param = param.split(':')
                param_id = splitted_param[0]
                param_type = splitted_param[1]
                symbol_table.add_symbol(param_id, param_type)
                self.emit(f"{param_id} dd 0")  

    def exitFunc_decl(self, ctx:XamaSyntaticAnalyser.Func_declContext):
        symbol_table.exit_scope()  
        self.emit("ret")  

    def enterPrint_stmt(self, ctx:XamaSyntaticAnalyser.Print_stmtContext):
        self.emit("call print") 
        
    # Chama a função print (implemente em assembly)

    def enterStmt(self, ctx:XamaSyntaticAnalyser.StmtContext):
        if ctx.getChild(0).getText() == 'if':
            self.enterIf_stmt(ctx)
        elif ctx.getChild(0).getText() == 'while':
            self.enterWhile_stmt(ctx)
        elif ctx.getChild(0).getText() == 'print':
            self.enterPrint_stmt(ctx.print_stmt())
        elif ctx.lv():
            self.handleLv(ctx.lv())

    def enterIf_stmt(self, ctx:XamaSyntaticAnalyser.StmtContext):
        label_else = self.new_label()
        label_end = self.new_label()
        condition = ctx.expr().getText()
        self.emit(f"cmp {condition}, 0")
        self.emit(f"je {label_else}")
        # Emitir o código para o bloco if
        self.enterStmt(ctx.stmt(0))
        self.emit(f"jmp {label_end}")
        self.emit(f"{label_else}:")
        if ctx.stmt(1):
            self.enterStmt(ctx.stmt(1))  # Emitir o código para o bloco else, se existir
        self.emit(f"{label_end}:")

    def enterWhile_stmt(self, ctx:XamaSyntaticAnalyser.StmtContext):
        label_start = self.new_label()
        label_end = self.new_label()
        condition = ctx.expr().getText()
        self.emit(f"{label_start}:")
        self.emit(f"cmp {condition}, 0")
        self.emit(f"je {label_end}")
        # Emitir o código para o bloco while
        self.enterStmt(ctx.stmt(0))
        self.emit(f"jmp {label_start}")
        self.emit(f"{label_end}:")
        
    def handleLv(self, ctx:XamaSyntaticAnalyser.LvContext):
        id_ = ctx.ID().getText()
        if not symbol_table.lookup(id_):
            print(f"Erro: Variável ou função '{id_}' não declarada")
        else:
            self.emit(f"mov eax, [{id_}]")

    def handleAssign(self, ctx):
        left_value = ctx.lv().getText()
        expression = ctx.expr().getText()
        self.enterExpr(ctx.expr())
        self.emit(f"mov [{left_value}], eax")


    def enterExpr(self, ctx:XamaSyntaticAnalyser.ExprContext):
        if len(ctx.children) == 3:
            # Lida com expressões binárias (ex: a + b)
            self.handleBinaryExpr(ctx)
        else:
            # Lidar com variáveis ou valores literais
            if hasattr(ctx, 'lv') and ctx.lv():  # Verifica se lv() existe
                self.handleLv(ctx.lv())
            else:
                # Trata outras expressões, como constantes e literais
                text = ctx.getText()
                if text.isdigit():  # Verifica se é um número
                    self.emit(f"mov eax, {text}")
                elif text in ['true', 'false']:  # Verifica se é um valor booleano
                    self.emit(f"mov eax, {'1' if text == 'true' else '0'}")
                else:
                    print(f"Erro: Expressão não reconhecida: {text}")
            
    def handleBinaryExpr(self, ctx):
        left = ctx.getChild(0).getText()
        operator = ctx.getChild(1).getText()
        right = ctx.getChild(2).getText()

        if left.isdigit():
            self.emit(f"mov eax, {left}")
        else:
            self.handleLv(ctx.getChild(0))

        if right.isdigit():
            if operator == '+':
                self.emit(f"add eax, {right}")
            elif operator == '-':
                self.emit(f"sub eax, {right}")
        else:
            if operator == '+':
                self.emit(f"add eax, [{right}]")
            elif operator == '-':
                self.emit(f"sub eax, [{right}]")
 
    def get_assembly_code(self):
        return self.assembly_code
            
del XamaSyntaticAnalyser
