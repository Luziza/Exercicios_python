#!/usr/bin/env python3
# Lista de exercícios - Estruturas de repetição For

# ATENÇÃO !!!
# Todos os exercícios devem ser resolvidos com "for".
# Utilizar "for item in lista" sempre que possível.
# Utilizar "for i, item in enumerate(item) sempre que possível.


import math


def soma_das_temperaturas(lista):
    """Retorna a soma_das_temperaturas dos elementos de uma lista.

    Argumentos:
        lista (lista de floats): Uma lista de valores float.

    Retorna:
        float: a soma_das_temperaturas dos elementos da lista.
    """
    
    soma = 0
    for i in lista:
        soma += i
    return soma


def quantidade_de_impares(valor_inicial, valor_final):
    """Determine a quantidade de números ímpares num intervalo,
    excluindo os valores limite do intervalo.

    Argumentos:
        valor_inicial (int): o limite inferior do intervalo, excluindo-o;
        valor_final (int): o limite superior do intervalo, excluindo-o;

    Retorna:
        int: a quantidade de números ímpares dentro do intervalo dado.
    """

    
    valor1 = valor_inicial + 1
    valor2 = valor_final 
    lista = []
    for i in range(valor1, valor2):
        if i % 2 != 0:
            lista.append(i)
    return len(lista)


def soma_das_temperaturas_dos_inteiros(valor1, valor2):
    """Calcule a soma_das_temperaturas dos números inteiros no intervalo dado.
    Considere que os limites do intervalo podem ser informados
    como números negativos ou fora de ordem.
    Ex: 1 e 5 ou 5 e 1, retorna 9

    Argumentos:
        valor1 (int): um dos limite do intervalo, excluindo-o;
        valor2 (int): o outro limite do intervalo, excluindo-o;

    Retorna:
        float: a soma_das_temperaturas dos valores dentro do intervalo dado.
    """

    lista = []
    if valor1 < valor2:
        for i in range (valor1 + 1, valor2):
            lista.append(i)
        return sum(lista)
    elif valor1 > valor2:
        for i in range (valor2 + 1, valor1):
            lista.append(i)
        return sum(lista)




def serie(n):
    """Dado n, calcule o valor de
    s = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n

    Argumento:
        n (int): o valor final da série;

    Retorna:
        float: a soma_das_temperaturas dos valores da série,
        segundo a fórmula e o valor de n informados.

    """

    lista = []
    for i in range(1, n + 1):
        conta = (1/i)
        lista.append(conta)
    return round(sum(lista), 2)


def ordenamento_contrario(lista):
    """Inverta a ordem dos elemntos da lista.

    Argumento:
        lista (list): uma lista de elementos, independente de tipo.

    Retorna:
        list: uma lista com os elementos a ordem invertida.
    """






def intercalamento_listas(lista1, lista2):
    """Usando 'lista1' e 'lista2', ambas do mesmo comprimento,
    crie uma nova lista composta pelo intercalamento entre as duas.
    Intercalar significa que a nova lista terá o 1o elemento da 1a lista,
    seguido do 1o elemento da 2a lista, seguido do 2o elemento da 1o lista,
    seguido do 2o elemento da 2a lista e assim por diante.

    Argumentos:
        lista1 (list): uma lista de elementos, independente de tipo;
        lista2 (list): uma lista de elementos, independente de tipo;

    Retorna:
        list: uma lista com os elementos intercalados das duas listas recebidas.
    """

    novo = []
    # zip: O que a função fez foi: para cada elemento da lista x, juntou o elemento correspondente 
    # em posição da lista y a ele em uma tupla e a adicionou a uma lista.
    for i, a in zip(lista1, lista2):
        novo.append(i)
        novo.append(a)
    return novo


