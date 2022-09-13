def SQUARE_MATRIX_MULTIPLY(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C


def SQUARE_MATRIX_MULTIPLY_RECURSIVE(A, B):
    try:
        n = len(A)
    except:
        n=1
    if n==1:
        C=[[0]]
        C[0][0]=A[0][0]*B[0][0]
    # C = [[0] * n for _ in range(n)]

    else:
        C11=MATRIX_ADD(SQUARE_MATRIX_MULTIPLY_RECURSIVE(MATRIX_EXACT(A,0,n//2,0,n // 2),MATRIX_EXACT(B,0,n//2,0,n // 2)),SQUARE_MATRIX_MULTIPLY_RECURSIVE(MATRIX_EXACT(A,0,n//2,n // 2,n),MATRIX_EXACT(B,n//2,n,0,n // 2)))
        C12=MATRIX_ADD(SQUARE_MATRIX_MULTIPLY_RECURSIVE(MATRIX_EXACT(A,0,n//2,0,n // 2),MATRIX_EXACT(B,0,n//2,n // 2,n)),SQUARE_MATRIX_MULTIPLY_RECURSIVE(MATRIX_EXACT(A,0,n//2,n // 2,n),MATRIX_EXACT(B,n//2,n,n // 2,n)))
        C21=MATRIX_ADD(SQUARE_MATRIX_MULTIPLY_RECURSIVE(MATRIX_EXACT(A,n//2,n,0,n//2),MATRIX_EXACT(B,0,n//2,0,n // 2)),SQUARE_MATRIX_MULTIPLY_RECURSIVE(MATRIX_EXACT(A,n//2,n,n // 2,n),MATRIX_EXACT(B,n//2,n,0,n // 2)))
        C22=MATRIX_ADD(SQUARE_MATRIX_MULTIPLY_RECURSIVE(MATRIX_EXACT(A,n//2,n,0,n//2),MATRIX_EXACT(B,0,n//2,n//2,n)),SQUARE_MATRIX_MULTIPLY_RECURSIVE(MATRIX_EXACT(A,n//2,n,n // 2,n),MATRIX_EXACT(B,n//2,n,n // 2,n)))
        C=[C11+C12,C21+C22]
    return C

def MATRIX_EXACT(A,row_up,row_down,col_left,col_right):
    C=A[row_up:row_down]
    for i in range(0,row_down-row_up):
        C[i]=C[i][col_left:col_right]
    return C

def MATRIX_ADD(A,B):
    try:
        C=[[0]*len(A[0]) for _ in range(len(A))]
    except:
        return A+B
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j]=A[i][j]+B[i][j]
    return  C

# C = SQUARE_MATRIX_MULTIPLY_RECURSIVE([[2, 2,3,7], [1, 2,3,7], [1, 2,3,4], [1, 2,3,4]], [[1, 2,3,7], [1, 2,3,1], [1, 2,3,4], [1, 2,3,4]])
C = SQUARE_MATRIX_MULTIPLY_RECURSIVE([[1,2],[1,2]],[[1,2],[1,2]])

print(C)

print(SQUARE_MATRIX_MULTIPLY([[2, 2,3,7], [1, 2,3,7], [1, 2,3,4], [1, 2,3,4]], [[1, 2,3,7], [1, 2,3,1], [1, 2,3,4], [1, 2,3,4]]))