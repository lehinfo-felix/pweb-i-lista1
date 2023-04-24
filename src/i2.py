# Escreva um programa em Python que imprima os números ímpares de 1 a 20.

imp = []
for i in range(1, 21):
    if i % 2 != 0:
        imp.append(i)
print('Os números ímpares contidos entre 1 e 20 são: ' + str(imp))
