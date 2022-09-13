def COUNTING_SORT(A,k):
    C=[0]*(k+1)
    B=[0]*len(A)
    for j in range(len(A)):
        C[A[j]]=C[A[j]]+1
    for i in range(k+1):
        C[i]=C[i]+C[i-1]
    # for j in range(len(A)-1,-1,-1):
    #     B[C[A[j]]-1]=A[j]
    #     C[A[j]]=C[A[j]]-1
    for j in range(len(A)):
        B[C[A[j]]-1]=A[j]
        C[A[j]]=C[A[j]]-1
    return B

import random
b = random.randint(1, 100)
# b = 10
l, r = random.randint(1, 2), random.randint(1, 1e2)
if l > r:
    l, r = r, l
A = [random.randint(l, r) for x in range(b)]

print(sorted(A))
B=[0]*(b)
print(COUNTING_SORT(A,101))