'''
Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.

Entrada
A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.
'''

# -*- coding: utf-8 -*-

# Leia o número de casos de teste
N = int(input())

# Processar cada caso de teste
for _ in range(N):
    X = int(input())
    
    # Verificar se X é primo
    if X <= 1:
        print(f"{X} nao eh primo")
        continue
    
    if X == 2:
        print(f"{X} eh primo")
        continue
    
    if X % 2 == 0:
        print(f"{X} nao eh primo")
        continue
    
    primo = True
    for i in range(3, int(X**0.5) + 1, 2):
        if X % i == 0:
            primo = False
            break
    
    if primo:
        print(f"{X} eh primo")
    else:
        print(f"{X} nao eh primo")
