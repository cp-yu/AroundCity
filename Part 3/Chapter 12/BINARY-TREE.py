def INORDER_TREE_WALK(x):
    if x!=None:
        INORDER_TREE_WALK(x.left)
        print(x.key,end=",")
        INORDER_TREE_WALK(x.right)

def TREE_SEARCH(x,k):
    if x==None or k==x.key:
        return x
    if k<x.key:
        return TREE_SEARCH(x.left,k)
    return TREE_SEARCH(x.right, k)

def ITERATIVE_SEARCH(x,k):
    while x!=None and K!=x.key:
        if k<x.key:
            x=x.left
        else:
            x=x.right
    return x

def TREE_MINIMUM(x):
    while x.left!=None:
        x=x.left
    return x

def TREE_MAXIMUM(x):
    while x.right != None:
        x=x.right
    return  x

def TREE_SUCCESSOR(x):
    if x.right != None:
        return TREE_MINIMUM(x.right)
    y= x.p
    while y!=None and x== y.right:
        x=y
        y=y.p
    return y


def TREE_INSEART(T,z):
    y=None
    x=T.root
    while x!=None:
        y=x
        if z.key<x.key:
            x=x.left
        else:
            x=x.right
    z.p=y
    if y==None:
        T.root=z
    elif z.key < y.key:
        y.left=z
    else:
        y.right=z

def TRANSLANT(T,u,v):
    if u.p==None:
        T.root=v
    elif u==u.p.left:
        u.p.left=v
    else:
        u.p.right=v
    if v!=None:
        v.p=u.p

def TREE_DELETE(T,z):
    if z.left==None:
        TRANSLANT(T,z,z.right)
    elif z.right==None:
        TRANSLANT(T,z,z.left)
    else:
        y=TREE_MINIMUM(z.right)
        if y.p!=z:
            TRANSLANT(T,y,y.right)
            y.right=z.right
            y.right.p=y
        TRANSLANT(T,z,y)
        y.left = z.left
        y.left.p=y
