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
# - - - - - - - - - - - - - - - - - - Semantic  - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

ide_table = {}
func_table = {}  # nome, tipos, parametros,
type_buffer = []
typedef_table = {}
struct_table = {}
func_list = []  # nome, tipos, parametros,

# - - - - - - - - - - - - - - - General - - - - - - - - - - - - - - - - - - - - - - - - -

def get_token_name():
    global tokens, tokens_position
    return tokens[tokens_position][2]

def raise_semantic_error(msg):
    full_msg = f"Erro linha {tokens[tokens_position][0]}\n"
    if msg[-1] != "\n":
        msg += "\n"
    
    full_msg += msg
    print(msg)
    semantic_output_file.write(msg)

# - - - - - - - - - - - - - - - Type checking - - - - - - - - - - - - - - - - - - - - - -

def get_available_types():
    primitive_types = ['int', 'real', 'string', 'boolean']
    struct_types = list(struct_table.keys())
    typedef_types = list(typedef_table.keys())
    return primitive_types + struct_types + typedef_types

def get_num_type(num):
    if "." in num:
        return "real"
    else:
        return "int"

def is_type_correct(expected_type, value, value_general_type):
    if value_general_type == "num":
        if "." in value and expected_type == "real":
            return True
        elif "." not in value and expected_type == "int":
            return True
    elif value_general_type == "str":
        if expected_type == "string":
            return True
    elif value_general_type == "true" or value_general_type == "false" and expected_type == "boolean":
        return True
    return False

# - - - - - - - - - - - - - - - Typedef - - - - - - - - - - - - - - - - - - - - - -

def add_typedef(primitive_type, new_type):
    typedef_table = {new_type: primitive_type}

# - - - - - - - - - - - - - - - Functions - - - - - - - - - - - - - - - - - - - - - -

def append_func(return_type="None"):
    func_list.append({"name": tokens[tokens_position][2],
                    "params": [],
                    "return": return_type
    })

def append_func_params(params):
    func_list[-1]["params"] = params

def get_arg_type(arg):
    if arg is None:
        return None
    available_types = get_available_types()
    if arg in available_types:
        return arg
    if isinstance(arg, dict):
        general_type = arg["general_type"]
        if general_type == 'num':
            return get_num_type(arg["value"])
        if general_type == "str":
            return "string"
        if general_type == "true" or general_type == "false":
            return "boolean"
    if arg in ide_table.keys():
        return ide_table[arg]["type"]
    raise_semantic_error(f'Variável {arg}\
        usada como parâmetro não foi declarada')
    return None

def get_args_types(func_args):
    args_type_list = []
    available_types = get_available_types()
    for arg in func_args:
        args_type_list.append(get_arg_type(arg))
    return args_type_list

def check_func_params(func_id, func_params):
    func_params = get_args_types(func_params)
    idx = 0

    if func_id is not None:
        if func_id in func_table.keys():
            if func_params not in func_table[func_id]["params"]:
                raise_semantic_error(f"Função {func_id} não recebe os argumentos {func_params}")
            else:
                idx = func_table[func_id]["params"].index(func_params)
            return func_table[func_id]["return"][idx]
        else:
            raise_semantic_error(f"Função {func_id} não declarada")

def test_func_list():
    for i in func_list:
        print(i)

def test_func_table():
    for key in func_table.keys():
        print(key, func_table[key])

def transform_func_list():
    for func in func_list:
        name = func["name"]
        if name not in func_table.keys():
            func_table[name] = {"params": [func["params"]],
                                "return": [func["return"]]}
        else:
            func_table[name]["params"].append(func["params"])
            func_table[name]["return"].append(func["return"])

# - - - - - - - - - - - - - - -  Structs - - - - - - - - - - - - - - -

def append_struct(struct_name):
    # TODO: Pegar os campos da struct e adicionar uma lista deles.
    # Pode ser uma tupla com tipo e identificador. Por ex:
    # [(int, a), (real, b), (string, c)]
    # pra struct{
    #    int a = 3
    #    real b = 3.2
    #    string c = "ola Mundo"
    # }
    struct_table["struct_" + struct_name] = None

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - -  Program Flow Functions - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def next_token():
    global tokens, token, tokens_position
    tokens_position += 1
    if tokens_position < len(tokens):
        token = tokens[tokens_position][1]
    else:
        token = "$"

def print_error_msg(expected_token):
    global token, fout
    msg = f'Erro linha {tokens[tokens_position][0]}:\n\
        Esperava {expected_token}, recebido {token}\n\n'
    print(msg)
    fout.write(msg)

