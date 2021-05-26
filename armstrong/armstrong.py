    
def calc(numero):

    tam = len(numero)
    soma = 0
    for n in range(0,tam):
        soma += int(numero[n])**tam

    if soma == int(numero):
        print(tam)

    else:
        print("-1")
    
