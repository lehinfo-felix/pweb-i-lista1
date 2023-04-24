# Escreva um programa em Python que leia um número inteiro e imprima a sequência de Fibonacci até esse número.

seq = []
response = int(
    input("Quantos numeros da sequencia de Fibonacci desejas renderizar? "))


def fibo(n):
    if n == 0:
        return []
    else:
        for i in range(1, 2):
            seq.append(1)
        for i in range(len(seq), n):
            seq.append(seq[i-1] + seq[i-2])
        return seq


print(fibo(response))