def recover_from_error(sync_list):
    global tokens, token, tokens_position
    i = tokens_position + 1
    while i < len(tokens):
        if tokens[i][1] in sync_list:
            print(f'Ignorados {i - tokens_position} tokens após erro\n') # TODO: remove?
            tokens_position = i
            token = tokens[tokens_position][1]
            break
        i += 1
    if i == len(tokens):
        i = sync_function(sync_words, normal_flow=False)
    if i == len(tokens):
        print('Não foi possível recuperar deste erro até o final do arquivo\n')

def find_token_nearby(expected_token):
    global tokens, token, tokens_position
    # TODO: Add case if expected_token = first or follow list
    if token == expected_token:
        return True
    for i in range(1, 3): # check neighboors     >> ((-)
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
        find_token_nearby(expected_token) 
        return
            
    if sync_list is not None:
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
    i = tokens_position + 1
    while i < len(tokens):
        token = tokens[i][1]
        if token in sync_list:
            print(f'Ignorados {i - tokens_position} tokens após erro\n') # TODO: remove?
            tokens_position = i
            break
        i += 1
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
        decls()
        success()
    elif token in first_ConstBlock:
        const_block()
        var_block()
        decls()
        success()
    elif token in first_VarBlock:
        var_block()
        decls()
        success()
    elif token in first_Decls:
        decls()
        success()
    else:
        raise_error(first_Program)

def structs():
    if token in first_StructBlock:
        struct_block()
        structs()

def start():
    transform_func_list()
    test_func_table()
    check_func_params("testFunction", ["int", "real"])  # ok
    check_func_params("testFunction", ["int", "int"])  # erro
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
            struct_name = get_token_name()
            append_struct(struct_name)
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
    token_type = ""
    if token == "int" or token == "real" or token == "boolean" or token == "string":
        token_type = token
        next_token()
        return token_type
    elif token == "struct":
        next_token()
        if token == "id":
            token_type = tokens[tokens_position][2]
            next_token()
            return "struct_" + token_type
    else:
        raise_error(first_Type, follow_Type)

def typedef():
    if token == "typedef":
        next_token()
        primitive_type = type_func()
        if token == "id":
            new_type = get_token_name()
            add_typedef(primitive_type, new_type)
            next_token()
            if token != ";":
                raise_error(';')
            next_token()
        else:
            raise_error("IDENTIFICADOR", follow_Typedef)
    else:
        raise_error("typedef", follow_Typedef)

def var_decls():
    if token in first_VarDecl:
        var_decl()
        var_decls()

def var_decl():
    if token in first_Type:
        var_type = type_func() #TODO Fazer verificacao atribuicao de tipos
        var_name = var()
        var_list()
        ide_table[var_name] = {"type": var_type, "class": "var"}
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
        var_name = get_token_name()
        next_token()
        arrays()
        return var_name
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
        const_type = type_func()
        const_name = const()
        const_value = const_list()
        if const_value is not None:
            if not is_type_correct(const_type, const_value["value"], const_value["general_type"]):
                print("Erro: declaração de constante com tipo inválido.")
            ide_table[const_name] = {"type": const_type, "class": "const"}
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
        const_name = get_token_name()
        next_token()
        arrays()
        return const_name
    else:
        raise_error("IDENTIFICADOR", follow_Const)

def const_list():
    if token == ",":
        next_token()
        const_list() #TODO tratar dos casos lista de constantes
    elif token == "=":
        next_token()
        token_value = decl_atribute()
        if token == ";":
            next_token()
            return token_value
        else:
            raise_error(";", follow_ConstList)
    else:
        raise_error(first_ConstList, follow_ConstList)

def decl_atribute():
    if token in first_ArrayDecl:
        array_decl()
    elif token in first_Expr:
        token_value = expr()
        return token_value
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
        raise_error(first_ArrayDef, follow_ArrayDef)

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
        token_value = expr()
        if token == ";":
            next_token()
            return token_value
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
    return_args = []
    if token in first_Expr:
        return_args += [expr()]
        return_args += args_list()
    return return_args

def args_list():
    return_args = []
    if token == ",":
        next_token()
        return_args += [expr()]
        return_args += args_list()
    return return_args

def func_decl():
    func_params = []
    return_type = ""
    if token == "function":
        next_token()
        return_type = param_type()
        if token == "id":
            append_func(return_type)
            next_token()
            if token != "(":
                raise_error("(", first_Params)
            next_token()
            func_params = params()
            append_func_params(func_params)
            if token != ")":
                raise_error(")", follow_FuncDecl)
            next_token()
            func_block()
        else:
            raise_error("IDENTIFICADOR", follow_FuncDecl)
    else:
        raise_error("function", follow_FuncDecl)

