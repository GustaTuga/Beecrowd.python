# Loop ate achar números iguais
while True:
    x, y = map(int, input().split())
    if x != y:
        if x > y:
            print('Decrescente')
        else:
            print('Crescente')
    else:
        break