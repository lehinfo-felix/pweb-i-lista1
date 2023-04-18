# Escreva um programa em Python que leia um número inteiro e imprima a tabuada desse número (de 1 a 10).

response = input("Insira um numero: ")

def getMult(res):
    mult = []
    for i in range(1, 11):
        calcMult = (i*int(res))        
        msg = (str(i)+'x' + res + '=' + str(calcMult))
        mult.append(msg)
    
    return(mult)

print(getMult(response))
