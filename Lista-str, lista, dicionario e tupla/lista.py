# Lista de exercícios 2 - Estruturas (strings, listas, tuplas e dicionários)
# Resolva os problemas utilizando apenas os métodos das estruturas de dados e funções nativas (embutidas).
# Não utilize estruturas de decisão (if, elif, else) ou repetição(for e while).


from unittest.util import sorted_list_difference


def palindromo(texto):
    """Faça uma função que verifique se uma texto é palíndromo,
        isto é, se é igual quando lido de trás pra frente.

    Argumento:
        texto (string): Um texto qualquer.

    Retorna:
        bool: True ou False, dependendo dd texto ser palíndromo ou não.
    """

    texto = texto.lower()
    texto = texto.strip()  #tira os espaços nas laterais na frase " ovo " --> "ovo"
    texto = texto.replace(".", "")
    texto = texto.replace("!", "")
    texto = texto.replace(" ", "") #tira os espaços entre as palavras
    return texto == texto [::-1] #retorna ao contrário -------- se for [:-1] ele tira o ultimo valor e n inverte a palavra






def troca_caixa(texto):
    """Vogais ficam em caixa alta (maiúsculas)
        Consoantes ficam em caixa baixa (minúsculas)

    Argumento:
        texto (string): Um texto qualquer.

    Retorna:
        string: o texto convertido, conforme o enunciado.
    """

    grande = texto.lower()
    grande = grande.replace('a', 'A') 
    grande = grande.replace('e', 'E')
    grande = grande.replace('i', 'I')
    grande = grande.replace('o', 'O')
    grande = grande.replace('u', 'U')
    return grande



def imprime_mes_por_extenso(data):
    """Faça um programa que solicite a data de nascimento (dd/mm/aaaa)
        e imprima com o nome do mês por extenso ("dia 99 de mes de 9999").

    Argumento:
        data (string): uma data no formato "dd/mm/aaaa".

    Retorna:
        string: a data, no formato "99 de mês de 9999".
    """

    meses = {
        1: "janeiro", 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro' 
    }

    d, m , a = data.split("/")
    mes_extenso = meses[int(m)]

    return d + " de " + mes_extenso + " de " + a






def encontra_caracter(texto, caracter_procurado):
    """Receba um texto e retorne a localização da primeira vez que
    aparece o caracter especificado.

    Args:
        texto (string): um texto qualquer.
        caracter_procurado (string): um caracter.

    Returns:
        int: a posição do caracter procurado no texto.
    """

    return texto.index(caracter_procurado)



def é_azarado(numero):
    """O último dígito não pode ser igual ao primeiro, porque isso dá azar.

    Argumento:
        numero (string): Um numero, no formato string.

    Retorna:
        bool: True ou False, baseado no enunciado.
    """
    
    return numero [0] == numero[-1]





def ordenamento_contrario(lista):
    """Inverta a ordem dos elementos da lista.

    Argumento:
        lista (list): uma lista de elementos, independente de tipo.

    Retorna:
        list: uma lista com os elementos em ordem inversa.
    """

    #pq o lista.reversed() n funciona?

    a = lista[::-1]
    return a


def maximo(lista):
    """Retorna o maior elemento da lista.

    Argumento:
        lista (list): uma lista de elementos float;

    Retorna:
        int: o maior elemento da lista.
    """

    return max(lista)


def minimo(lista):
    """Retorna o menor elemento da lista.

    Argumento:
        lista (list): uma lista de elementos float;

    Retorna:
        int: o menor elemento da lista.
    """

    return min(lista)


def maior_menor(lista):
    """Calcule o maior e o menor número da lista recebida.

    Argumento:
        lista (list): uma lista de elementos float;

    Retorna:
        uma tupla com dois números inteiros, o maior e o menor da lista.
    """
    menor = min(lista)
    maior = max(lista)
    return maior, menor


def media_saltos_lista(saltos):
    """Receba uma lista com os saltos de um atleta e calcule a média
        dos seus saltos, sabendo que o melhor e o pior saltos são desconsiderados.

    Argumento:
        saltos (list): uma lista com os saltos (float) de um atleta.

    Retorna:
        float: a média dos saltos, de acordo com o enunciado.
    """

    ordem = sorted(saltos)
    del ordem[-1]
    del ordem[0]

    conta = sum(ordem)/len(ordem)
    return conta


