'''
Na matemática, um número perfeito é um número inteiro para o qual a soma de todos os seus divisores positivos próprios (excluindo ele mesmo) é igual ao próprio número. Por exemplo o número 6 é perfeito, pois 1+2+3 é igual a 6. Sua tarefa é escrever um programa que imprima se um determinado número é perfeito ou não.

Entrada
A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 20), indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor inteiro X (1 ≤ X ≤ 108), que pode ser ou não, um número perfeito.
'''

# entrada de dados
teste = int(input())

# declaração de valores
numTeste = 0

# processamento de dados
while numTeste < teste:
    # declaração de valor da soma inicial
    soma = 0
    
    # entrada de numero 
    num = int(input())

    for i in range(1, num):
        if (num % i == 0):
            soma += i
    
    # saida de dados
    if num == soma:
        print(f'{num} eh perfeito')
    else:
        print(f'{num} nao eh perfeito')
    
    numTeste += 1