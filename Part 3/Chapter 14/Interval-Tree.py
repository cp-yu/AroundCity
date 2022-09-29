def INTERVAL_INSERT(T,x):
    pass

def INTERVAL_DELETE(T,x):
    pass

def INTERVAL_SEARCH(T,i):
    x=T.root
    while x!=T.nil and not Overlap(x.int,i):
        if x.left!=T.nil and x.left.max>=i.low:
            x=x.left
        else:
            x=x.right
    return x

def Overlap(int,i):
    if i.high>=int.low or i.low<=int.high:
        return  True

    return False