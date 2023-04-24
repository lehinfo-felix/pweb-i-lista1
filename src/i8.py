# Escreva um programa em Python que leia uma lista de números e imprima o maior e o menor número da lista.

nums = []

while True:
    qnt = int(input('Quantos numeros desejas inserir? '))
    if not qnt <= 0:
        break
    print('Valor inválido')

for i in range(1, qnt+1):
    nums.append(int(input('Digite um numero: ')))


def maior_menor(nums):
    maior = max(nums)
    menor = min(nums)
    return [maior, menor]


print('O maior numero da lista é: ', str(maior_menor(nums)[0])+'\n'
      + 'O menor numero da lista é: ', str(maior_menor(nums)[1]))
