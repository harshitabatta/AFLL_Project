  #  Python Dictionary Grammar Rules
# 
import ply.lex as lex
import ply.yacc as yacc

# Define the tokens
tokens = (
    'STRING',
    'NUMBER',
    'COLON',
    'COMMA',
    'LBRACE',
    'RBRACE',
)

# Define the regular expressions for the tokens
t_COLON = r':'
t_COMMA = r','
t_LBRACE = r'{'
t_RBRACE = r'}'

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Define the regular expression for a string
def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

# Define the regular expression for a number
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define the error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Define the grammar rules
def p_dict(p):
    '''dict : LBRACE items RBRACE'''
    p[0] = dict(p[2])

def p_items(p):
    '''items : item
             | item COMMA items'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_item(p):
    '''item : STRING COLON STRING
            | STRING COLON NUMBER'''
    p[0] = (p[1], p[3])

def p_error(p):
    print("Syntax error at '%s'" % p.value)

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Test the parser
input_str = '{ "key1": "value1", "key2": 2 }'


# Give the lexer some input
lexer.input(input_str)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)

result = parser.parse(input_str)
print(result)

'''
(base) ramanyala@CA-WQ127GTWRJ lex % python dictionary_gen.py 
Generating LALR tables
LexToken(LBRACE,'{',1,0)
LexToken(STRING,'key1',1,2)
LexToken(COLON,':',1,8)
LexToken(STRING,'value1',1,10)
LexToken(COMMA,',',1,18)
LexToken(STRING,'key2',1,20)
LexToken(COLON,':',1,26)
LexToken(NUMBER,2,1,28)
LexToken(RBRACE,'}',1,30)
{'key1': 'value1', 'key2': 2}
'''