'''
Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em seguida mostre o vetor X.

Entrada
A entrada contém 10 valores inteiros, podendo ser positivos ou negativos.
'''

# declaração de matriz
x = []

# processamento de dados
for i in range(10):
    # entrada de valores
    num = int(input())
    if num < 1:
        num = 1
    x.append(num)

    # saida de dados
    print(f'X[{i}] = {num}')