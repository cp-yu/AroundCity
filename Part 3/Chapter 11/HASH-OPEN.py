def HASH_INSERT(T,k):
    for i in range(len(T)):
        j=h(k,i)
        if T[j]==None:
            T[j]=k
            return j
    raise ValueError("hash table overflow")

def HASH_SEARCH(T,k):
    for i in range(len(T)):
        j=h(k,i)
        if not T[j] :
            return None
        elif T[j] ==k:
            return j
    return  None


def h(k,i):
    pass