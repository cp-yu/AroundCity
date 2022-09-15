def LIST_SEARCH(L,k):
    x=L.head
    while x!= None and x.key!=k:
        x=x.next
    return x

def LIST_INSERT(L,x):
    x.next=L.head
    if L.head!=None:
        L.head.prev=x
    L.head = x
    x.prev = None

def LIST_DELETE(L,x):
    if x.prev!=None:
        x.prev.next=x.next
    else:
        L.head=x.next
    if x.next!=None:
        x.next.prev=x.prev

def LIST_DELETE_SENTRY(L,x):
    x.prev.next=x.next
    x.next.prev=x.prev


def LIST_SEARCH_SENTRY(L,k):
    x=L.nil.next
    while x!=L.nil and x.key!=k:
        x=x.next
    return x

def LIST_INSERT_SENTRY(L, x):
    x.next=L.nil.next
    L.nil.next.prev=x
    L.nil.next=x
    x.prev = L.nil
