def LCS_LENGTH(X,Y):
    m=len(X)
    n=len(Y)
    b=[[0]*n for _ in range(m)]
    c=[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m):
        for j in range(1,n):
            if X[i]==Y[j]:
                c[i,j]=c[i-1,j-1]+1
                b[i,j]=7  # which implies number keyboard
            elif c[i-1,j]>=c[i,j-1]:
                c[i,j]=c[i-1,j]
                b[i,j]=8
            else:
                c[i,j]=c[i,j-1]
                b[i,j]=4
    return [c,b]


def PRINT_LCS(b,X,i,j):
    if i==0 or j==0:
        return
    if b[i,j]==7:
        PRINT_LCS(b,X,i-1,j-1)
        print(X[i])
    elif b[i,j]==8:
        PRINT_LCS(b,X,i-1,j)
    else:
        PRINT_LCS(b,X,i,j-1)