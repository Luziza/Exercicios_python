# Avaliação 3 - BSI
# Utilize for ou while em todo os problemas abaixo.


def fibonacci_ate_valor(n):
    """
    Retorne uma lista com os elementos até chegar no valor de n.
    Fibonacci = 1,1,2,3,5,8,13,...

    Argumento:
        n (int): o valor limite do termo da série.

    Retorna:
        uma lista de elementos inteiros.
    """

    n1 = 0
    n2 = 1

    lista = [1]
        
    while n2 < n:
        soma = n1 + n2
        n1 = n2
        n2 = soma
        lista.append(soma)
        
    return lista




def multiplos_sete_ordenados_sem_repeticao(lista):
    """
    Faça uma função que receba uma lista e retorne uma nova lista,
    com os números divisíveis por 7, em ordem crescente, sem repetição.

    Argumento:
        lista: uma lista de números.

    Retorna:
        list: uma lista, de acordo com o critério estabelecido.
    """

    nova = []
    for i, numero in enumerate(lista):
        if numero % 7 == 0:
            nova.append(numero)
    return sorted(set((nova)))



def converte_nome_funcao(nome):
    """
    Camel Casing é uma forma de escrever nomes de identificadores, (como varíaveis e funções) usando letras maiúsculas para separar as palavras.
    A palavra "camel" em inglês significa camelo (lembre-se das córcovas do camelo e tudo faz sentido). Desenvolva uma solução que quebre o "camel casing", usando espaços entre as palavras.

    Exemplo
    "camelCasing"  =>  "camel Casing"
    "mediaFinalAposRecuperacao"  =>  "media Final Apos Recuperacao"
    "soma"   =>  "soma"
    "" =>  ""

    Argumento:
        nome (string): a palavra original que será processada.

    Returna:
        string: um conjunto de palavras, que foram separadas segundo o critério do "camel casing".
    """

    novo = ''
    for i in nome:
        if i == i.upper():
            novo += ' ' + i 
        else:
            novo += i
    return novo

def apenas_letras(conteudo):
    """
    Faça uma função que receba um texto e retorne apenas as letras.
    Remova números, espaços e caracteres de pontuação.

    Argumento:
        conteudo (string): um texto contendo letras, números, sinais de pontuação e espaços em branco.

    Retorna:
        string: uma string contendo apenas as letras.
    """

    characters = "1-! 23456789()"
    for i in range(len(characters)):
        conteudo = conteudo.replace(characters[i],"")

    return conteudo

def crescimento_populacional_2(populacao_atual, percentual, aumento, populacao_final):
    """
    Determine quantos anos a população da cidade levará para ultrapassar a população final. Os valores de população atual, percentual de aumento anual, aumento por mudança e da população final são informados como parâmetros da função.

    Aqui vai um exemplo: suponha que a população é p0 = 1000 no início do ano. A população aumenta regularmente em 2% ao ano e, além disso, 50 novos habitantes por ano vêm morar na cidade.

    Quantos anos a cidade precisa para ver sua população maior ou igual a p = 1200 habitantes?

    No final do primeiro ano, haverá:
    1000 + 1000 * 0,02 + 50 => 1070 habitantes (o número de habitantes é um inteiro)

    No final do 2º ano, haverá:
    1070 + 1070 * 0,02 + 50 => 1141 habitantes

    No final do 3º ano, haverá:
    1141 + 1141 * 0,02 + 50 => 1213

    Serão necessários 3 anos inteiros.

    Observação:
    Não se esqueça de converter o parâmetro de porcentagem em porcentagem no corpo de sua função: se o parâmetro de porcentagem for 2, você deve convertê-lo para 0,02.

    Argumentos:
        populacao_atual (int): a população inicial, no ano zero.
        percentual (float): o percentual de aumento da população a cada ano.
        aumento (int): a quantidade de pessoas que chegam na cidade de fora.
        populacao_final (int): a população que se quer chegar.

    Returna:
        int: a quantidade de anos até se alcançar (ou passar) a população final.
    """

    anos = 0
    p = percentual / 100
    while populacao_atual < populacao_final:
        populacao_atual += (populacao_atual * p) + aumento
        anos += 1
    return anos


# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = f"\033[31m{'Falhou'}"
    else:
        prefixo = f"\033[32m{'Passou'}"
        acertos += 1
    print(f"{prefixo} Esperado: {esperado} \tObtido: {obtido}\033[1;m")


def main():
    print("Fibonnaci até um valor:")
    test(fibonacci_ate_valor(3), [1, 1, 2, 3])
    test(fibonacci_ate_valor(5), [1, 1, 2, 3, 5])
    test(fibonacci_ate_valor(7), [1, 1, 2, 3, 5, 8])
    test(fibonacci_ate_valor(20), [1, 1, 2, 3, 5, 8, 13, 21])

    print("Múltiplos de sete ordenados e sem repetição:")
    test(multiplos_sete_ordenados_sem_repeticao([2, 2]), [])
    test(multiplos_sete_ordenados_sem_repeticao([1, 6, 14]), [14])
    test(multiplos_sete_ordenados_sem_repeticao([1, 7, 14]), [7, 14])
    test(multiplos_sete_ordenados_sem_repeticao([14, 1, 2, 7]), [7, 14])
    test(
        multiplos_sete_ordenados_sem_repeticao([21, 1, 7, 23, 7, 14, 7, 5]), [7, 14, 21]
    )

    print("Converte nome função:")
    test(converte_nome_funcao("helloWorld"), "hello World")
    test(converte_nome_funcao("camelCase"), "camel Case")
    test(converte_nome_funcao("breakCamelCase"), "break Camel Case")
    test(
        converte_nome_funcao("quantidadeDeDiasPerdidosPorFumar"),
        "quantidade De Dias Perdidos Por Fumar",
    )
    test(
        converte_nome_funcao("mediaFinalAposRecuperacao"),
        "media Final Apos Recuperacao",
    )

    print("Apenas letras:")
    test(apenas_letras("BSI1 Programação 1"), "BSIProgramação")
    test(apenas_letras("BSI1-Programação1!"), "BSIProgramação")
    test(apenas_letras("(47) 9 9988-7766"), "")

    print("Crescimento Populacional:")
    test(crescimento_populacional_2(1000, 2, 50, 1200), 3)
    test(crescimento_populacional_2(1500, 5, 100, 5000), 15)
    test(crescimento_populacional_2(1500000, 2.5, 10000, 2000000), 10)


if __name__ == "__main__":
    main()
    print(
        f"\n{total} Testes, {acertos} Ok, {total - acertos} Falhas: Nota {round(acertos * 100 / total)}"
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")