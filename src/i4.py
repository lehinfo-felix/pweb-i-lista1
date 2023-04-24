# Escreva um programa em Python que leia um número inteiro e imprima se ele é positivo ou negativo.

response = input('Insira um número: ')

if int(response) > 0:
    print('O número ' + response + ' é positivo')

elif int(response) < 0:
    print('O número ' + response + ' é negativo')

else:
    print('O número ' + response +
          ' não pode ser considerado positivo nem negativo')
