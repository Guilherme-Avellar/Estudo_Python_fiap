# DEFINIÇÃO DOS subalgoritmoS
# Definição da função superior

# explicação:

# Função encadeada é: Uma função criada dentro de outra que só funciona na função criada,
# ou seja o programa principal não consegue "chamar" a função que foi criada em outra
# diretamente, pois ela esta no escopo da função em que foi criada. Para chama-la, deve-se
# chamar a função principal, para função principal chamar ela, caso precise, pois tem a
# possibilidade não precisar usa-la.

# exemplo:

def media2notas(n1: float, n2: float) -> float:
    # Definição da função encadeada
    def nota_valida(nota: float) -> bool:
        return 0 <= nota <= 10
        # return nota >= 0 and nota <= 10 (tbm funciona, mas o python gosta mais do outro jeito)

    # nota_valida(3.14) # -> não daria erro chamar a função aqui, mas não faz sentido esse comando
    # comparar com linha 39

    # continuação da escrita da função superior
    if nota_valida(n1) and nota_valida(n2):
        return (n1 + n2) / 2
    else:
        return -1
        # retornará -1 caso um dos parâmetros não seja uma nota válida


# PROGRAMA PRINCIPAL
nota1 = float(input("Nota 1:"))
nota2 = float(input("Nota 2:"))
retorno = media2notas(nota1, nota2)
if retorno == -1:
    print("Nota(s) inválida(s)!")
else:
    print(f"Média = {retorno}")

# nota_valida(3.14) # -> Da erro chamar a função fora do escopo da principal
