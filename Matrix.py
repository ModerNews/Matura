def dot(A: list, B: list):
    C = []
    if not compatibility_check(A, B):
        return None, A
    for i in range(len(A)):
        C.append([])
        temp = []
        for j in range(len(B[1])):
            for k in range(len(A[1])):
                temp.append(A[i][k] * B[k][j])
            C[i].append(sum(temp))
            temp.clear()
    return C

def compatibility_check(A: list, B: list):
    if len(A[1]) != len(B):
        return False
    else:
        return True