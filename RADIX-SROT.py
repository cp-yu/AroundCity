def RADIX_SORT(A,d):
    for i in range(1,d+1):
        A.sort(key=lambda x:int('{0:0>10}'.format(x)[d-i]))
    return A

import random
b = random.randint(1, 100)
# b = 10
l, r = random.randint(1, 2), random.randint(1, 1e2)
if l > r:
    l, r = r, l
A = [random.randint(l, r) for x in range(b)]

print(sorted(A))

B=sorted(A)
print(RADIX_SORT(A,3))
print(A)