def proc_decl():
    func_params = []
    if token == "procedure":
        next_token()
        if token == "id":
            append_func()
            next_token()
            if token != "(":
                raise_error("(", first_Params)
            next_token()
            func_params = params()
            append_func_params(func_params)
            if token != ")":
                raise_error(")", first_FuncBlock)
            next_token()
            func_block()
        elif token == "start":
            start()
        else:
            raise_error("IDENTIFICADOR", follow_ProcDecl)
    else:
        raise_error("procedure", follow_ProcDecl)

def param_type():
    param_type_str = ""
    if token in first_Type:
        param_type_str = type_func()
    elif token == "id":
        param_type_str = tokens[tokens_position][2]
        next_token()
    else:
        raise_error(first_ParamType, follow_ParamType)
    return param_type_str

def params():
    func_params = []
    extra_params = []
    if token in first_Param:
        func_params.append(param())
        extra_params = params_list()
        func_params += extra_params
        return func_params

def param():
    dimensions = ""
    func_single_param = ""
    if token in first_ParamType:
        func_single_param = param_type()
        if token == "id":
            next_token()
            dimensions = param_arrays()
            return func_single_param + dimensions
        else:
            raise_error("IDENTIFICADOR", follow_Param)
    else:
        raise_error(first_ParamType, follow_ParamType)

def params_list():
    func_params = []
    extra_params = []
    if token == ",":
        next_token()
        func_params.append(param())
        extra_params = params_list()
        func_params += extra_params
    return func_params

def param_arrays():
    dimensions = 0
    if token == "[":
        next_token()
        if token != "]":
            raise_error("]", first_ParamMultArrays)
        dimensions = 1
        next_token()
        dimensions += param_mult_arrays()
    if dimensions == 0:
        dimensions = ""
    else:
        dimensions = str(dimensions) + "d"
    return dimensions

def param_mult_arrays():
    dimensions = 0
    if token == "[":
        next_token()
        if token == "num":
            next_token()
            if token != "]":
                raise_error("]", first_ParamMultArrays)
            next_token()
            dimensions = 1
            dimensions += param_mult_arrays()
        else:
            raise_error("NÚMERO", follow_ParamMultArrays)
    return dimensions

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
        var_name = get_token_name()
        next_token()
        var_value = stm_id(var_name)
        if not var_name in ide_table:
            raise_semantic_error(f"Variável {var_name} não instanciada")
        elif ide_table[var_name]["class"] == "const":
            raise_semantic_error(f"Variável {var_name} é uma constante.\
                \nNão é possível atribuir valores a uma constante")
        # elif not is_type_correct(ide_table[var_name]["type"], var_value["value"], var_value["general_type"]):
        #     print("Erro: atribuição de variável com tipo errado")
    elif token in first_StmCmd:
        stm_cmd()
    else:
        raise_error(first_VarStm, follow_VarStm)

def stm_id(func_id=None):
    if token in first_Assign:
        token_value = assign()
        return token_value
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
        func_args = []
        next_token()
        func_args = args()
        check_func_params(func_id, func_args)
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

def compare_types(arg1, arg2):
    type_arg1 = get_arg_type(arg1)
    type_arg2 = get_arg_type(arg2)

    if type_arg1 is None:
        return arg2
    if type_arg2 is None:
        return arg1
    if type_arg1 != type_arg2:
        print_arg1 = arg1
        print_arg2 = arg2
        if isinstance(arg1, dict):
            print_arg1 = arg1["value"]
        if isinstance(arg2, dict):
            print_arg2 = arg2["value"]
        raise_semantic_error(f'Valor {print_arg1} [{type_arg1}]\
 não é do mesmo tipo de valor {print_arg2} [{type_arg2}]')
    return arg1

def expr():
    if token in first_Or:
        return or_func()
    else:
        raise_error(first_Expr, follow_Expr)

def or_func():
    if token in first_And:
        lexema1 = and_func()
        lexema2 = or_()
        lexema1 = compare_types(lexema1, lexema2)
        return lexema1
    else:
        raise_error(first_Or, follow_Or)

def or_():
    if token == "||":
        next_token()
        lexema1 = and_func()
        lexema2 = or_()
        lexema1 = compare_types(lexema1, lexema2)
        return lexema1

def and_func():
    if token in first_Equate:
        lexema1 = equate()
        lexema2 = and_()
        lexema1 = compare_types(lexema1, lexema2)
        return lexema1
    else:
        raise_error(first_And, follow_And)

