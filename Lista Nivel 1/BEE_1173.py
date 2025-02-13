'''
Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10]. Em cada posição subsequente, coloque o dobro do valor da posição anterior. Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente. Mostre o vetor em seguida.

Entrada
A entrada contém um valor inteiro (V<=50).

Saída
'''

# declaração de matriz
n =[]

# entrada do numero
num = int(input())

# processamento de dados
for i in range(10):
    print(f'N[{i}] = {num}')
    num *= 2