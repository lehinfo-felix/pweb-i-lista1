# Escreva um programa em Python que leia uma lista de números e um número x e imprima se o número x está na lista.

nums = []
while True:
    qnt = int(input('Quantos numeros desejas inserir? '))
    if not qnt <= 0:
        break
    print('Valor inválido')

for i in range(1, qnt+1):
    nums.append(int(input('Digite um numero: ')))

num = int(input('Qual numero desejas buscar? '))

for i in nums:
    if i == num:
        print(f'O numero {num} está na lista, na posicao {nums[i]}')
        break
else:
    print(f'O numero {num} não está na lista')
