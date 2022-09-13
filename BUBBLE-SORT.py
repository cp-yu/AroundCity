import random
b=random.randint(1,100)
l,r=random.randint(1,1e1),random.randint(1,1e3)
if l>r:
    l,r=r,l
A=[random.randint(l,r) for x in range(b)]

def BUBBLE_SORT(A):
    for i in range(len(A)-2):
        for j in range(len(A)-1,i,-1):
            if A[j]<A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]
    return A



# A=[23,153,135,1,5165,44,654,163]
A=BUBBLE_SORT(A)
print(A)