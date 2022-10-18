import math
import numpy as np
from fractions import Fraction


def suma(a, b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    # print('Suma => ' + str(real) + ' + ' + str(img) + 'i')
    return real, img


def inverso(a):
    real = -1 * (a[0])
    img = -1 * (a[1])
    return real, img



def resta(a, b):
    real = a[0] - b[0]
    img = a[1] - b[1]
    return real, img



def multiplicacion(a, b):
    real = (a[0] * b[0]) - (a[1] * b[1])
    img = (a[0] * b[1]) + (b[0] * a[1])
    # print('Multiplicación => ' + str(real) + ' + ' + str(img) + 'i')
    return real, img


def division(a, b):
    if modulo2(b) == 0:
        return "Error, division por 0"
    else:
        real = (a[0] * b[0] + a[1] * b[1]) / (b[0] ** 2 + b[1] ** 2)
        img = (a[0] * b[1] + b[0] * a[1]) / (b[0] ** 2 + b[1] ** 2)
        return real, img



def modulo(a):
    modul = math.sqrt(a[0] ** 2 + a[1] ** 2)
    # print('Módulo => ' + str(round(modul, 4)))
    return modul



def modulo2(c):
    modul2 = c[0] ** 2 + c[1] ** 2
    # print('Módulo^2 => ' + str(modul2))
    return modul2



def conjugado(a):
    real = a[0]
    img = -1 * (a[1])
    # print('Conjugado => ' + str(a) + ' + ' + str(-b) + 'i')
    return real, img



def polar(a, b):
    magnitud = math.sqrt((a ** 2) + (b ** 2))
    angulo = math.atan2(b, a)
    return magnitud, angulo



def cartesiano(a, b):
    x = a * math.cos(b)
    y = a * math.sin(b)
    return x, y


def fase(a, b):
    f = math.atan2(b, a)
    return f



def sumavectores(a, b):
    if len(a) == len(b):
        vector = [[0 for i in range(1)] for j in range(len(a))]
        for i in range(len(a)):
            for j in range(1):
                vector[i][j] = suma(a[i][j], b[i][j])
        return vector
    else:
        print("Debido a que los vectores no tienen el mismo tamaño, no es posible realizar la operación")


def restavectores(a, b):
    if len(a) == len(b):
        vector = [[0 for i in range(1)] for j in range(len(a))]
        for i in range(len(a)):
            for j in range(1):
                vector[i][j] = resta(a[i][j], b[i][j])
        return vector
    else:
        print("Debido a que los vectores no tienen el mismo tamaño, no es posible realizar la operación")


def inversovector(a):
    vector = [[0 for i in range(1)] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(1):
            vector[i][j] = inverso(a[i][j])
    return vector


def multescalarvector(c, a):
    vector = [[0 for i in range(1)] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(1):
            vector[i][j] = multiplicacion(c, a[i][j])
    return vector


def sumamatrices(a, b):
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        matriz = [[0 for i in range(len(b[0]))] for j in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                matriz[i][j] = suma(a[i][j], b[i][j])
        return matriz
    else:
        print("Debido a que las matrices no tienen tamaños compatibles, no es posible realizar la operación")



def inversomatriz(a):
    matriz = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            matriz[i][j] = inverso(a[i][j])
    return matriz



def multescalarmatriz(c, a):
    matriz = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            matriz[i][j] = multiplicacion(c, a[i][j])
    return matriz



def traspuesta(a):
    matriz = [[0 for i in range(len(a))] for j in range(len(a[0]))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            matriz[j][i] = a[i][j]
    return matriz



def conjugadomatriz(a):
    matriz = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            matriz[i][j] = conjugado(a[i][j])
    return matriz



def adjuntamatriz(a):
    matriz = conjugadomatriz(a[:])
    return traspuesta(matriz)



def multmatrices(a, b):
    if len(a[0]) == len(b):
        matriz = [[[0, 0] for i in range(len(b[0]))] for j in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    matriz[i][j] = suma(matriz[i][j], multiplicacion(a[i][k], b[k][j]))
        return matriz
    else:
        print("Debido a que las matrices no tienen tamaños compatibles, no es posible realizar la operación")



def productointerno(a, b):
    rta = [0, 0]
    adj = adjuntamatriz(a)
    matriz = multmatrices(adj, b)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j:
                rta = suma(rta, matriz[i][j])
            else:
                rta = rta
    return rta



def normavector(a):
    rt = productointerno(a, a)
    return math.sqrt(rt[0])



def distancia(a, b):
    v = restavectores(a, b)
    rt = normavector(v)
    return rt


def matrizunitaria(a):
    t = adjuntamatriz(a)
    u = multmatrices(t, a)
    ur = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(u)):
        for j in range(len(u[0])):
            ur[i][j] = (round(u[i][j][0]), round(u[i][j][1]))
    I = [[[0, 0] for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i == j:
                I[i][j] = (1, 0)
            else:
                I[i][j] = (0, 0)
    if I == ur:
        # print("La matriz es unitaria")
        return True
    else:
        # print("La matriz no es unitaria")
        return False



def matrizhermitiana(a):
    adj = adjuntamatriz(a)
    if adj == a:
        # print("La matriz es hermitiana")
        return adj
    else:
        # print("La matriz no es hermitiana")
        return adj


def productotensor(a, b):
    matriz = [[0 for i in range(len(b[0] * len(a[0])))] for j in range(len(a) * len(b))]
    # print(matriz)
    for i in range(len(a)):
        for j in range(len(b[0])):
            matriz[i][j] = multescalarmatriz(a[i][j], b)
            # print(a[i][j])
    return matriz


# Función printnumcomplejos: Escribe de una mejor manera el resultado de las operaciones de números complejos
# def printnumcomplejos(c):
# return print(str(round(c[0], 4)) + ' + ' + str(round(c[1], 4)) + 'i')


# Prueba de las diferentes funciones
# print(suma((1, 2), (2, 3)))
# print(inverso((2, 3)))
# resta((1, 2), (2, 3))
# multiplicacion((1, 2), (2, 3))
# division((2, 3), (3, 5))
# modulo(5, 2)
# conjugado(5, 2)
# polar(4, 3)
# cartesiano(8.246211251235321, 1.3258176636680326)
# fase(2, 5)
V1 = [[[1, 2]], [[2, 3]], [[3, 4]], [[4, 5]]]
V2 = [[[2, 4]], [[4, 6]], [[8, 10]], [[12, 14]]]
V3 = [[[1, 2]], [[2, 3]], [[3, 4]]]
V4 = [[[2, 3]], [[4, 1]], [[3, -4]]]
V5 = [[[1, 2]], [[1, 2]], [[1, 2]]]
V6 = [[[1, 2]],
      [[1, 2]],
      [[1, 2]]]
c = (2, -1)
# print(sumavectores(V1, V2))
# print(restavectores(V1, V2))
# print(inversovector(V1))
# print(multescalarvector(c, V2))
x = [
    [[1, 2], [2, 3], [1, 3]],
    [[4, 5], [5, 6], [6, 7]],
    [[2, 1], [5, 5], [4, 2]]
]
y = [
    [[2, 1], [3, 3], [1, 5]],
    [[2, 2], [3, 3], [5, 2]],
    [[1, 5], [2, 6], [7, 2]]
]
z = [
    [(5, 0), (3, 3), (1, 5)],
    [(3, -3), (3, 0), (2, 6)],
    [(1, -5), (2, -6), (3, 0)]
]
u = [
    [[0, 1], [0, 0], [0, 0]],
    [[0, 0], [0, 1], [0, 0]],
    [[0, 0], [0, 0], [0, 1]]
]
#print(sumamatrices(x, y))
# print(inversomatriz(x))
# print(multescalarmatriz(c, y))
# print(traspuesta(x))
# # print(traspuesta(V1))
# print(conjugadomatriz(y))
# print(adjuntamatriz(x))
# print(multmatrices(x, y))
# print(multmatrices(x, V6))
# print(productointerno(V3, V4))
# print(normavector(x))
# print(distancia(V1, V2))
# print(matrizunitaria(u))
# print(matrizhermitiana(z))
m1 = [
    [[1, 2], [2, 1]],
    [[2, 3], [1, 0]]
]
m2 = [
    [[2, 1], [1, 2]],
    [[1, 0], [1, 0]]
]
m3 = [
    [[1, 0], [1, 0]]
]
# print(productotensor(m3, m2))


