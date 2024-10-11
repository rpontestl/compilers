grammar xama;

/* Programa */
program : decl_list EOF;

/* Lista de Declarações */
decl_list : decl_list decl 
          | decl;

/* Declaração */
decl : var_decl 
     | const_decl 
     | type_decl 
     | func_decl;

/* Declaração de Variáveis */
var_decl : 'tmp' type id_list ';';

/* Declaração de Constante */
const_decl : 'cte' type ID '=' expr ';';

/* Tipo */
type : 'integer'
     | 'char'
     | 'boolean'
     | 'string'
     | 'float'
     | ID;

/* Lista de Identificadores */
id_list : id_list ',' ID 
        | ID;

/* Declaração de Tipo */
type_decl : 'type' ID '=' 'array' '[' NUM ']' 'of' type
          | 'type' ID '=' 'struct' '{' const_decl '}'
          | 'type' ID '=' type;

/* Funções */
func_decl : 'function' ID '(' param_list ')' ':' type block;

/* Lista de Parâmetros */
param_list : param_list ',' ID ':' type 
           | ID ':' type;

/* Bloco */
block : '{' var_const_list stmt_list '}';

/* Lista de Variáveis/Constantes */
var_const_list : var_const_list var_decl
               | var_const_list const_decl
               | var_decl
               | const_decl;

/* Lista de Statements */
stmt_list : stmt_list stmt 
          | stmt;

/* Statement */
stmt : 'if' '(' expr ')' stmt 
     | 'if' '(' expr ')' stmt 'else' stmt 
     | 'while' '(' expr ')' stmt 
     | 'do' stmt 'while' '(' expr ')' ';' 
     | block 
     | lv '=' expr ';' 
     | 'break' ';' 
     | 'continue' ';' 
     | 'return' expr ';'
     | print_stmt;

/* Comando de Impressão */
print_stmt : 'print' '(' expr_list ')' ';'; 

/* Expressão */
expr : expr '&&' cond 
     | expr '||' cond 
     | cond;

cond : cond '&' bitwise 
     | cond '|' bitwise 
     | cond '^' bitwise 
     | bitwise;

bitwise : bitwise '<' relational 
        | bitwise '>' relational 
        | bitwise '<=' relational 
        | bitwise '>=' relational 
        | bitwise '==' relational 
        | bitwise '!=' relational 
        | relational;

relational : relational '>>' shift
           | relational '<<' shift
           | shift;

shift : shift '+' add_sub
      | shift '-' add_sub
      | add_sub;

add_sub : add_sub '*' mul_div
        | add_sub '/' mul_div
        | mul_div;

mul_div : lv
        | '++' lv
        | '--' lv
        | lv '++'
        | lv '--'
        | '(' expr ')'
        | ID '(' expr_list ')'
        | '-' mul_div
        | '!' mul_div
        | TRUE
        | FALSE
        | CHR
        | STR
        | NUM;

/* Lista de Expressões */
expr_list : expr_list ',' expr 
          | expr;

/* Variável */
lv : lv '.' ID 
   | lv '[' expr ']'
   | ID;

/* Terminais */
ID   : [a-zA-Z][a-zA-Z0-9]*;
TRUE : 'true';
FALSE: 'false';
CHR  : '\'' . '\'';
STR  : '"' .*? '"';
NUM  : [0-9]+ ('.' [0-9]+)?;

// Regra para ignorar espaços em branco, tabulações e quebras de linha
WS : [ \t\r\n]+ -> skip;  // Ignora espaços, tabulações e quebras de linha
