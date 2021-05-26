# Menu que será mostrado ao usuário

import implement as imp               # importe das funções necessárias
import input as ipt                   

def menu():
    while True:
        print("""
            Se você deseja saber qual o maior
            entre três números, encontrou o 
            programa certo!\n""")

        tupla = ipt.entrada()                                                                    # Invocação da função que pega dados
        maior_num = imp.max_num(tupla)                                                           # Invocação da função que processa os dados

        print(f"O maior número entre {tupla[0]}, {tupla[1]} e {tupla[2]} é {maior_num} .")       # Resultado do processamento de quem é o maior
        valid = input("\nDeseja tentar mais uma vez?(Y/N) ")                                     # Pergunta ao usuário se ele quer rodar o código mais uma vez

        if valid.lower() == "n":                                                                 # Verifica se a resposta foi não e sai do programa
            print("\nObrigado por usar o programa!")
            break