import os


# First & Follow

first_Program          = ['const', 'procedure', 'var', 'struct']
follow_Program         = ['$']

first_Decls =            ['function',  'procedure']
follow_Decls =          ['$']

first_Decl    =         ['function', 'procedure']
follow_Decl    =        ['function', '$', 'procedure']

first_Structs   =       [ 'struct']
follow_Structs   =      ['const', 'procedure', 'var']

first_StructBlock =     ['struct']
follow_StructBlock =    ['const', 'procedure', 'var', 'struct']

first_Extends       =   [ 'extends']
follow_Extends       =  ['{']

first_ConstBlock      = [ 'const']
follow_ConstBlock      =['}', 'procedure', 'var']

first_VarBlock        = [ 'var']
follow_VarBlock        =['local', 'print', 'if', ';', 'procedure', 'return', 'id', 'read', '}', 'global', 'while', '}']

first_Type          =   ['string', 'int', 'real', 'boolean', 'struct']
follow_Type          =  ['id']

first_Typedef         = ['typedef']
follow_Typedef        = ['string', 'int', 'typedef', 'real', 'boolean', 'id', 'global', 'local', 'struct', '}']

first_VarDecls         =['local', 'string', 'int', 'typedef', 'real',  'boolean', 'struct', 'id', 'global']
follow_VarDecls        =['}']

first_VarDecl          =['local', 'string', 'int', 'typedef', 'real', 'boolean', 'struct', 'id', 'global']
follow_VarDecl         =['local', 'string', 'int', 'typedef', 'real', 'boolean', 'struct', 'id', '}', 'global']

first_VarId            =['=', '.', '[', '--', 'id', '++', '(']
follow_VarId           =['local', 'string', 'int', 'typedef', 'real', 'boolean', 'struct', 'id', '}', 'global']

first_Var              =['id']
follow_Var             =[',', ';']

first_VarList=          [ ',']
follow_VarList=         [';']

first_ConstDecls=       ['local', 'string', 'int', 'typedef', 'real',  'boolean', 'struct', 'id', 'global']
follow_ConstDecls=      ['}']

first_ConstDecl  =      ['local', 'string', 'int', 'typedef', 'real', 'boolean', 'struct', 'id', 'global']
follow_ConstDecl  =     ['local', 'string', 'int', 'typedef', 'real', 'boolean', 'struct', 'id', '}', 'global']

first_ConstId     =     ['=', '.', '[', '--', 'id', '++', '(']
follow_ConstId     =    ['local', 'string', 'int', 'typedef', 'real', 'boolean', 'struct', 'id', '}', 'global']

first_Const        =    ['id']
follow_Const        =   ['=', ',']

first_ConstList     =   ['=', ',']
follow_ConstList     =  ['local', 'string', 'int', 'typedef', 'real', ';', 'boolean', 'struct', 'id', '}', 'global']

