#  Python List Declaration Grammar rules
# 
import ply.lex as lex
import ply.yacc as yacc

# Define the list of token names
tokens = (
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'INTEGER',
    'FLOAT',
    'STRING'
)

# Define the regular expressions for each token
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
# t_INTEGER = r'\d+'    
# t_FLOAT = r'\d+\.\d+'
t_STRING = r'\".*?\"'   

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'



def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)    
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define the error handling function
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Define the parser rules
def p_list(p):
    '''list : LBRACKET values RBRACKET'''
    p[0] = list(p[2])

def p_values(p):
    '''values : value
              | value COMMA values'''
    print(p[1])
    if len(p) == 2:                       
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_value(p):
    '''value : INTEGER
             | FLOAT
             | STRING'''
    p[0] = p[1]

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()


# Define the error handling for the parser
def p_error(p):
    print("Syntax error at '%s'" % p.value)

# Test the parser with some input
input_str = '[1, 2.0, "three"]'

# input_str = '[1]'

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
(base) ramanyala@CA-WQ127GTWRJ lex % python array_gen.py
LexToken(LBRACKET,'[',1,0)        
LexToken(INTEGER,'1',1,1)
LexToken(COMMA,',',1,2)
LexToken(FLOAT,'2.0',1,4)
LexToken(COMMA,',',1,7)
LexToken(STRING,'"three"',1,9)
LexToken(RBRACKET,']',1,16)
['1', '2.0', '"three"']

'''
