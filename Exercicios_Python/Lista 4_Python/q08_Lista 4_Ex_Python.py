#08. Criar um algoritmo que calcule a soma dos números pares entre 25 e 200.

def Soma():
    soma = 0
    for i in range(25, 200):
        if i % 2 == 0:
            soma = soma + i

    print(soma, end = ' ')


Soma()
