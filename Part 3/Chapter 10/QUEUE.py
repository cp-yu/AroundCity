def ENQUEUE(Q,x):
    Q[Q.tail]=x
    if Q.tail==len(Q):
        Q.tail=0
    else:
        Q.tail+=1

def DEQUEUE(Q):
    x=Q[Q.head]
    if Q.head==len(Q):
        Q.head=1
    else:
        Q.head+=1
    return x