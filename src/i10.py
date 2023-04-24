# Escreva um programa em Python que leia uma lista de números e imprima apenas os números pares da lista.

nums = []

while True:
    qnt = int(input('Quantos numeros desejas inserir? '))
    if not qnt <= 0:
        break
    print('Valor inválido')

for i in range(1, qnt+1):
    nums.append(int(input('Digite um numero: ')))


def pares(nums):
    return [num for num in nums if num % 2 == 0]


print('Os numeros pares da lista são: ', str(pares(nums)))
