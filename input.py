# Tratamento do Input

def entrada():
    
    # Pega três números como entrada do usuário e trata o erro caso o usuário cometa algum erro
    while True:
        try:
            num1 = int(input("Digite o primeiro número a ser testado -> "))
            num2 = int(input("Digite o segundo número a ser testado  -> "))
            num3 = int(input("Digite o primeiro número a ser testado -> "))
            
            return num1, num2, num3
        except ValueError:
            print("\nERRO: Só serão aceitos números inteiros!\n")
