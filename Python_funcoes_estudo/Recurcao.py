
# Algoritimo simple de recurção ensinado pela fiap

# DEFINIÇÃO DO subalgoritmo RECURSIVO
def contagemRecursiva(inicio: float, limite: float) -> None:
    if inicio > limite:
        print("Fim!")
    else:
        print(inicio)
        contagemRecursiva(inicio + 1, limite)

# PROGRAMA PRINCIPAL
print("Executando a função recursiva...")
contagemRecursiva(1, 3)