first_DeclAtribute   =  ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global', '{']
follow_DeclAtribute   = [';']

first_ArrayDecl=        ['{']
follow_ArrayDecl=       [';']

first_ArrayVector=      [ ',']
follow_ArrayVector=     [';']

first_ArrayDef    =     ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_ArrayDef    =    ['}']

first_ArrayExpr    =    [ ',']
follow_ArrayExpr    =   ['}']

first_Array         =   ['[']
follow_Array         =  [')', '++', '=', ';', '+', '>=', '&&', '-', '>', '!=', '.', '[', '||', ',', ']', '<=', '--', '==', '*', '<', '/', '}']

first_Index          =  ['false', 'local', 'str', 'true', '!', '(',  'id', 'num', 'global']
follow_Index          = [']']

first_Arrays          = [ '[']
follow_Arrays          =[';', '+', '-', ']', '<=', '--', '==', '*', '/', '}', ')', '++', '=', '>=', '&&', '>', '!=', '.', '||', ',', '<']

first_Assign =           ['=', '--', '++']
follow_Assign =          ['string', 'int', 'typedef', 'real', ';', 'return', 'else', 'boolean', 'id', 'global', 'local', 'print', 'if', 'struct', 'read', '}', 'while', '{']

first_Access  =         ['.']
follow_Access  =        [')', '++', '=', ';', '+', '>=', '&&', '-', '>', '!=', '.', '||', ',', ']', '<=', '--', '==', '*', '<', '/', '}']

first_Accesses =        ['.', 'ε']
follow_Accesses =       [')', '++', '=', ';', '+', '>=', '&&', '-', '>', '!=', '||', ',', ']', '<=', '--', '==', '*', '<', '/', '}']

first_Args      =       ['false', 'local', 'str', 'true', '!', '(',  'id', 'num', 'global']
follow_Args      =      [')']

first_ArgsList   =      [ ',']
follow_ArgsList   =     [')']

first_FuncDecl    =     ['function']
follow_FuncDecl    =    ['function', '$', 'procedure']

first_StartBlock   =    ['procedure']
follow_StartBlock   =   ['function', '$', 'procedure']

first_ProcDecl      =   ['procedure']
follow_ProcDecl      =  ['function', '$', 'procedure']

first_ParamType      =  ['string', 'boolean', 'struct', 'int', 'id', 'real']
follow_ParamType      = ['id']

first_Params          = [ 'string', 'boolean', 'struct', 'int', 'id', 'real']
follow_Params          =[')']

first_Param =            ['string', 'boolean', 'struct', 'int', 'id', 'real']
follow_Param =           [',', ')']

first_ParamsList =       [ ',']
follow_ParamsList =      [')']

first_ParamArrays =     [ '[']
follow_ParamArrays =    [',', ')']

first_ParamMultArrays=  [ '[']
follow_ParamMultArrays= [',', ')']

first_FuncBlock =        ['{']
follow_FuncBlock =       ['function', '$', 'procedure']

first_FuncStms   =      ['local', 'print', 'if', ';', 'return',  'id', 'read', 'global', 'while', '{']
follow_FuncStms   =     ['}']

first_FuncStm     =     ['local', 'print', 'if', ';', 'return', 'id', 'read', 'global', 'while', '{']
follow_FuncStm     =    [';', 'return', 'else', 'id', 'global', 'local', 'print', 'if', 'read', '}', 'while', '{']

first_ElseStm      =    [ 'else']
follow_ElseStm      =   ['local', 'print', 'if', ';', 'return', 'id', 'read', 'global', 'while', '{']

first_FuncNormalStm =   ['local', 'print', ';', 'return', 'id', 'read', 'global', '{']
follow_FuncNormalStm =  [';', 'return', 'else', 'id', 'global', 'local', 'print', 'if', 'read', '}', 'while', '{']

first_VarStm         =  ['local', 'print', 'id', 'read', 'global']
follow_VarStm         = [';', 'return', 'else', 'id', 'global', 'local', 'print', 'if', 'read', '}', 'while', '{']

first_StmId =            ['=', '.', '[', '--', '(', '++']
follow_StmId =           ['string', 'int', 'typedef', 'real', ';', 'return', 'else', 'boolean', 'id', 'global', 'local', 'print', 'if', 'struct', 'read', '}', 'while', '{']

first_StmScope =         ['local', 'global']
follow_StmScope =        ['string', 'int', 'typedef', 'real', ';', 'return', 'else', 'boolean', 'id', 'global', 'local', 'print', 'if', 'struct', 'read', '}', 'while', '{']

first_StmCmd    =       ['read', 'print']
follow_StmCmd    =      [';', 'return', 'else', 'id', 'global', 'local', 'print', 'if', 'read', '{', 'while', '{']

first_Expr       =      ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_Expr       =     [';', ')', ',', ']', '}']

first_Or          =     ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_Or          =    [';', ')', ',', ']', '}']

first_Or_          =    [ '||']
follow_Or_          =   [';', ')', ',', ']', '}']

first_And           =   ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_And           =  ['||', ',', ')', ']', ';', '}']

first_And_           =  ['&&', 'ε']
follow_And_           = ['||', ',', ')', ']', ';', '}']

first_Equate =           ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_Equate =          ['||', ',', ')', ']', ';', '&&', '}']

first_Equate_ =         [ '==', '!=']
follow_Equate_ =        ['||', ',', ')', ']', ';', '&&', '}']

first_Compare  =        ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_Compare  =       ['||', ',', ')', ']', ';', '==', '&&', '}', '!=']

first_Compare_  =       [ '<', '>=', '>', '<=']
follow_Compare_  =      ['||', ',', ')', ']', ';', '==', '&&', '}', '!=']

first_Add        =      ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_Add        =     [')', ';', '>=', '&&', '>', '!=', '||', ',', ']', '<=', '==', '<', '}']

first_Add_        =     [ '-', '+']
follow_Add_        =    [')', ';', '>=', '&&', '>', '!=', '||', ',', ']', '<=', '==', '<', '}']

first_Mult         =    ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_Mult         =   [')', ';', '+', '>=', '&&', '-', '>', '!=', '||', ',', ']', '<=', '==', '<', '}']

first_Mult_         =   [ '/', '*']
follow_Mult_         =  [')', ';', '+', '>=', '&&', '-', '>', '!=', '||', ',', ']', '<=', '==', '<', '}']

first_Unary          =  ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_Unary          = [')', ';', '+', '>=', '&&', '-', '>', '!=', '||', ',', ']', '<=', '==', '*', '<', '/', '}']

first_Value =            ['false', 'local', 'str', 'true', '(', 'id', 'num', 'global']
follow_Value =           [')', ';', '+', '>=', '&&', '-', '>', '!=', '||', ',', ']', '<=', '==', '*', '<', '/', '}']

first_IdValue =          ['.',  '[', '(']
follow_IdValue =         [')', ';', '+', '>=', '&&', '-', '>', '!=', '||', ',', ']', '<=', '==', '*', '<', '/', '}']

first_LogExpr  =        ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_LogExpr  =       [')']

follow_LogOr =           [')']
first_LogOr     =       ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']

first_LogOr_     =      [ '||']
follow_LogOr_ =          [')']

first_LogAnd   =        ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_LogAnd  =        [')', '||']

first_LogAnd_   =       ['&&', 'ε']
follow_LogAnd_  =       [')', '||']

first_LogEquate  =      ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_LogEquate =      ['||', '&&', ')']

first_LogEquate_  =     [ '==', '!=']
follow_LogEquate_ =     ['||', '&&', ')']

first_LogCompare   =    ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_LogCompare  =    ['==', '||', '&&', ')', '!=']

first_LogCompare_   =   [ '<', '>=', '>', '<=']
follow_LogCompare_  =   ['==', '||', '&&', ')', '!=']

first_LogUnary       =  ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_LogUnary      =  ['||', ')', '<=', '==', '<', '>=', '&&', '>', '!=']

first_LogValue        = ['false', 'local', 'str', 'true', '(', 'id', 'num', 'global']
follow_LogValue       = ['||', ')', '<=', '==', '<', '>=', '&&', '>', '!=']

sync_words = ["start", "procedure", "function", "if", "then", "while", "print", "read"]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - -  Program Flow Functions - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def next_token():
    global tokens, token, tokens_position
    tokens_position += 1
    token = tokens[tokens_position][1]

def print_error_msg(expected_token):
    global token, fout
    msg = f'Erro linha {tokens[tokens_position][0]}:\n\
        Esperava {expected_token}, recebido {token}\n\n'
    print(msg)
    fout.write(msg)

def recover_from_error(sync_list):
    global tokens, tokens_position
    i = tokens_position
    while i+1 < len(tokens):
        i += 1
        if tokens[i][1] in sync_list:
            print(f'Ignorados {i - tokens_position} tokens após erro\n') # TODO: remove?
            tokens_position = i
            break
    if i == len(tokens):
        i = sync_function(sync_words, normal_flow=False)
    if i == len(tokens):
        print('Não foi possível recuperar deste erro até o final do arquivo\n')

def find_token_nearby(expected_token):
    global tokens, token, tokens_position
    # TODO: Add case if expected_token = first or follow list
    if token == expected_token:
        return True
    for i in range(1, 3): # check neighboors
        if tokens[tokens_position+i][1] == expected_token:
            tokens_position += i
            token = tokens[tokens_position+i][1]
            return True
        if tokens[tokens_position-i][1] == expected_token:
            tokens_position -= i
            token = tokens[tokens_position-i][1]
            return True
    return False

def raise_error(expected_token, sync_list=None):
    global tokens, token, tokens_position, fout, errors_count
    errors_count += 1
    print_error_msg(expected_token)

    if expected_token in ["{", "}", "(", ")", "[", "]"]:
        if find_token_nearby(expected_token):
            return
    if sync_list != None:
        recover_from_error(sync_list)

def success():
    global fout, errors_count
    if errors_count == 0:
        msg = 'Análise Sintática concluída com sucesso!\n'
        print(msg)
        fout.write(msg)
    else:
        msg = f'Análise Sintática concluída com {errors_count} erros\n'
        print(msg)
        fout.write(msg)

def sync_function(sync_list, normal_flow=True):
    global tokens, tokens_position
    i = tokens_position
    while i < len(tokens):
        i += 1
        token = [tokens][i][1]
        if token in sync_list:
            print(f'Ignorados {i - tokens_position} tokens após erro\n') # TODO: remove?
            tokens_position = i
            break
    if not normal_flow:
        if token == 'start':
            start()
            decls()
            success()
        if token == 'procedure':
            proc_decl()
            decls()
            success()
        if token == 'function':
            func_decl()
            decls()
            success()
        if token == 'if' or token == 'while' or token == 'print' or token == 'read':
            func_stms()
            if token != "}":
                raise_error("}")
            next_token()
            decls()
            success()
        if token == 'then':
            func_stms()
            if token != "}":
                raise_error("}")
            next_token()
            decls()
            success()
    return i

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - -  Production Functions - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def program():
    if token in first_Structs:
        structs()
        const_block()
        var_block()
        start_block()
        decls()
        success()
    elif token in first_ConstBlock:
        const_block()
        var_block()
        start_block()
        decls()
        success()
    elif token in first_VarBlock:
        var_block()
        start_block()
        decls()
        success()
    elif token in first_StartBlock:
        start_block()
        decls()
        success()
    else:
        raise_error(first_Program)

def structs():
    if token in first_StructBlock:
        struct_block()
        structs()

def start():
    if token == "start":
        next_token()
        if token != "(":
            raise_error("(")
        next_token()
        if token != ")":
            raise_error(")")
        next_token()
        func_block()
    else:
        raise_error("start", follow_StartBlock)

def start_block():
    if token == "procedure":
        next_token()
        start()
    else:
        raise_error("procedure", follow_StartBlock)

def decls():
    if token in first_Decl:
        decl()
        decls()

def decl():
    if token in first_FuncDecl:
        func_decl()
    elif token in first_ProcDecl:
        proc_decl()
    else:
        raise_error(first_Decl, follow_Decl)

def struct_block():
    if token == "struct":
        next_token()
        if token == "id":
            next_token()
            extends()
            if token != "{":
                raise_error("{")
            next_token()
            const_block()
            var_block()
            if token == "}":
                next_token()
            else:
                raise_error("}", follow_StructBlock)
        else:
            raise_error("IDENTIFICADOR", follow_StructBlock)
    else:
        raise_error("struct", follow_StructBlock)

def extends():
    if token == "extends":
        next_token()
        if token == "struct":
            next_token()
            if token == "id":
                next_token()

def const_block():
    if token == "const":
        next_token()
        if token != "{":
            raise_error("{")
        next_token()
        const_decls()
        if token != "}":
            raise_error("}")
        next_token()
    else:
        raise_error("const", follow_ConstBlock)

def var_block():
    if token == "var":
        next_token()
        if token != "{":
            raise_error("{")
        next_token()
        var_decls()
        if token != "}":
            raise_error("}")
        next_token()

def type_func():
    if token == "int" or token == "real" or token == "boolean" or token == "string":
        next_token()
    elif token == "struct":
        next_token()
        if token == "id":
            next_token()
    else:
        raise_error(first_Type, follow_Type)

def typedef():
    if token == "typedef":
        next_token()
        type_func()
        if token == "id":
            next_token()
            if token != ";":
                raise_error(';')
            next_token()
        else:
            raise_error("IDENTIFICADOR", follow_TypeDef)
    else:
        raise_error("typedef", follow_TypeDef)

def var_decls():
    if token in first_VarDecl:
        var_decl()
        var_decls()

def var_decl():
    if token in first_Type:
        type_func()
        var()
        var_list()
        if token != ";":
            raise_error(";", follow_VarDecl)
        else:
            next_token()
    elif token in first_Typedef:
        typedef()
    elif token in first_StmScope:
        stm_scope()
    elif token == "id":
        next_token()
        var_id()
    else:
        raise_error(first_VarDecl, follow_VarDecl)

def var_id():
    if token in first_Var:
        var()
        var_list()
        if token == ";":
            next_token()
        else:
            raise_error(";", follow_VarId)
    elif token in first_StmId:
        stm_id()
    else:
        raise_error(first_VarId, follow_VarId)

def var():
    if token == "id":
        next_token()
        arrays()
    else:
        raise_error("IDENTIFICADOR", follow_Var)

def var_list():
    if token == ",":
        next_token()
        var()
        var_list()
    
def const_decls():
    if token in first_ConstDecl:
        const_decl()
        const_decls()

def const_decl():
    if token in first_Type:
        type_func()
        const()
        const_list()
    elif token in first_Typedef:
        typedef()
    elif token in first_StmScope:
        stm_scope()
    elif token == "id":
        next_token()
        const_id()
    else:
        raise_error(first_ConstDecl, follow_ConstDecl)

def const_id():
    if token in first_Const:
        const()
        const_list()
        if token == ";":
            next_token()
        else:
            raise_error(";", follow_ConstId)
    elif token in first_StmId:
        stm_id()
    else:
        raise_error(first_ConstId, follow_ConstId)

def const():
    if token == "id":
        next_token()
        arrays()
    else:
        raise_error("IDENTIFICADOR", follow_Const)

def const_list():
    if token == ",":
        next_token()
        const()
        const_list()
    elif token == "=":
        decl_atribute()
        if token == ";":
            next_token()
        else:
            raise_error(";", follow_ConstList)
    else:
        raise_error(first_ConstList, follow_ConstList)

def decl_atribute():
    if token in first_ArrayDecl:
        array_decl()
    elif token in first_Expr:
        expr()
    else:
        raise_error(first_DeclAtribute, follow_DeclAtribute)

def array_decl():
    if token != "{":
        raise_error("{")
    next_token()
    array_def()
    if token != "}":
        raise_error("}")
    next_token()
    array_vector()

def array_vector():
    if token == ",":
        next_token()
        array_decl()

def array_def():
    if token in first_Expr:
        expr()
        array_expr()
    else:
        raise_error(first_ArrayDef, follow_ArrrayDef)

def array_expr():
    if token == ",":
        next_token()
        array_def()

def array():
    if token != "[":
        raise_error("[")
    next_token()
    index()
    if token != "]":
        raise_error("]")
    next_token()

def index():
    if token in first_Expr:
        expr()

def arrays():
    if token in first_Array:
        array()
        arrays()

def assign():
    if token == "=":
        next_token()
        expr()
        if token == ";":
            next_token()
        else:
            raise_error(";", follow_Assign)
    elif token == "++":
        next_token()
        if token == ";":
            next_token()
        else:
            raise_error(";", follow_Assign)
    elif token == "--":
        next_token()
        if token == ";":
            next_token()
        else:
            raise_error(";", follow_Assign)
    else:
        raise_error(first_Assign, follow_Assign)

def access():
    if token == ".":
        next_token()
        if token == "id":
            next_token()
            arrays()
        else:
            raise_error("IDENTIFICADOR", follow_Access)
    else:
        raise_error(".", follow_Access)
    
def accesses():
    if token in first_Access:
        access()
        accesses()

def args():
    if token in first_Expr:
        expr()
        args_list()

def args_list():
    if token == ",":
        next_token()
        expr()
        args_list()

def func_decl():
    if token == "function":
        next_token()
        param_type()
        if token == "id":
            next_token()
            if token != "(":
                raise_error("(", first_Params)
            next_token()
            params()
            if token != ")":
                raise_error(")", follow_FuncDecl)
            next_token()
            func_block()
        else:
            raise_error("IDENTIFICADOR", follow_FuncDecl)
    else:
        raise_error("function", follow_FuncDecl)

def proc_decl():
    if token == "procedure":
        next_token()
        if token == "id":
            next_token()
            if token != "(":
                raise_error("(", first_Params)
            next_token()
            params()
            if token != ")":
                raise_error(")", first_FuncBlock)
            next_token()
            func_block()
        else:
            raise_error("IDENTIFICADOR", follow_ProcDecl)
    else:
        raise_error("procedure", follow_ProcDecl)

def param_type():
    if token in first_Type:
        type_func()
    elif token == "id":
        next_token()
    else:
        raise_error(first_ParamType, follow_ParamType)

def params():
    if token in first_Param:
        param()
        params_list()

def param():
    if token in first_ParamType:
        param_type()
        if token == "id":
            next_token()
            param_arrays()
        else:
            raise_error("IDENTIFICADOR", follow_Param)
    else:
        raise_error(first_ParamType, follow_ParamType)

def params_list():
    if token == ",":
        next_token()
        param()
        params_list()

def param_arrays():
    if token != "[":
        raise_error("[", ["]"])
    next_token()
    if token != "]":
        raise_error("]", first_ParamMultArrays)
    next_token()
    param_mult_arrays()

def param_mult_arrays():
    if token == "[":
        next_token()
        if token == "num":
            next_token()
            if token != "]":
                raise_error("]", first_ParamMultArrays)
            next_token()
            param_mult_arrays()
        else:
            raise_error("NÚMERO", follow_ParamMultArrays)

def func_block():
    if token != "{":
        raise_error("{", follow_FuncBlock)
    next_token()
    var_block()
    func_stms()
    if token != "}":
        raise_error("}", follow_FuncBlock)
    next_token()

def func_stms():
    if token in first_FuncStm:
        func_stm()
        func_stms()

def func_stm():
    if token == "if":
        next_token()
        if token != "(":
            raise_error("(", first_LogExpr)
        next_token()
        log_expr()
        if token != ")":
            raise_error(")", follow_FuncStm)
        next_token()
        if token == "then":
            next_token()
            func_stm()
            else_stm()
            func_stm()
        else:
            raise_error("then", follow_FuncStm)
    elif token == "while":
        next_token()
        if token != "(":
            raise_error("(", first_LogExpr) # TODO: Add second sync list, follow_FuncStm
        next_token()
        log_expr()
        if token != ")":
            raise_error(")", follow_FuncStm)
        next_token()
        func_stm()
    elif token in first_FuncNormalStm:
        func_normal_stm()
    else:
        raise_error(first_FuncStm, follow_FuncStm)

def else_stm():
    if token == "else":
        next_token()

def func_normal_stm():
    if token == "{":
        next_token()
        func_stms()
        if token != "}":
            raise_error("}", follow_FuncNormalStm)
        next_token()
    elif token in first_VarStm:
        var_stm()
    elif token == ";":
        next_token()
    elif token == "return":
        next_token()
        expr()
        if token == ";":
            next_token()
        else:
            raise_error(";", follow_FuncNormalStm)
    else:
        raise_error(first_FuncNormalStm, follow_FuncNormalStm)

def var_stm():
    if token in first_StmScope:
        stm_scope()
    elif token == "id":
        next_token()
        stm_id()
    elif token in first_StmCmd:
        stm_cmd()
    else:
        raise_error(first_VarStm, follow_VarStm)

def stm_id():
    if token in first_Assign:
        assign()
    elif token in first_Array:
        array()
        arrays()
        accesses()
        assign()
    elif token in first_Access:
        access()
        accesses()
        assign()
    elif token == "(":
        next_token()
        args()
        if token != ")":
            raise_error(")", follow_StmId)
        next_token()
        if token == ";":
            next_token()
        else:
            raise_error(";", follow_StmId)
    else:
        raise_error(first_StmId, follow_StmId)

def stm_scope():
    if token == "local" or token == "global":
        next_token()
        access()
        accesses()
        assign()
    else:
        raise_error(first_StmScope, follow_StmScope)

def stm_cmd():
    if token == "print" or token == "read":
        next_token()
        if token != "(":
            raise_error("(", first_Args) # TODO: third sync
        next_token()
        args()
        if token != ")":
            raise_error(")", follow_StmCmd)
        else:
            next_token()
            if token == ";":
                next_token()
            else:
                raise_error(";", follow_StmCmd)
    else:
        raise_error(first_StmCmd, follow_StmCmd)

def expr():
    if token in first_Or:
        or_func()
    else:
        raise_error(first_Expr, follow_Expr)

def or_func():
    if token in first_And:
        and_func()
        or_()
    else:
        raise_error(first_Or, follow_Or)

def or_():
    if token == "||":
        next_token()
        and_func()
        or_()

def and_func():
    if token in first_Equate:
        equate()
        and_()
    else:
        raise_error(first_And, follow_And)

def and_():
    if token == "&&":
        next_token()
        equate()
        and_()

def equate():
    if token in first_Compare:
        compare()
        equate_()
    else:
        raise_error(first_Equate, follow_Equate)

def equate_():
    if token == "==" or token == "!=":
        next_token()
        compare()
        equate_()

def compare():
    if token in first_Add:
        add()
        compare_()
    else:
        raise_error(first_Compare, follow_Compare)

def compare_():
    if token == "<" or token == ">" or token == "<=" or token == ">=":
        add()
        compare_()

def add_func():
    if token in first_Mult:
        mult()
        add_()
    else:
        raise_error(first_Add, follow_Add)

def add_():
    if token == "+" or token == "-":
        next_token()
        mult()
        add_()

def mult():
    if token in first_Unary:
        unary()
        mult_()
    else:
        raise_error(first_Mult, follow_Mult)

def mult_():
    if token == "*" or token == "/":
        next_token()
        unary()
        mult_()

def unary():
    if token == "!":
        next_token()
        unary()
    elif token in firtst_Value:
        value()
    else:
        raise_error(first_Unary, follow_Unary)

def value():
    if token == "num" or token == "str" or token == "true" or token == "false":
        next_token()
    elif token == "local" or token == "global":
        next_token()
        access()
    elif token == "id":
        next_token()
        id_value()
    elif token == "(":
        next_token()
        expr()
        if token == ")":
            next_token()
        else:
            raise_error(")", follow_Value)
    else:
        raise_error(first_Value, follow_Value)

def id_value():
    if token in first_Arrays:
        arrays()
        accesses()
    elif token == "(":
        next_token()
        args()
        if token == ")":
            next_token()
        else:
            raise_error(")", follow_IdValue)
    else:
        raise_error(first_IdValue, follow_IdValue)

def log_expr():
    if token in first_LogOr:
        log_or()
    else:
        raise_error(first_LogExpr, follow_LogExpr)

def log_or():
    if token in first_LogAnd():
        log_and()
        log_or_()
    else:
        raise_error(first_LogOr, follow_LogOr)

def log_or_():
    if token == "||":
        next_token()
        log_and()
        log_or_()

def log_and():
    if token in first_LogEquate:
        log_equate()
        log_and_()
    else:
        raise_error(first_LogAnd, follow_LogAnd)

def log_and_():
    if token == "&&":
        next_token()
        log_equate()
        log_and_()

def log_equate():
    if token in first_LogCompare:
        log_compare()
        log_equate_()
    else:
        raise_error(first_LogEquate, follow_LogEquate)

def log_equate_():
    if token == "==" or token == "!=":
        next_token()
        log_compare()
        log_equate_()

def log_compare():
    if token in first_LogUnary:
        log_unary()
        log_compare_()
    else:
        raise_error(first_LogCompare, follow_LogCompare)

def log_compare_():
    if token == "<" or token == ">" or token == "<=" or token == ">=":
        next_token()
        log_unary()
        log_compare_()

def log_unary():
    if token == "!":
        next_token()
        log_unary()
    elif token in first_LogValue:
        log_value()
    else:
        raise_error(first_LogUnary, follow_LogUnary)

def log_value():
    if token == "num" or token == "str" or token == "true" or token == "false":
        next_token()
    elif token == "local" or token == "global":
        next_token()
        access()
    elif token == "id":
        next_token()
        id_value()
    elif token == "(":
        next_token()
        log_expr()
        if token == ")":
            next_token()
        else:
            raise_error(")", follow_LogValue)
    else:
        raise_error(first_LogValue, follow_LogValue)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - Main  - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

input_dir = 'lexical_output/'
output_dir = 'syntactic_output/'
files_read = 0
tokens = []
tokens_position = 0
token = ''
errors_count = 0

def read_lexical_output(input_dir):
    global tokens, token, tokens_position, errors_count
    tokens = []
    tokens_position = 0
    errors_count = 0
    
    with open(f'{input_dir}{filename}', 'r') as fin:
        for line in fin.readlines():
            token_info = line.split() 
            # 0 = line_number
            # 1 = token type
            # 2 = token
            if token_info[1] == "SIB": # check all 
                continue
            if token_info[1] == "IDE":
                tokens.append((token_info[0], "id"))
            elif token_info[1] == "NUM":
                tokens.append((token_info[0]), "num")
            else:
                tokens.append((token_info[0], token_info[2]))
        token = tokens[tokens_position][1]

for filename in os.listdir(input_dir):
    read_lexical_output(input_dir)
    file_num = filename.split('.')[0][5:]
    with open(f'{output_dir}saida{file_num}.txt', 'w') as fout:
        program()
    files_read += 1

print(f"Read {files_read} files\
 \nWrote {files_read} files")
