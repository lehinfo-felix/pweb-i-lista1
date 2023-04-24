# Escreva um programa em Python que leia dois números inteiros e imprima o maior deles.

numberOne = str(input('Insira um número: '))
numberTwo = str(input('Insira outro número: '))

if (numberOne == numberTwo):
    print('Os números são iguais!')
else:
    res = numberOne if numberOne > numberTwo else numberTwo
    print('O maior número é ' + res)
