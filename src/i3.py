# Escreva um programa em Python que leia um número inteiro e imprima se ele é par ou ímpar.

response = input("Insira um numero: ")

if int(response) % 2 == 0:
    res = 'par'
else:
    res = 'impar'

print('O número ' + response + ' é ' + res)