def im_pares(lista):
    """Separe em listas os pares e impares, dos inteiros da lista recebida.

    Argumento:
        lista (lista de inteiros): uma lista de elementos int;

    Retorna:
        uma tupla com duas listas de inteiros sendo a primeira uma lista com os pares
        e a segunda uma lista com os ímpares.
    """

    lista_par = []
    lista_impar = []

    for i in lista:
        if i % 2 == 0:
            lista_par.append(i)
        else:
            lista_impar.append(i)
    return (lista_par, lista_impar)

def maior_menor(lista):
    """Calcule o maior e o menor número da lista recebida.

    Argumento:
        lista (list): uma lista de elementos float;

    Retorna:
        uma tupla com dois números inteiros, o maior e o menor da lista.
    """

    tupla = []
    for i in lista:
        if i == max(lista):
            tupla.append(i)
        elif i  == min(lista):
            tupla.append(i)
    return tuple(sorted(tupla, reverse=True))

           


def dar_troco(valor_a_pagar, valor_em_dinheiro):
    """Calcule o troco a devolver ao cliente com notas de 1,2,5,10,20,50.
        A resposta deve conter a quantidade de cada nota, sem considerar centavos.

    Argumentos:
        valor_a_pagar (float): o valor da conta
        valor_em_dinheiro (float): o valor que foi dado para pagar a conta.

    Retorna:
        uma lista de uma tuplas, onde cada dupla contém dois valores:
        o valor da nota e a quantidade daquela nota.
        Se a quantidade de notas for igual a zero, não deve aparecer na lista.
    """




def media_anual(temperaturas):
    """Receba uma lista com as temperaturas médias de cada mês
    e devolva uma lista com os números correspondentes aos meses
    que possuem temperatura superior á média anual.

    Argumentos:
        temperaturas (lista de floats): as temperaturas médias de cada mês no ano, em ordem.

    Retorna:
        lista de inteiros: uma lista com o número correspondente ao mês em que a
        temperatura média foi maior que a temperatura média anual.
    """

    lista = []
    anual = sum(temperaturas) / len (temperaturas)
    for i, numero in enumerate(temperaturas):
        if numero > anual:
            lista.append(i)
    return lista

def maiores_13(idades, alturas):
    """Receba as idades e alturas de diversas pessoas, em duas
        listas separadas e de igual comprimento.
        Calcule a media das alturas e retorne as alturas daqueles que
        possuem 'idades' maior que 13 e altura inferior a media da turma.

    Argumentos:
        idades (lista de inteiros): Uma lista de idades;
        alturas (lista de floats): uma lista de alturas;

    Retorna:
        uma lista de alturas dos alunos, conforme o critério definido.
    """

    lista_nova = []

    conta_i = sum(idades) / len(idades)
    conta_a = sum(alturas) / len(alturas)

    for a, y in zip(idades, alturas):
        if a > 13 and y < conta_a:
            lista_nova.append(y)
       
    return lista_nova


def testa_primo(valor):
    """Recebe um valor e verifica se ele é um número primo ou não.

    Argumento:
        valor (int): um número inteiro.

    Retorna:
        bool: True ou False, se o valor e ou não primo.
    """


        


def lista_de_primos(inicio, fim):
    """Retorne uma lista de primos entre os valores informados, incluindo
    os limites.

    Argumentos:
        inicio (int): limite inferior;
        fim (int): limite superior;

    Retorna:
        lista de inteiros, os primos dentro do intervalo especificado.
    """

    lista = []
    for i in range(inicio, fim):
            if  i == 2 or i == 3 or i == 5 or i == 11 or i == 7 or i == 13 or i > 1 and i % i == 0 and i % 2 != 0  and i % 3 != 0 and i % 5 != 0 and i % 11 != 0 and  i % 13 != 0 and i % 7 != 0:
                lista.append(i)
    return lista



