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
follow_Extends       =  ['[']

first_ConstBlock      = [ 'const']
follow_ConstBlock      =[']', 'procedure', 'var']

first_VarBlock        = [ 'var']
follow_VarBlock        =['local', 'print', 'if', ';', 'procedure', 'return', 'id', 'read', ']', 'global', 'while', '[']

first_Type          =   ['string', 'int', 'real', 'boolean', 'struct']
follow_Type          =  ['id']

first_Typedef         = ['typedef']
follow_Typedef        = ['string', 'int', 'typedef', 'real', 'boolean', 'id', 'global', 'local', 'struct', ']']

first_VarDecls         =['local', 'string', 'int', 'typedef', 'real',  'boolean', 'struct', 'id', 'global']
follow_VarDecls        =[']']

first_VarDecl          =['local', 'string', 'int', 'typedef', 'real', 'boolean', 'struct', 'id', 'global']
follow_VarDecl         =['local', 'string', 'int', 'typedef', 'real', 'boolean', 'struct', 'id', ']', 'global']

first_VarId            =['=', '.', '[', '--', 'id', '++', '(']
follow_VarId           =['local', 'string', 'int', 'typedef', 'real', 'boolean', 'struct', 'id', ']', 'global']

first_Var              =['id']
follow_Var             =[',', ';']

first_VarList=          [ ',']
follow_VarList=         [';']

first_ConstDecls=       ['local', 'string', 'int', 'typedef', 'real',  'boolean', 'struct', 'id', 'global']
follow_ConstDecls=      [']']

first_ConstDecl  =      ['local', 'string', 'int', 'typedef', 'real', 'boolean', 'struct', 'id', 'global']
follow_ConstDecl  =     ['local', 'string', 'int', 'typedef', 'real', 'boolean', 'struct', 'id', ']', 'global']

first_ConstId     =     ['=', '.', '[', '--', 'id', '++', '(']
follow_ConstId     =    ['local', 'string', 'int', 'typedef', 'real', 'boolean', 'struct', 'id', ']', 'global']

first_Const        =    ['id']
follow_Const        =   ['=', ',']

first_ConstList     =   ['=', ',']
follow_ConstList     =  ['local', 'string', 'int', 'typedef', 'real', ';', 'boolean', 'struct', 'id', ']', 'global']

