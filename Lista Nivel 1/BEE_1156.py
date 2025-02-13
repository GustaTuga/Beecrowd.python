'''
Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?

Entrada
Não há nenhuma entrada neste problema.

Saída
A saída contém um valor correspondente ao valor de S.
O valor deve ser impresso com dois dígitos após o ponto decimal.
'''

# declaração de valores
soma = 0
numerador = 1
denominador = 1

# processamento de dados
while numerador <= 39:
    soma += numerador / denominador
    numerador += 2
    denominador *= 2

# saida de dados
print(f'{soma:.2f}')