def OS_SELECT(x,i):
    r=x.left.size+1
    if i==r:
        return x
    elif i<r:
        return OS_SELECT(x.left,i)
    else:
        return OS_SELECT(x.right, i-r)

def OS_RANK(T,x):
    r=x.left.size + 1
    y=x
    while y!=T.root:
        if y== y.p.right:
            r=r+y.p.left.size+1
        y=y.p
    return r


def LEFT_ROTATE(T,x):
    y=x.right
    x.right=y.left
    if y.left!=T.nil:
        y.left.p=x
    y.p=x.p
    if x.p==T.nil:
        T.root=y
    elif x==x.p.left:
        x.p.left=y
    else:
        x.p.right=y
    y.left=x
    x.p=y
    y.size=x.size
    x.size=x.left.size+x.right.size+1


def RIGHT_ROTATE(T,x):
    y=x.left
    x.left=y.right
    if y.right!=T.nil:
        y.right.p=x
    y.p=x.p
    if x.p==T.nil:
        T.root=y
    elif x==x.p.right:
        x.p.right=y
    else:
        x.p.left=y
    y.right=x
    x.p=y
    y.size = x.size
    x.size = x.left.size + x.right.size + 1