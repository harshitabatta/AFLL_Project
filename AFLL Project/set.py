#  Python Set Grammar Rules
# 
import ply.lex as lex
import ply.yacc as yacc

# Define the lexer tokens
tokens = (
    'NUMBER',
    'STRING',
    'COMMA',
    'LBRACE',
    'RBRACE',
)

# Define the regular expressions for the lexer tokens
t_COMMA = r','
t_LBRACE = r'{'
t_RBRACE = r'}'

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\''
    t.value = t.value[1:-1]
    return t

# Define the error handling for the lexer
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Define the grammar rules for the parser
def p_set(p):
    '''set : LBRACE elements RBRACE'''
    p[0] = set(p[2])

def p_elements(p):
    '''elements : element
                | element COMMA elements'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_element(p):
    '''element : NUMBER
               | STRING'''
    p[0] = p[1]

# Define the error handling for the parser
def p_error(p):
    print("Syntax error at '%s'" % p.value)

# Build the parser
parser = yacc.yacc()

# Test the parser with some input
input_str = '{1, "two", 3, \'four\'}'


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
(base) ramanyala@CA-WQ127GTWRJ lex % python set3_gen.py
LexToken(LBRACE,'{',1,0)
LexToken(NUMBER,1,1,1)
LexToken(COMMA,',',1,2)
LexToken(STRING,'two',1,4)
LexToken(COMMA,',',1,9)
LexToken(NUMBER,3,1,11)
LexToken(COMMA,',',1,12)
LexToken(STRING,'four',1,14)
LexToken(RBRACE,'}',1,20)
{1, 3, 'four', 'two'}
'''