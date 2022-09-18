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

def RB_INSERT(T,z):
    y=T.nil
    x=T.root
    while x!= T.nil:
        y=x
        if z.key<x.key:
            x=x.left
        else:
            x=x.right
    z.p=y
    if y==T.nil:
        T.root=z
    elif z.key<y.key:
        y.left=z
    else:
        y.right=z
    z.left = T.nil
    z.right = T.nil
    z.color="RED"
    RB_INSERT_FIXUP(T,z)

def RB_INSERT_FIXUP(T,z):
    if z.p==z.p.p.left:
        y=z.p.p.right
        if y.color=="RED":
            z.p.color="BLACK"
            y.color = "BLACK"
            z.p.p.color = "RED"
            z=z.p.p
        elif z==z.p.right:
            z=z.p
            LEFT_ROTATE(T,z)
        z.p.color="BLACK"
        z.p.p.color = "RED"
        RIGHT_ROTATE(T,z.p.p)
    else:
        y = z.p.p.left
        if y.color == "RED":
            z.p.color = "BLACK"
            y.color = "BLACK"
            z.p.p.color = "RED"
            z = z.p.p
        elif z == z.p.left:
            z = z.p
            RIGHT_ROTATE(T, z)
        z.p.color = "BLACK"
        z.p.p.color = "RED"
        LEFT_ROTATE(T, z.p.p)
    T.root.color="BLACK"

def RB_TRANSPLANT(T,u,v):
    if u.p==T.nil:
        T.root=v
    elif u==u.p.left:
        u.p.left=v
    else:
        u.p.right=v
    v.p=u.p

def TREE_MINIMUM(x):
    while x.left!=None:
        x=x.left
    return x

def RB_DELETE(T,z):
    y=z
    y_origin_color=y.color
    if z.left==T.nil:
        x=z.right
        RB_TRANSPLANT(T,z,z.right)
    elif z.right ==T.nil:
        x=z.left
        RB_TRANSPLANT(T,z,z.left)
    else:
        y=TREE_MINIMUM(z.right)
        y_origin_color=y.color
        x=y.right
        if y.p==z:
            x.p=y
        else:
            RB_TRANSPLANT(T,y,y.right)
            y.right = z.right
            y.right.p=y
        RB_TRANSPLANT(T,z,y)
        y.left=z.left
        y.left.p=y
        y.color=z.color
    if y_origin_color=="BLACK":
        RB_DELETE_FIXUP(T,x)

def RB_DELETE_FIXUP(T,x):
    while x!=T.root and x.color=="BLACK":
        if x==x.p.left:
            w=x.p.right
            if w.color=="RED":
                w.color="BLACK"
                x.p.color="RED"
                LEFT_ROTATE(T,x.p)
                w=x.p.right
            if w.left.color=="BLACK" and w.right.color == "BLACK":
                w.color="RED"
                x=x.p
            elif w.right.color == "BLACK":
                w.left.color="BLACK"
                w.color="RED"
                RIGHT_ROTATE(T,w)
                w=x.p.right
            w.color=x.p.color
            x.p.color="BLACK"
            w.right.color="BLACK"
            LEFT_ROTATE(T,x.p)
            x=T.root
        else:
            if x == x.p.right:
                w = x.p.left
                if w.color == "RED":
                    w.color = "BLACK"
                    x.p.color = "RED"
                    RIGHT_ROTATE(T, x.p)
                    w = x.p.left
                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"
                    x = x.p
                elif w.left.color == "BLACK":
                    w.right.color = "BLACK"
                    w.color = "RED"
                    LEFT_ROTATE(T, w)
                    w = x.p.left
                w.color = x.p.color
                x.p.color = "BLACK"
                w.left.color = "BLACK"
                RIGHT_ROTATE(T, x.p)
                x = T.root
    x.color="BLACK"

