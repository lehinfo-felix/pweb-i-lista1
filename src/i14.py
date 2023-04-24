# Escreva um programa em Python que leia uma lista de números e imprima a lista em ordem decrescente.

nums = []

while True:
    qnt = int(input('Quantos numeros desejas inserir? '))
    if not qnt <= 0:
        break
    print('Valor inválido')

for i in range(1, qnt+1):
    nums.append(int(input('Digite um numero: ')))

print('A ordem decrescente é: ', str(sorted(nums, reverse=True)))
