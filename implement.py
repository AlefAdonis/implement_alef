# Define função que pega tres numero e retorna o maior
# inteiro entre eles.

def max_num(tupla):

    num1 = tupla[0]                    # pegando os valores da tupla na posiçao 0
    num2 = tupla[1]                    # pegando os valores da tupla na posiçao 1
    num3 = tupla[2]                    # pegando os valores da tupla na posiçao 2

    
    if num1 >= num2:                   # se numero 1 for maior ou igual a numero 2
        if num1 >= num3:               # e maior que numero 3
            return num1                # retorne numero 1
    else:
        if num2 >= num3:               # se numero 2 for maior ou igual ao numero 3
            return num2                # retorne numero 2
        else:
            return num3                # senão, retorne numero 3

