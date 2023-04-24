# Escreva um programa em Python que leia um número inteiro e imprima a tabuada desse número (de 1 a 10).

response = input("Insira um numero: ")


def getSum(res):
    res = int(res)
    aux = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = []
    for i in range(0, 9):
        calc = int(aux[int(i)]) + int(res)
        line = str(aux[i]) + '+' + str(res) + '=' + str(calc)
        result.append(line)
    return result


def getMult(res):
    res = int(res)
    aux = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = []
    for i in range(0, 9):
        calc = int(aux[int(i)]) * int(res)
        line = str(aux[i]) + 'x' + str(res) + '=' + str(calc)
        result.append(line)
    return result


def getSub(res):
    res = int(res)
    aux = [int(res+1), int(res+2), int(res+3), int(res+4),
           int(res+5), int(res+6), int(res+7), int(res+8), int(res+9)]
    result = []
    for i in range(0, 9):
        calc = int(aux[int(i)]) - int(res)
        line = str(aux[i]) + '-' + str(res) + '=' + str(calc)
        result.append(line)
    return result


def getDiv(res):
    res = int(res)
    aux = [int(res*1), int(res*2), int(res*3), int(res*4),
           int(res*5), int(res*6), int(res*7), int(res*8), int(res*9)]
    result = []
    for i in range(0, 9):
        calc = int(aux[int(i)]) / int(res)
        line = str(aux[i]) + '/' + str(res) + '=' + str(calc)
        result.append(line)
    return result


def printResult(res):

    print('Soma:')
    for i in range(0, 9):
        print(getSum(res)[i])
    print()

    print('Multiplicação:')
    for i in range(0, 9):
        print(getMult(res)[i])
    print()

    print('Subtração:')
    for i in range(0, 9):
        print(getSub(res)[i])
    print()

    print('Divisão:')
    for i in range(0, 9):
        print(getDiv(res)[i])
    print()


printResult(response)
