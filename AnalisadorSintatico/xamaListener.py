# Generated from xama.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .xamaParser import xamaParser
else:
    from xamaParser import xamaParser

# This class defines a complete listener for a parse tree produced by xamaParser.
class xamaListener(ParseTreeListener):

    # Enter a parse tree produced by xamaParser#program.
    def enterProgram(self, ctx:xamaParser.ProgramContext):
        pass

    # Exit a parse tree produced by xamaParser#program.
    def exitProgram(self, ctx:xamaParser.ProgramContext):
        pass


    # Enter a parse tree produced by xamaParser#decl_list.
    def enterDecl_list(self, ctx:xamaParser.Decl_listContext):
        pass

    # Exit a parse tree produced by xamaParser#decl_list.
    def exitDecl_list(self, ctx:xamaParser.Decl_listContext):
        pass


    # Enter a parse tree produced by xamaParser#decl.
    def enterDecl(self, ctx:xamaParser.DeclContext):
        pass

    # Exit a parse tree produced by xamaParser#decl.
    def exitDecl(self, ctx:xamaParser.DeclContext):
        pass


    # Enter a parse tree produced by xamaParser#var_decl.
    def enterVar_decl(self, ctx:xamaParser.Var_declContext):
        pass

    # Exit a parse tree produced by xamaParser#var_decl.
    def exitVar_decl(self, ctx:xamaParser.Var_declContext):
        pass


    # Enter a parse tree produced by xamaParser#const_decl.
    def enterConst_decl(self, ctx:xamaParser.Const_declContext):
        pass

    # Exit a parse tree produced by xamaParser#const_decl.
    def exitConst_decl(self, ctx:xamaParser.Const_declContext):
        pass


    # Enter a parse tree produced by xamaParser#type.
    def enterType(self, ctx:xamaParser.TypeContext):
        pass

    # Exit a parse tree produced by xamaParser#type.
    def exitType(self, ctx:xamaParser.TypeContext):
        pass


    # Enter a parse tree produced by xamaParser#id_list.
    def enterId_list(self, ctx:xamaParser.Id_listContext):
        pass

    # Exit a parse tree produced by xamaParser#id_list.
    def exitId_list(self, ctx:xamaParser.Id_listContext):
        pass


    # Enter a parse tree produced by xamaParser#type_decl.
    def enterType_decl(self, ctx:xamaParser.Type_declContext):
        pass

    # Exit a parse tree produced by xamaParser#type_decl.
    def exitType_decl(self, ctx:xamaParser.Type_declContext):
        pass


    # Enter a parse tree produced by xamaParser#func_decl.
    def enterFunc_decl(self, ctx:xamaParser.Func_declContext):
        pass

    # Exit a parse tree produced by xamaParser#func_decl.
    def exitFunc_decl(self, ctx:xamaParser.Func_declContext):
        pass


    # Enter a parse tree produced by xamaParser#param_list.
    def enterParam_list(self, ctx:xamaParser.Param_listContext):
        pass

    # Exit a parse tree produced by xamaParser#param_list.
    def exitParam_list(self, ctx:xamaParser.Param_listContext):
        pass


    # Enter a parse tree produced by xamaParser#block.
    def enterBlock(self, ctx:xamaParser.BlockContext):
        pass

    # Exit a parse tree produced by xamaParser#block.
    def exitBlock(self, ctx:xamaParser.BlockContext):
        pass


    # Enter a parse tree produced by xamaParser#var_const_list.
    def enterVar_const_list(self, ctx:xamaParser.Var_const_listContext):
        pass

    # Exit a parse tree produced by xamaParser#var_const_list.
    def exitVar_const_list(self, ctx:xamaParser.Var_const_listContext):
        pass


    # Enter a parse tree produced by xamaParser#stmt_list.
    def enterStmt_list(self, ctx:xamaParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by xamaParser#stmt_list.
    def exitStmt_list(self, ctx:xamaParser.Stmt_listContext):
        pass


    # Enter a parse tree produced by xamaParser#stmt.
    def enterStmt(self, ctx:xamaParser.StmtContext):
        pass

    # Exit a parse tree produced by xamaParser#stmt.
    def exitStmt(self, ctx:xamaParser.StmtContext):
        pass


    # Enter a parse tree produced by xamaParser#print_stmt.
    def enterPrint_stmt(self, ctx:xamaParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by xamaParser#print_stmt.
    def exitPrint_stmt(self, ctx:xamaParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by xamaParser#expr.
    def enterExpr(self, ctx:xamaParser.ExprContext):
        pass

    # Exit a parse tree produced by xamaParser#expr.
    def exitExpr(self, ctx:xamaParser.ExprContext):
        pass


    # Enter a parse tree produced by xamaParser#cond.
    def enterCond(self, ctx:xamaParser.CondContext):
        pass

    # Exit a parse tree produced by xamaParser#cond.
    def exitCond(self, ctx:xamaParser.CondContext):
        pass


    # Enter a parse tree produced by xamaParser#bitwise.
    def enterBitwise(self, ctx:xamaParser.BitwiseContext):
        pass

    # Exit a parse tree produced by xamaParser#bitwise.
    def exitBitwise(self, ctx:xamaParser.BitwiseContext):
        pass


    # Enter a parse tree produced by xamaParser#relational.
    def enterRelational(self, ctx:xamaParser.RelationalContext):
        pass

    # Exit a parse tree produced by xamaParser#relational.
    def exitRelational(self, ctx:xamaParser.RelationalContext):
        pass


    # Enter a parse tree produced by xamaParser#shift.
    def enterShift(self, ctx:xamaParser.ShiftContext):
        pass

    # Exit a parse tree produced by xamaParser#shift.
    def exitShift(self, ctx:xamaParser.ShiftContext):
        pass


    # Enter a parse tree produced by xamaParser#add_sub.
    def enterAdd_sub(self, ctx:xamaParser.Add_subContext):
        pass

    # Exit a parse tree produced by xamaParser#add_sub.
    def exitAdd_sub(self, ctx:xamaParser.Add_subContext):
        pass


    # Enter a parse tree produced by xamaParser#mul_div.
    def enterMul_div(self, ctx:xamaParser.Mul_divContext):
        pass

    # Exit a parse tree produced by xamaParser#mul_div.
    def exitMul_div(self, ctx:xamaParser.Mul_divContext):
        pass


    # Enter a parse tree produced by xamaParser#expr_list.
    def enterExpr_list(self, ctx:xamaParser.Expr_listContext):
        pass

    # Exit a parse tree produced by xamaParser#expr_list.
    def exitExpr_list(self, ctx:xamaParser.Expr_listContext):
        pass


    # Enter a parse tree produced by xamaParser#lv.
    def enterLv(self, ctx:xamaParser.LvContext):
        pass

    # Exit a parse tree produced by xamaParser#lv.
    def exitLv(self, ctx:xamaParser.LvContext):
        pass



del xamaParser