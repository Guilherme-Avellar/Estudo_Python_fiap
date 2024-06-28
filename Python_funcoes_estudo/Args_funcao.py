
# Args, algo comum em C++ e Java, é um tipo de parâmetro que permite que a função
# receba um número ilimitado de paramentros quando ela for chamada.

# Detalhe, Args é o nome padrão pelas boas práticas, algo padrão, mas é possível por
# outro nome como *abacate

# exemplo
def mediaNs(*args):
    soma = 0
    for n in args:
        soma += n
    return soma / len(args) # len retorna o total de elementos de uma coisa

# pode passar qualquer quantidade de números
print(f"Média de quanto números quisermos: {mediaNs(1,2,3,9,10)}")
print(f"Média de quanto números quisermos: {mediaNs(1,2,3,9,10,4,5,6,7,8,9,10,4)}")

