def ALLOCATE_OBJECT():
    if free==None:
        raise ValueError("out of space")
    else:
        x=free
        free=x.next
        return x

def FREE_OBJECT(x):
    x.next=free
    free=x