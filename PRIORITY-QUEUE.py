def HEAP_MAXIMUM(A):
    return A[0]


def MAX_HEAPIFY_LOOP(A, i, heapsize):
    while True:
        l = LFET(i)
        r = RIGHT(i)
        if l < heapsize and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r < heapsize and A[r] > A[largest]:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            i = largest
        else:
            break


def HEAP_EXTRACT_MAX(A, heapsize):
    assert heapsize >= 1
    max = A[0]
    A[0] = A[heapsize - 1]
    heapsize = heapsize - 1
    MAX_HEAPIFY_LOOP(A, 0, heapsize)
    return max


def PARENT(i):
    return (i - 1) // 2

def LFET(i):
    return 2 * i + 1


def RIGHT(i):
    return 2 * i + 2


def HEAP_INCREASE_KEY(A, i, key):
    assert key >= A[i]
    A[i] = key
    while i > 0 and A[PARENT(i)] < A[i]:
        A[i], A[PARENT(i)] = A[PARENT(i)], A[i]
        i = PARENT(i)


def MAX_HEAP_INSERT(A, key, heapsize):
    heapsize = heapsize + 1
    A[heapsize] = float("-inf")
    HEAP_INCREASE_KEY(A, heapsize, key)
    return heapsize
