# Escreva um programa em Python que leia uma lista de números e imprima apenas os números ímpares da lista.

nums = []

while True:
    qnt = int(input('Quantos numeros desejas inserir? '))
    if not qnt <= 0:
        break
    print('Valor inválido')

for i in range(1, qnt+1):
    nums.append(int(input('Digite um numero: ')))


def impares(nums):
    return [num for num in nums if not num % 2 == 0]


print('Os numeros impares da lista são: ', str(impares(nums)))
