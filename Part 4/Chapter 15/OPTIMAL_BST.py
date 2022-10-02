def OPTIMAL_BST(p,q,n):
    e=[[0]*n for _ in range(n+1)]
    root=[[0]*n for _ in range(n)]
    w=[[0]*n for _ in range(n+1)]
    for i in range(n+1):
        e[i,i-1]=q[i-1]
        w[i,i-1]=q[i-1]
    for l in range(n):
        for i in range(n-l+1):
            j=i+l-1
            e[i,j]=float("inf")
            w[i,j]=w[i,j-1]+p[j]+q[j]
            for r in range(i,j):
                t=e[i,r-1]+e[r+1,j]+w[i,j]
                if t<e[i,j]:
                    t=e[i,r-1]+e[r+1,j]+w[i,j]
                    if t<e[i,j]:
                        e[i,j]=t
                        root[i,j]=r
    return [e,root]