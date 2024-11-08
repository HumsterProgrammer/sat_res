import io

# <S> ::= <conj> <disj_tail>
# <disj_tail> ::= ∨ <conj> <disj_tail> | ε
# <conj> ::= <expr> <conj_tail>
# <conj_tail> ::= ∧ <expr> <conj_tail> | ε
# <expr> ::= <var> | ( <S> ) | ¬ <expr>
# <var> ::= x <var_tail>
# <var_tail> ::= 0 <var_tail> | 1 <var_tail> | ε

def parseSAT(charstream): # io.StringIO("example")
    parseConj(charstream)
    parseDisjTail(charstream)
    
def parseDisjTail(charstream):
    if charstream.read(1) == "∨":
    
def parseConj(charstream):
    parseExpr(charstream)
    
def parseConjTail(charstream):
    if charstream.read(1) == "∧":
    
def parseExpr(charstream):
    
def parseVar(charstream):
    parseChar(charstream.read(), "x")
    parseVarTail(charstream, 0)

def parseVarTail(charstream, num):
    c = charstream.read(1)
    if c == "0":
        return parseVarTail(charstream, 2*num)
    elif c == "1":
        return parseVarTail(charstream, 2*num+1)
    else:
        return num
    
def parseChar(char, sample):
    if char != sample:
        raise Exception()