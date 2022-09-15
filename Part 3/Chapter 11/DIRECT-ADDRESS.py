def DIRECT_ADDRESS_SEARCH(T,k):
    return T[k]

def DIRECT_ADDRESS_INSERT(T,x):
    T[x.key]=x

def DIRECT_ADDRESS_DELETE(T,x):
    T[x.key]=None