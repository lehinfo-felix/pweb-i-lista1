# Escreva um programa em Python que leia uma lista de números e imprima a média dos números.

nums = []

while True:
    qnt = int(input('Quantos numeros desejas inserir? '))
    if not qnt <= 0:
        break
    print('Valor inválido')

for i in range(1, qnt+1):
    nums.append(int(input('Digite um numero: ')))


def media(nums):
    return sum(nums)/len(nums)


print('A média dos numeros da lista é: ', str(media(nums)))
