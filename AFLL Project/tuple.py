 #  Python Tuple Grammar Rules
# 
import ply.lex as lex
import ply.yacc as yacc

# Define the tokens
tokens = (
    'NUMBER',
    'STRING',
    'COMMA',
    'LPAREN',
    'RPAREN',
)

# Define the regular expressions for the tokens
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Define a regular expression for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a regular expression for strings
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

# Define error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Define the grammar rules
def p_tuple(p):
    'tuple : LPAREN elements RPAREN'
    p[0] = tuple(p[2])

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

# Define error handling rule
def p_error(p):
    print("Syntax error in input!")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Test the parser with some input
input_str = '(1, "hello", 2, "world")'

# Give the lexer some input
lexer.input(input_str)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)

# Test the parser
result = parser.parse(input_str)
print(result)

'''
(base) ramanyala@CA-WQ127GTWRJ lex % python tuple_gen.py
LexToken(LPAREN,'(',1,0)
LexToken(NUMBER,1,1,1)
LexToken(COMMA,',',1,2)
LexToken(STRING,'hello',1,4)
LexToken(COMMA,',',1,11)
LexToken(NUMBER,2,1,13)
LexToken(COMMA,',',1,14)
LexToken(STRING,'world',1,16)
LexToken(RPAREN,')',1,23)
(1, 'hello', 2, 'world')
'''
