

# Forma 1
# essa forma de importar outro arquivo, exige que todos os subalgoritimos sejam iniciados
# pelo nome do arquivo

# import Recurcao

# Recurcao.contagemRecursiva(1, 10)

# contagemRecursiva(1, 10) # -> isso, por exemplo não funcionaria, daria erro


# Tem que chamar o nome do arquivo, depois o que vc quer desse arquivo com `.`
# Porém executa o que esta no arquivo principal. Há uma chamada de função nele


# Forma 2
# importa apenas o que vc quer da biblioteca. Pode separando com virgula depois do import, as
# funcinalidade escolhidas

# from Recurcao import contagemRecursiva

# contagemRecursiva(1, 10)

# Forma 3
# importar todas as funcionalidades do arquivo

# from Recurcao import *

# contagemRecursiva(1, 10)

# Parecido com a Forma 1, poupa a escrita do arquivo mais a funcionalidade


# Vantagens e desvantagens:
# Dependendo da situação, não é bom importar tudo como na Forma 3, por administração
# de memória, então a Forma 1 e Forma 2 pode ser conveniente, importando apenas o que
# se irá usar. A Forma 1 apenas possui mais sintaxe.
