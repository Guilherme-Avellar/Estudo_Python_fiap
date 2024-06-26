
# Uma forma de fazer a documentação como o UML prega em python

# Lembrando que no python não há a obrigatoriedade de definição de tipos


def media0(n1: float, n2: float) -> float:
    return (n1 + n2) / 2

# ou

def media1(n1, n2: float) -> float:
    return (n1 + n2) / 2

# outro exemplo

def media2(nota1: float, nota2: float) -> str:
    media: float
    media = (nota1 + nota2) / 2
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

# outro exemplo, que seria o void do C/C++

# Atenção, há um detalhe nessa função. Se nenhum parametro for passado a ela quando
# for chamada, ela usará esses que estão em seus parametros (Edson e 8). Porém, se
# for passado algo como parametro ela descarta esses valores. Chamados de VALOR PADRÃO
# evita erros
def saudacao(usuario: str = 'Edson', hora: int = 8) -> None:
    if hora < 12:
        turno = "Bom dia"
    elif hora < 18:
        turno = "Boa tarde"
    else:
        turno = "Boa noite"
    print(f"{usuario}, {turno} ! Seja bem-vindo à FIAP!")



print ("corta pra 18")

# Os floats ao lado de n1 e n2 indicam que os parâmetros devem ser do tipo float,
# enquanto o último float, ao lado de ->, significa que a função retornará um dado float