def fibonacci(n):
    """Retorne uma lista com os n primeiros valores da série de Fibonacci.
    Fibonacci = 1,1,2,3,5,8,13,...

    Argumento:
        n (int): a quantidade de elementos que serão gerados.

    Retorna:
        uma lista de elementos inteiros correspondendo aos n primeiros elementos da série
        de Fibonacci.
    """

    penultimo = 1
    antipenultimo = 0
    lista = []

    for i in range(0, n):
        penultimo = penultimo + antipenultimo
        antipenultimo += antipenultimo
        antipenultimo += penultimo 
        i += i
        lista.append(penultimo)
    return lista






def altera_salarios(salarios):
    """Calcule o aumento de salário de acordo com a seguinte tabela:
    - até 1 SM(inclusive): aumento de 20%
    - de 1 até 2 SM(inclusive): aumento de 15%
    - de 2 até 5 SM(inclusive): aumento de 10%
    - acima de 5 SM: aumento de 5%
    Salário mínimo para referência: R$ 724,00

    Argumento:
        salarios (lista de floats): os salários originais.

    Retorna:
        uma lista de elementos float, correspondendo aos salários corrigidos.
    """

    lista = []
    minimo = 724
    for i in salarios:
        if i <= minimo:
            total = (i * 0.20) + i
            lista.append(total)
        elif i > minimo and i <= (minimo * 2):
            total1 = (i * 0.15) + i
            lista.append(total1)
        elif i > minimo * 2 and i <= (minimo * 5):
            total2 = (i * 0.10) + i
            lista.append(total2)
        elif i > minimo * 5:
            total3 = (i * 0.05) + i
            lista.append(total3)
    return lista






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

    print("soma_das_temperaturas elementos da lista:")
    test(soma_das_temperaturas([]), 0)
    test(soma_das_temperaturas([0]), 0)
    test(soma_das_temperaturas([1]), 1)
    test(soma_das_temperaturas([1, 1]), 2)
    test(soma_das_temperaturas([2, 3]), 5)
    test(soma_das_temperaturas([1, 3, 2, 5]), 11)
    test(soma_das_temperaturas([-1, 1]), 0)
    test(soma_das_temperaturas([10, -10]), 0)
    test(soma_das_temperaturas([-2, -1]), -3)

    print("Quantidade de ímpares:")
    test(quantidade_de_impares(1, 10), 4)
    test(quantidade_de_impares(1, 11), 4)
    test(quantidade_de_impares(1, 50), 24)
    test(quantidade_de_impares(1, 60), 29)
    test(quantidade_de_impares(40, 80), 20)

    print("soma_das_temperaturas de números inteiros:")
    test(soma_das_temperaturas_dos_inteiros(1, 5), 9)
    test(soma_das_temperaturas_dos_inteiros(1, 50), 1224)
    test(soma_das_temperaturas_dos_inteiros(50, 1), 1224)
    test(soma_das_temperaturas_dos_inteiros(10, 1), 44)
    test(soma_das_temperaturas_dos_inteiros(-10, 1), -45)
    test(soma_das_temperaturas_dos_inteiros(10, -10), 0)

    print("Série:")
    test(serie(1), 1.00)
    test(serie(15), 3.32)
    test(serie(10), 2.93)
    test(serie(5), 2.28)

    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista2 = [-1, 0]
    lista3 = [-10, 0, 10, 2, 100, -100, -100.1]
    lista4 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
    lista5 = [1, 3, 5, 7, 9]
    lista6 = [2, 4, 6, 8, 10]

    print(" Listas invertidas:")
    test(ordenamento_contrario(lista1), ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    test(ordenamento_contrario(lista2), ([0, -1]))
    test(ordenamento_contrario(lista3), ([-100.1, -100, 100, 2, 10, 0, -10]))

    print(" Lista Intercalada:")
    test(intercalamento_listas(lista5, lista6), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test(intercalamento_listas(lista6, lista5), [2, 1, 4, 3, 6, 5, 8, 7, 10, 9])

    print(" Lista de pares e impares:")
    test(im_pares(lista1), ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9]))
    test(im_pares(lista5), ([], [1, 3, 5, 7, 9]))
    test(im_pares(lista6), ([2, 4, 6, 8, 10], []))

    print(" Maior e o menor da lista:")
    test(maior_menor(lista1), (10, 1))
    test(maior_menor(lista2), (0, -1))
    test(maior_menor(lista3), (100, -100.1))
    test(maior_menor(lista4), (-1, -10))

    print(" Troco do pagamento:")
    test(dar_troco(10, 10), [])
    test(dar_troco(1, 201), [(50, 4)])
    test(dar_troco(10, 148), [(50, 2), (20, 1), (10, 1), (5, 1), (2, 1), (1, 1)])
    test(dar_troco(10, 109), [(50, 1), (20, 2), (5, 1), (2, 2)])

    print(" Meses acima da média:")
    test(media_anual([20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]), [])
    test(media_anual([25, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]), [0])
    test(
        media_anual([23, 25, 26, 24, 21, 22, 26, 24, 25, 22, 23, 19]),
        [1, 2, 3, 6, 7, 8],
    )
    test(
        media_anual([19, 20, 21, 20, 17, 18, 19, 20, 22, 21, 20]),
        [1, 2, 3, 7, 8, 9, 10],
    )
    test(
        media_anual([21, 22, 23, 21, 22, 22, 23, 21, 23, 22, 21, 23, 21]),
        [1, 2, 4, 5, 6, 8, 9, 11],
    )

    print(" Alturas abaixo da media:")
    test(maiores_13([13, 13, 14], [1.7, 1.7, 1.5]), [1.5])
    test(maiores_13([13, 13, 14, 13], [1.7, 1.7, 1.5, 1.6]), [1.5])
    test(maiores_13([14, 20], [1.6, 2]), [1.6])
    test(maiores_13([10, 7, 13, 15, 20, 21], [1.7, 1.21, 1.65, 2, 1.9, 1.5]), [1.5])
    test(
        maiores_13([14, 15, 16, 17, 18, 30], [1.9, 1.89, 1.85, 1.95, 2, 1.99]),
        [1.9, 1.89, 1.85],
    )
    test(
        maiores_13([10, 9, 90, 9, 13, 14, 15], [1.25, 1.3, 1.7, 1.41, 1.5, 1.55, 1.7]),
        [],
    )

    print(" Testa se um número é primo:")
    test(testa_primo(0), False)
    test(testa_primo(1), False)
    test(testa_primo(2), True)
    test(testa_primo(3), True)
    test(testa_primo(4), False)
    test(testa_primo(5), True)
    test(testa_primo(7), True)
    test(testa_primo(9), False)
    test(testa_primo(11), True)
    test(testa_primo(13), True)

    print(" Lista de primos:")
    test(lista_de_primos(0, 1), [])
    test(lista_de_primos(5, 10), [5, 7])
    test(lista_de_primos(10, 20), [11, 13, 17, 19])
    test(lista_de_primos(0, 21), [2, 3, 5, 7, 11, 13, 17, 19])
    test(
        lista_de_primos(43, 102), [43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    )

    print(" Fibonacci:")
    test(fibonacci(1), [1])
    test(fibonacci(2), [1, 1])
    test(fibonacci(3), [1, 1, 2])
    test(fibonacci(4), [1, 1, 2, 3])

    print(" Aumenta salários:")
    test(
        altera_salarios(
            [500, 724.0, 725.00, 1448.00, 1449.00, 3620.00, 3621.00, 4000.00]
        ),
        [600.0, 868.8, 833.75, 1665.2, 1593.9, 3982.0, 3802.05, 4200.0],
    )


if __name__ == "__main__":
    main()
    print(
        f"\n{total} Testes, {acertos} Ok, {total - acertos} Falhas: Nota {round(acertos * 100 / total)}"
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")