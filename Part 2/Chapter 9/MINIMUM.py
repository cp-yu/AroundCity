def MINIMUM(A):
    min=A[0]
    for i in range(1,len(A)):
        if min>A[i]:
            min=A[i]
    return min


if __name__ == "__main__":
    import random

    b = random.randint(1, 100)
    # b = 10
    l, r = random.randint(1, 2), random.randint(1, 1e2)
    if l > r:
        l, r = r, l
    # A = [random.randint(l, r) for x in range(b)]
    A = [random.random() for x in range(b)]

    print(sorted(A))

    B = sorted(A)
    print(MINIMUM(A))
    print(B)