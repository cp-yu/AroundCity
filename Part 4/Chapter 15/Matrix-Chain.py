def MATRIX_MULTIPLY(A,B):
    if len(A[0])!=len(B):
        raise ValueError("incompatible dimensions")
    else:
        C=[[0]*len(B[0]) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(A[0])):
                    C[i][j]=C[i][j]+A[i][k]*B[k][j]
    return C



def MATRIX_CHAIN_ORDER(p):
    n=len(p)-1
    m=[[0]*n for _ in range(n)]
    s=[[0]*n for _ in range(n)]
    for l in range(2,n+1):
        for i in range(n-l+2):
            j=i+l-1
            m[i][j]=float("inf")
            for k in range(i,j):
                q=m[i][k]+m[k+1][j]+p[i-2]*p[k-1]*p[j-1]
                if q<m[i][j]:
                    m[i][j]=q
                    s[i][j]=k
    return [m,s]


def PRINT_OPTIMAL_PARENS(s,i,j):
    if i==j:
        print("A"+str(i))
    else:
        print("(")
        PRINT_OPTIMAL_PARENS(s,i,s[i,j])
        PRINT_OPTIMAL_PARENS(s,s[i,j]+1,j)
        print(")")
