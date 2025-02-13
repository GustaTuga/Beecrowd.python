'''
Faça um programa que leia um vetor A[100]. No final, mostre todas as posições do vetor que armazenam um valor menor ou igual a 10 e o valor armazenado em cada uma das posições.

Entrada
A entrada contém 100 valores, podendo ser inteiros, reais, positivos ou negativos.
'''

A = [float(input()) for _ in range(100)]  # Lê 100 valores e armazena no vetor

for i in range(100):
    if A[i] <= 10:  # Verifica se o valor é menor ou igual a 10
        print(f"A[{i}] = {A[i]:.1f}")  # Exibe a posição e o valor formatado com uma casa decimal
