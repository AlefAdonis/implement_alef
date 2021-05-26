def entrada():

    try:
        numero = int(input("Digite um número: "))

        return str(numero)
    
    except RuntimeError and ValueError:
        print("ERRO!")