first_DeclAtribute   =  ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global', '[']
follow_DeclAtribute   = [';']

first_ArrayDecl=        ['[']
follow_ArrayDecl=       [';']

first_ArrayVector=      [ ',']
follow_ArrayVector=     [';']

first_ArrayDef    =     ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_ArrayDef    =    [']']

first_ArrayExpr    =    [ ',']
follow_ArrayExpr    =   [']']

first_Array         =   ['[']
follow_Array         =  [')', '++', '=', ';', '+', '>=', '&&', '-', '>', '!=', '.', '[', '||', ',', ']', '<=', '--', '==', '*', '<', '/', ']']

first_Index          =  ['false', 'local', 'str', 'true', '!', '(',  'id', 'num', 'global']
follow_Index          = [']']

first_Arrays          = [ '[']
follow_Arrays          =[';', '+', '-', ']', '<=', '--', '==', '*', '/', ']', ')', '++', '=', '>=', '&&', '>', '!=', '.', '||', ',', '<']

first_Assign =           ['=', '--', '++']
follow_Assign =          ['string', 'int', 'typedef', 'real', ';', 'return', 'else', 'boolean', 'id', 'global', 'local', 'print', 'if', 'struct', 'read', ']', 'while', '[']

first_Access  =         ['.']
follow_Access  =        [')', '++', '=', ';', '+', '>=', '&&', '-', '>', '!=', '.', '||', ',', ']', '<=', '--', '==', '*', '<', '/', ']']

first_Accesses =        ['.', 'ε']
follow_Accesses =       [')', '++', '=', ';', '+', '>=', '&&', '-', '>', '!=', '||', ',', ']', '<=', '--', '==', '*', '<', '/', ']']

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

first_FuncBlock =        ['[']
follow_FuncBlock =       ['function', '$', 'procedure']

first_FuncStms   =      ['local', 'print', 'if', ';', 'return',  'id', 'read', 'global', 'while', '[']
follow_FuncStms   =     [']']

first_FuncStm     =     ['local', 'print', 'if', ';', 'return', 'id', 'read', 'global', 'while', '[']
follow_FuncStm     =    [';', 'return', 'else', 'id', 'global', 'local', 'print', 'if', 'read', ']', 'while', '[']

first_ElseStm      =    [ 'else']
follow_ElseStm      =   ['local', 'print', 'if', ';', 'return', 'id', 'read', 'global', 'while', '[']

first_FuncNormalStm =   ['local', 'print', ';', 'return', 'id', 'read', 'global', '[']
follow_FuncNormalStm =  [';', 'return', 'else', 'id', 'global', 'local', 'print', 'if', 'read', ']', 'while', '[']

first_VarStm         =  ['local', 'print', 'id', 'read', 'global']
follow_VarStm         = [';', 'return', 'else', 'id', 'global', 'local', 'print', 'if', 'read', ']', 'while', '[']

first_StmId =            ['=', '.', '[', '--', '(', '++']
follow_StmId =           ['string', 'int', 'typedef', 'real', ';', 'return', 'else', 'boolean', 'id', 'global', 'local', 'print', 'if', 'struct', 'read', ']', 'while', '[']

first_StmScope =         ['local', 'global']
follow_StmScope =        ['string', 'int', 'typedef', 'real', ';', 'return', 'else', 'boolean', 'id', 'global', 'local', 'print', 'if', 'struct', 'read', ']', 'while', '[']

first_StmCmd    =       ['read', 'print']
follow_StmCmd    =      [';', 'return', 'else', 'id', 'global', 'local', 'print', 'if', 'read', ']', 'while', '[']

first_Expr       =      ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_Expr       =     [';', ')', ',', ']', ']']

first_Or          =     ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_Or          =    [';', ')', ',', ']', ']']

first_Or_          =    [ '||']
follow_Or_          =   [';', ')', ',', ']', ']']

first_And           =   ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_And           =  ['||', ',', ')', ']', ';', ']']

first_And_           =  ['&&', 'ε']
follow_And_           = ['||', ',', ')', ']', ';', ']']

first_Equate =           ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_Equate =          ['||', ',', ')', ']', ';', '&&', ']']

first_Equate_ =         [ '==', '!=']
follow_Equate_ =        ['||', ',', ')', ']', ';', '&&', ']']

first_Compare  =        ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_Compare  =       ['||', ',', ')', ']', ';', '==', '&&', ']', '!=']

first_Compare_  =       [ '<', '>=', '>', '<=']
follow_Compare_  =      ['||', ',', ')', ']', ';', '==', '&&', ']', '!=']

first_Add        =      ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_Add        =     [')', ';', '>=', '&&', '>', '!=', '||', ',', ']', '<=', '==', '<', ']']

first_Add_        =     [ '-', '+']
follow_Add_        =    [')', ';', '>=', '&&', '>', '!=', '||', ',', ']', '<=', '==', '<', ']']

first_Mult         =    ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_Mult         =   [')', ';', '+', '>=', '&&', '-', '>', '!=', '||', ',', ']', '<=', '==', '<', ']']

first_Mult_         =   [ '/', '*']
follow_Mult_         =  [')', ';', '+', '>=', '&&', '-', '>', '!=', '||', ',', ']', '<=', '==', '<', ']']

first_Unary          =  ['false', 'local', 'str', 'true', '!', '(', 'id', 'num', 'global']
follow_Unary          = [')', ';', '+', '>=', '&&', '-', '>', '!=', '||', ',', ']', '<=', '==', '*', '<', '/', ']']

first_Value =            ['false', 'local', 'str', 'true', '(', 'id', 'num', 'global']
follow_Value =           [')', ';', '+', '>=', '&&', '-', '>', '!=', '||', ',', ']', '<=', '==', '*', '<', '/', ']']

first_IdValue =          ['.',  '[', '(']
follow_IdValue =         [')', ';', '+', '>=', '&&', '-', '>', '!=', '||', ',', ']', '<=', '==', '*', '<', '/', ']']

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

# read tokens

def next_token(token_list):
    return next(token_list)

def raise_error():
    print('Achei um erro!')

def program():
    if token in first_Structs:
        structs()
        const_block()
        var_block()
        start_block()
        decls()
    if token in first_ConstBlock:
        const_block()
        var_block()
        start_block()
        decls()
    if token in first_VarBlock:
        var_block()
        start_block()
        decls()
    if token in first_StartBlock:
        start_block()
        decls()
    else:
        raise_error()

def structs():
    if token in first_StructBlock:
        struct_block()
        structs()

def start_block():
    if token == "procedure":
        next_token()
        if token == "start":
            next_token()
            if token == "(":
                next_token()
                if token == ")":
                    next_token()
                    func_block()
                else:
                    raise_error()
            else:
                raise_error()
        else:
            raise_error()
    else:
        raise_error()

def decls():
    if token in first_Decl:
        decl()
        decls()

def decl():
    if token in first_FuncDecl:
        func_decl()
    if token in first_ProcDecl:
        proc_decl()
    else:
        raise_error()

def struct_block():
    if token == "struct":
        next_token()
        if token == "id":
            next_token()
            extends()
            if token == "{":
                next_token()
                const_block()
                var_block()
                if token == "}":
                    next_token()
                else:
                    raise_error()
            else:
                raise_error()
        else:
            raise_error()
    else:
        raise_error()

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
        if token == "{":
            next_token()
            const_decls()
            if token == "}":
                next_token()
            else:
                raise_error()
        else:
            raise_error()
    else:
        raise_error()

def var_block():
    if token == "var":
        next_token()
        if token == "{":
            next_token()
            var_decls()
            if token == "}":
                next_token()

def type_func():
    if token == "int" or token == "real" or token == "boolean" or token == "string":
        next_token()
    if token == "struct":
        next_token()
        if token == "id":
            next_token()
    else:
        raise_error()

def typedef():
    if token == "typedef":
        next_token()
        type_func()
        if token == "id":
            next_token()
            if token == ";":
                next_token()
            else:
                raise_error()
        else:
            raise_error()
    else:
        raise_error()

def var_decls():
    if token in first_VarDecl():
        var_decl()
        var_decls()

def var_decl():
    if token in first_Type:
        type_func()
        var()
        var_list()
        if token == ";":
            next_token()
        else:
            raise_error()
    if token in first_Typedef:
        typedef()
    if token in first_StmScope:
        stm_scope()
    if token == "id":
        next_token()
        var_id()
    else:
        raise_error()

def var_id():
    if token in first_Var:
        var()
        var_list()
        if token == ";":
            next_token()
        else:
            raise_error
    if token in first_StmId:
        stm_id()
    else:
        raise_error()

def var():
    if token == "id":
        next_token()
        arrays()
    else:
        raise_error()

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
    if token in first_Typedef:
        typedef()
    if token in first_StmScope:
        stm_scope()
    if token == "id":
        next_token()
        const_id()
    else:
        raise_error()

def const_id():
    if token in first_Const:
        const()
        const_list()
        if token == ";":
            next_token()
        else:
            raise_error()
    if token in first_StmId:
        stm_id()
    else:
        raise_error()

def const():
    if token == "id":
        next_token()
        arrays()
    else:
        raise_error()

def const_list():
    if token == ",":
        next_token()
        const()
        const_list()
    if token == "=":
        decl_atribute()
        if token == ";":
            next_token()
        else:
            raise_error()
    else:
        raise_error()

def decl_atribute():
    if token in first_ArrayDecl:
        array_decl()
    if token in first_Expr:
        expr()
    else:
        raise_error()

def array_decl():
    if token == "{":
        next_token()
        array_def()
        if token == "}":
            next_token()
            array_vector()
        else:
            raise_error()
    else:
        raise_error()

def array_vector():
    
