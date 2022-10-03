def RECURSIVE_ACTIVITY_SELECTOR(s,f,k,n):
    m=k+1
    while m<=n and s[m]<f[k]:
        m=m+1
    if m<=n:
        tmp=RECURSIVE_ACTIVITY_SELECTOR(s,f,m,n)
        if tmp:
            tmp.append(m)
            return tmp
        else:
            return [m]
    else:
        return None

    
def GREEDY_ACTIVITY_SELECTOR(s,f):
    n=s.length
    A=[1]
    k=1
    for m in range(1,n):
        if s[m]>=f[k]:
            A.append(m)
            k=m
    return A