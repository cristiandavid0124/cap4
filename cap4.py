from MATRIX-VECTOR-LIBRARY import *

# PROGRAMMING CHALLENGES

def probability(pos, v):
    a = normVector(v[pos])
    b = normVector(v)
    probability = (a / b)
    return probability * 100


def ProbabilityofPassing(v, v1):
    aux = [(0, 0)] * len(v)
    for i in range(len(v)):
        aux[j] = conjugate(v1[i])
    answer = (0, 0)
    for j in range(len(v)):
        answer = sumcplx(answer, multicplx(v[j], aux[j]))
    return answer


def VectorProduct(v, v1):
    answer = 0
    for i in range(len(v)):
        answer += v[i] * v1[i]
    return answer


# Exercise # 4.4.1
def UnitaryVerify(u1, u):
    if unitMatrix(m)(U1) and unitMatrix(m)(u):
        answer = matrixProduct(u1, u)
        return unitMatrix(answer)


# Exercise # 4.4.2
def Experiment(v, n, clicks):
    for i in range(clicks):
        v = multiScalarMatrixCplx(v, n)
    return v