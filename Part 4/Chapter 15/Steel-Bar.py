def CUT_ROD(p,n):
    if n==0:
        return 0
    q=float("-inf")
    for i in range(n):
        q=max(q,p[i]+CUT_ROD(p,n-i))
    return q


def MEMOIZED_CUT_ROD(p,n):
    r=[float("-inf")]*n
    return MEMOIZED_CUT_ROD_AUX(p,n,r)

def MEMOIZED_CUT_ROD_AUX(p, n,r):
    if r[n-1]>=0:
        return r[n-1]
    if n==0:
        q=0
    else:
        q=float("-inf")
        for i in range(n):
            q=max(q,p[i]+MEMOIZED_CUT_ROD_AUX(p,n-i,r))
    r[n]=q
    return q


def BOTTOM_UP_CUT_ROD(p,n):
    r=[0]*n
    for j in range(n):
        q=float("-inf")
        for i in range(j):
            q=max(q,p[i]+r[j-i])
        r[j]=q
    return r[n]

def EXTENDED_BOTTOM_UP_CUT_ROD(p,n):
    r=[0]*n
    s=[0]*n
    for j in range(n):
        q=float("-inf")
        for i in range(j):
            if q<p[i]+r[j-i]:
                q=p[i]+r[j-i]
                s[j]=i
        r[j]=q
    return [r,s]

def PRINT_CUT_ROD_SOLUTION(p,n):
    tmp=EXTENDED_BOTTOM_UP_CUT_ROD(p,n)
    r,s=tmp[0],tmp[1]
    while n>=0:
        print(s[n])
        n=n-s[n]