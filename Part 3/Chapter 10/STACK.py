def STACK_EMPTY(S):
    if s.top ==0:
        return True
    else:
        return False

def PUSH(S,x):
    S.top+=1
    S[S.top]=x

def POP(S):
    if STACK_EMPTY(S):
        raise ValueError("underflow")
    else:
        S.top-=1
        return S[S.top+1]