def contem(lista, item_procurado):
    """Verifica se uma lista contém um item procurado e devolve um valor booleano.

    Args:
        lista (list): uma lista de elementos de qualquer tipo.
        item_procurado (qualquer tipo): um item a ser procurado na lista.

    Returns:
        bool: um valor booleano (True/False), de acordo com o enunciado.
    """

    return item_procurado in lista




def conta(lista, item_procurado):
    """Informa quantas ocorrências de um item existem numa lista.

    Args:
        lista (list): uma lista de elementos de qualquer tipo.
        item_procurado (qualquer tipo): um item a ser procurado na lista.

    Returns:
        int: a quantidade de ocorrências do item procurado na lista.
    """

    return lista.count(item_procurado)





def mes_extenso(mes):
    """Receba um número correspondente ao mês e devolva a abreviatura do
    nome do mês, com 3 letras.
    Ex.: 1-jan, 2-fev, ..., 12-dez.
    Use uma lista com os nomes dos meses.

    Args:
        mes (list): uma lista de números de 1 a 12 correspondendo aos meses do ano.

    Returns:
        string: a abreviatura do nome do mês, com 3 dígitos.
    """

    lista = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    return lista[mes - 1]
    


def media_temperaturas(temperaturas):
    """Retorna a média das temperaturas da lista.

    Argumento:
        temperaturas (list): uma lista de temperaturas (float).

    Retorna:
        float: a média das temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)


def leet(texto):
    """
    Converte texto em leet. Veja os testes para exemplos.
    Dicionário para usar na conversão:
        troca = {'a':'4','e':'3','g':'9','i':'1','s':'5','t':'7','o':'0'}

    Argumento:
        texto (string): Um texto qualquer.

    Retorna:
        string: o texto convertido, conforme o enunciado.
    """

    texto = texto.replace("a", "4")
    texto = texto.replace("e", "3")
    texto = texto.replace("g", "9")
    texto = texto.replace("i", "1")
    texto = texto.replace("s", "5")
    texto = texto.replace("t", "7")
    texto = texto.replace("o", "0")
    texto = texto.replace("A", "4")
    texto = texto.replace("E", "3")
    texto = texto.replace("G", "9")
    texto = texto.replace("I", "1")
    texto = texto.replace("S", "5")
    texto = texto.replace("T", "7")
    texto = texto.replace("O", "0")
    return texto


def apaga(texto, n):
    """
    Seja uma string texto e um inteiro n,
    retorna uma nova string sem a posição n.

    Argumento:
        texto (string): Um texto qualquer.

    Retorna:
        string: o texto convertido, conforme o enunciado.
    """

    return texto[:n] + texto[n + 1:]


# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = "\033[31m%s" % "Falhou"
    else:
        prefixo = "\033[32m%s" % "Passou"
        acertos += 1
    print(
        "%s Esperado: %s \tObtido: %s\033[1;m" % (prefixo, repr(esperado), repr(obtido))
    )


def main():
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista2 = [-1, 0]
    lista3 = [-10, 0, 10, 2, 100, -100, -100.1]
    lista4 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

    print(" Palíndromo:")
    test(palindromo("ovo"), True)  # normal
    test(palindromo("Ovo"), True)  # mudança de caixa
    test(palindromo("Ovo "), True)  # espaço no final
    test(palindromo(" Ovo "), True)  # espaço no início
    test(palindromo("Assam a massa"), True)  # frases (espaços em branco)
    test(palindromo("Ame o poema!"), True)  # frases com pontuação

    print(" Troca caixa:")
    test(troca_caixa("Araquari"), "ArAqUArI")  # normal
    test(troca_caixa("Caxias do Sul"), "cAxIAs dO sUl")  # com espaços
    test(troca_caixa("joinville"), "jOInvIllE")  # com espaços
    test(troca_caixa("ITAJAI"), "ItAjAI")  # com espaços

    print(" Mês por extenso:")
    test(imprime_mes_por_extenso("19/05/2014"), "19 de maio de 2014")
    test(imprime_mes_por_extenso("25/12/2016"), "25 de dezembro de 2016")

    print(" Encontra caracter:")
    test(encontra_caracter("--*--", "*"), 2)
    test(encontra_caracter("19/05/2014", "/"), 2)

    print(" É azarado:")
    test(é_azarado("213452"), True)
    test(é_azarado("213451"), False)

    print(" Listas invertidas:")
    test(ordenamento_contrario(lista1), ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    test(ordenamento_contrario(lista2), ([0, -1]))
    test(ordenamento_contrario(lista3), ([-100.1, -100, 100, 2, 10, 0, -10]))

    print(" Maior elemento da lista:")
    test(maximo(lista1), 10)
    test(maximo(lista2), 0)
    test(maximo(lista3), 100)
    test(maximo(lista4), -1)

    print(" Maior elemento da lista:")
    test(minimo(lista1), 1)
    test(minimo(lista2), -1)
    test(minimo(lista3), -100.1)
    test(minimo(lista4), -10)

    print(" Maior e o menor elementos da lista:")
    test(maior_menor(lista1), (10, 1))
    test(maior_menor(lista2), (0, -1))
    test(maior_menor(lista3), (100, -100.1))
    test(maior_menor(lista4), (-1, -10))

    print(" Média dos saltos em lista:")
    test(media_saltos_lista([10, 10, 10, 10, 10]), 10)
    test(media_saltos_lista([9, 9.1, 8, 7, 6.9]), 8)
    test(media_saltos_lista([1, 1, 3, 5, 5]), 3)
    test(media_saltos_lista([10, 10, 9.9, 10, 10]), 10)
    test(media_saltos_lista([1, 4.5, 0, 7, 5]), 3.5)

    print("Possui item:")
    test(contem([1, 2, 3, 4, 5], 6), False)
    test(contem([1, 2, 3, 4, 5], 3), True)
    test(contem(["b", "s", "i"], "i"), True)
    test(contem(["b", "s", "i"], "S"), False)

    print("Conta itens:")
    test(conta([1, 2, 3, 4, 5], 6), 0)
    test(conta([1, 2, 3, 4, 5], 1), 1)
    test(conta([1, 2, 1, 4, 1], 1), 3)
    test(conta(["b", "s", "i"], "i"), 1)
    test(conta(["b", "s", "i"], "S"), 0)
    test(conta(["b", "s", "i", "i", "f", "c"], "i"), 2)

    print("Mês por extenso:")
    test(mes_extenso(1), "jan")
    test(mes_extenso(2), "fev")
    test(mes_extenso(12), "dez")

    print("Média das temperaturas:")
    test(media_temperaturas([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 10.0)
    test(media_temperaturas([10, 12, 9, 13, 12, 10, 9, 13, 10, 12, 9, 13]), 11.0)

    print("leet")
    test(leet("ifc"), "1fc")
    test(leet("fisl2013"), "f15l2013")
    test(leet("deco"), "d3c0")
    test(leet("EMO"), "3M0")
    test(leet("restart"), "r3574r7")
    test(leet("infeliz"), "1nf3l1z")
    test(leet("The Cure"), "7h3 Cur3")
    test(leet("Eu te amo"), "3u 73 4m0")

    print("Apaga")
    test(apaga("kitten", 1), "ktten")
    test(apaga("kitten", 0), "itten")
    test(apaga("kitten", 2), "kiten")
    test(apaga("kitten", 4), "kittn")
    test(apaga("Hi", 0), "i")
    test(apaga("Hi", 1), "H")
    test(apaga("code", 0), "ode")
    test(apaga("code", 1), "cde")
    test(apaga("code", 2), "coe")
    test(apaga("code", 3), "cod")
    test(apaga("chocolate", 8), "chocolat")


if __name__ == "__main__":
    main()
    print(
        "\n%d Testes, %d Ok, %d Falhas: Nota %.1f"
        % (total, acertos, total - acertos, float(acertos * 10) / total)
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")