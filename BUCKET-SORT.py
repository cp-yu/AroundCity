def BUCKET_SORT(A):
    n=len(A)
    B=[[] for _ in range(n)]

    for i in range(n):
        B[int(n*A[i])].append(A[i])
    for i in range(n):
        if B[i]:
            B[i].sort()
    C=[]
    for b in B:
        if b:
            C=C+b
    return C

import random
b = random.randint(1, 100)
# b = 10
l, r = random.randint(1, 2), random.randint(1, 1e2)
if l > r:
    l, r = r, l
# A = [random.randint(l, r) for x in range(b)]
A = [random.random() for x in range(b)]

print(sorted(A))

B=sorted(A)
print(BUCKET_SORT(A))
print(A)