def and_():
    if token == "&&":
        next_token()
        lexema1 = equate()
        lexema2 = and_()
        lexema1 = compare_types(lexema1, lexema2)
        return lexema1

def equate():
    if token in first_Compare:
        lexema1 = compare()
        lexema2 = equate_()
        lexema1 = compare_types(lexema1, lexema2)
        return lexema1
    else:
        raise_error(first_Equate, follow_Equate)

def equate_():
    if token == "==" or token == "!=":
        next_token()
        lexema1 = compare()
        lexema2 = equate_()
        lexema1 = compare_types(lexema1, lexema2)
        return lexema1

def compare():
    if token in first_Add:
        lexema1 = add_func()
        lexema2 = compare_()
        lexema1 = compare_types(lexema1, lexema2)
        return lexema1
    else:
        raise_error(first_Compare, follow_Compare)

def compare_():
    if token == "<" or token == ">" or token == "<=" or token == ">=":
        next_token()
        lexema1 = add_func()
        lexema2 = compare_()
        lexema1 = compare_types(lexema1, lexema2)
        return lexema1

def add_func():
    if token in first_Mult:
        lexema1 = mult()
        lexema2 = add_()
        lexema1 = compare_types(lexema1, lexema2)
        return lexema1
    else:
        raise_error(first_Add, follow_Add)

def add_():
    if token == "+" or token == "-":
        next_token()
        lexema1 = mult()
        lexema2 = add_()
        lexema1 = compare_types(lexema1, lexema2)
        return lexema1

def mult():
    if token in first_Unary:
        lexema1 = unary()
        lexema2 = mult_()
        lexema1 = compare_types(lexema1, lexema2)
        return lexema1
    else:
        raise_error(first_Mult, follow_Mult)

def mult_():
    if token == "*" or token == "/":
        next_token()
        lexema1 = unary()
        lexema2 = mult_()
        lexema1 = compare_types(lexema1, lexema2)
        return lexema1

def unary():
    if token == "!":
        next_token()
        unary()
    elif token in first_Value:
        return value()
    else:
        raise_error(first_Unary, follow_Unary)

def value():
    if token == "num" or token == "str" or token == "true" or token == "false":
        token_value = {"value": tokens[tokens_position][2], "general_type": token}
        next_token()
        return token_value
    elif token == "local" or token == "global":
        next_token()
        access()
    elif token == "id":
        lexema = get_token_name()
        next_token()
        lexema = id_value(lexema)
        return lexema
    elif token == "(":
        next_token()
        lexema1 = expr()
        if token == ")":
            next_token()
            return lexema1
        else:
            raise_error(")", follow_Value)
    else:
        raise_error(first_Value, follow_Value)

def id_value(lexema=None):
    returned_type = lexema
    if token == "(":
        next_token()
        func_params = args()
        returned_type = check_func_params(lexema, func_params)
        if token == ")":
            next_token()
        else:
            raise_error(")", follow_IdValue)
    else:
        arrays()
        accesses()
    return returned_type

def log_expr():
    if token in first_LogOr:
        log_or()
    else:
        raise_error(first_LogExpr, follow_LogExpr)

def log_or():
    if token in first_LogAnd:
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
        lexema = get_token_name()
        next_token()
        lexema = id_value(lexema)
        return lexema
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

semantic_output_dir = 'semantic_output/'

def read_lexical_output(input_dir):
    global tokens, token, tokens_position, errors_count
    tokens = []
    tokens_position = 0
    errors_count = 0
    
    with open(f'{input_dir}{filename}', 'r', encoding='iso8859-1') as fin:
        for line in fin.readlines():
            token_info = line.split() 
            # 0 = line_number
            # 1 = token type
            # 2 = token 
            error_codes = ["SIB", "CMF", "NMF", "CoMF", "OpMF"]
            if token_info[1] in error_codes: # check all 
                continue
            if token_info[1] == "IDE":
                tokens.append((token_info[0], "id", token_info[2]))
            elif token_info[1] == "NRO":
                tokens.append((token_info[0], "num", token_info[2]))
            elif token_info[1] == "CAD":
                tokens.append((token_info[0], "str", token_info[2]))
            else:
                tokens.append((token_info[0], token_info[2], ""))
        token = tokens[tokens_position][1]

for filename in os.listdir(input_dir):
    if filename.startswith('saida'):
        read_lexical_output(input_dir)
    file_num = filename.split('.')[0][5:]
    with open(f'{output_dir}saida{file_num}.txt', 'w') as fout:
        with open(f'{semantic_output_dir}saida{file_num}.txt', 'w') as semantic_output_file:
            program()
    files_read += 1

print(f"Read {files_read} files\
 \nWrote {files_read} files")
