# Escreva um programa em Python que leia uma lista de números e imprima a lista em ordem crescente.

nums = []

while True:
    qnt = int(input('Quantos numeros desejas inserir? '))
    if not qnt <= 0:
        break
    print('Valor inválido')

for i in range(1, qnt+1):
    nums.append(int(input('Digite um numero: ')))

print('A ordem crescente é: ', str(sorted(nums)))
