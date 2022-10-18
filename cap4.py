import operaciones as lb
import math
#ejercicios cap 4

# n: número de posiciones, v: vector, p: posición p
def probposicion(v, p):
    # nv: norma del vector
    nv = lb.normavector(v)
    rt = (lb.modulo2(v[p][0])) / (nv ** 2)
    rt = rt * 100
    return rt


# a: vector 1, b: vector 2
def probvector(a, b):
    na = [1 / lb.normavector(a), 0]
    nb = [1 / lb.normavector(b), 0]
    # A y B son los vectores a y b normalizados
    A = lb.multescalarvector(na, a)
    B = lb.multescalarvector(nb, b)
    rt = lb.productointerno(B, A)
    return rt


def amplitudtransicion(a, b):
    return probvector(a, b)


def identidad(n):
    I = [[[0, 0] for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                I[i][j] = (1, 0)
            else:
                I[i][j] = (0, 0)
    return I


# o: observable, v: vector
def valoresperado(o, v):
    if len(o) == len(o[0]) and len(o[0]) == len(v):
        h = lb.matrizhermitiana(o)
        if h:
            ov = lb.multmatrices(o, v)
            val = lb.productointerno(ov, v)
            return val


# o: observable, v: vector
def operadordelta(o, v):
    val = valoresperado(o, v)
    I = identidad(len(o))
    mult = lb.multescalarmatriz(val, I)
    oI = lb.multescalarmatriz([-1, 0], mult)
    delta = lb.sumamatrices(o, oI)
    return delta


# o: observable, v: vector
def varianza(o, v):
    delta = operadordelta(o, v)
    d2 = lb.multmatrices(delta, delta)
    val = valoresperado(d2, v)
    return val


# Para esta funcion, se tomará un sistema con 2 matrices unitarias, n,m y el vector de estado inicial v.
def dinamica(n, m, v):
    h = lb.matrizunitaria(n)
    i = lb.matrizunitaria(m)
    print(h, i)
    # j = lb.matrizunitaria(l)
    if h and i:
        v1 = lb.multmatrices(n, v)
        v2 = lb.multmatrices(m, v1)
        # v3 = lb.multmatrices(l, v2)
        return v2  # v2 es el estado final


v = [
    [[2, 1]],
    [[-1, 2]],
    [[0, 1]],
    [[1, 0]],
    [[3, -1]],
    [[2, 0]],
    [[0, -2]],
    [[-2, 1]],
    [[1, -3]],
    [[0, -1]]
]
# p = 7
# print(probposicion(v, p))
# for i in range(10):
#     print(i, " ", probposicion(v, i))
V = [
    [[-1, -4]],
    [[2, -3]],
    [[-7, 6]],
    [[-1, 1]],
    [[-5, -3]],
    [[5, 0]],
    [[5, 8]],
    [[4, -4]],
    [[8, -7]],
    [[2, -7]]
]
x0 = [
    [[1, 0]],
    [[0, 0]],
    [[0, 0]],
    [[0, 0]],
    [[0, 0]],
    [[0, 0]],
    [[0, 0]],
    [[0, 0]],
    [[0, 0]],
    [[0, 0]],
]
x1 = [
    [[0, 0]],
    [[1, 0]],
    [[0, 0]],
    [[0, 0]],
    [[0, 0]],
    [[0, 0]],
    [[0, 0]],
    [[0, 0]],
    [[0, 0]],
    [[0, 0]],
]
# for i in range(10):
#     print(i, " ", probposicion(v, i))
# print(probvector(v, V))
# print(probvector(x0, x1))

m2 = [
    [(3, 0), (1, 2)],
    [(1, -2), (-1, 0)]
]
v2 = [
    [[math.sqrt(2) / 2, 0]],
    [[-math.sqrt(2) / 2, 0]]
]
# print(valoresperado(m, v2))
# print(operadordelta(m, v2))
# print(varianza(m, v2))

m3 = [
    [(0, 0), (1, 0)],
    [(1, 0), (0, 0)]
]
m4 = [
    [(math.sqrt(2) / 2, 0), (math.sqrt(2) / 2, 0)],
    [(math.sqrt(2) / 2, 0), (-(math.sqrt(2) / 2), 0)]
]
v3 = [
    [[1, 0]],
    [[0, 0]]
]
print(dinamica(m3, m4, v3))
print(lb.matrizunitaria(m4))


