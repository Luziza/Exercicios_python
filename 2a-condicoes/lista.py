# Lista de exercícios - Condições


def acrescimo_nota_bb(nota_sozinho, nota_com_ajuda):
    """Recebe a nota do litle brother antes de receber ajuda, e a nota
    depois que o big brother ajudou, e retorna o acrecimo que o big
    brother recebera em sua nota pela ajuda.
    O acréscimo é de 1/4 da diferença das notas, se for positivo.

    Argumentos:
        nota_sozinho (float): a nota que o aluno tirou sem ajuda.
        nota_com_ajuda (float): a nota que o aluno tirou após ter sido ajudado.

    Retorna:
        float: o acréscimo na nota obtido pelo aluno que ajudou seu colega.
    """

    conta = (nota_com_ajuda - nota_sozinho) / 4
    if (nota_com_ajuda - nota_sozinho) > 0:
        return round(conta, 1)
    else:
        return 0


def maior3(a, b, c):
    """Recebe três valores, e retorna o maior dos três.

    Argumentos:
        a (float): primeiro valor;
        b (float): segundo valor;
        c (float): terceiro valor;

    Retorna:
        float: o maior entre os três valores.
    """

    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else: 
        return c


def menor3(a, b, c):
    """Recebe três valores, e retorna o menor dos três.

    Argumentos:
        a (float): primeiro valor;
        b (float): segundo valor;
        c (float): terceiro valor;

    Retorna:
        float: o menor entre os três valores.
    """

    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else: 
        return c


def testa_lados(a, b, c):
    """Receba os três lados de um triângulo. Informe se os valores
    podem ser um triângulo. Indique, caso os lados formem um triângulo,
    se o mesmo é: equilátero, isósceles ou escaleno.

    Argumentos:
        a (float): primeiro lado;
        b (float): segundo lado;
        c (float): terceiro lado;

    Retorna:
        string: um texto indicando o resultado,
                conforme aparece nos testes no final desse arquivo.
    """

    if a + b < c or c + a < b or b + c < a:
        return "Não forma um triângulo"
    elif a == b == c:
        return "Triângulo equilátero"
    elif a != b != c and a != c:
        return "Triângulo escaleno"
    else: 
        return "Triângulo isósceles"

def ano_bissexto(ano):
    """Determine se um ano é bissexto ou não.

    Argumento:
        ano (int): um ano, no formato de 4 dígitos.

    Retorna:
        bool: True ou False (verdadeiro ou falso), caso a ano seja ou não bissexto.
    """

    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return True
    else:
        return False


def maior_dia_do_mes(mes, ano):
    """Retorna o último dia do mês para um determinado ano e mês.
        Os valores possíveis são: 28, 29, 30 ou 31.
        Devem ser considerados os anos bissextos.
        Uma função separada para determinar se um ano é bissexto
        poderia ser utilizada.

    Argumentos:
        mes (int): um mês no formato de dois dígitos;
        ano (int): um ano, no fomato de 4 dígitos;

    Retorna:
        int: um inteiro indicando o último dia válido para aquele mês e ano.
    """

    if mes == 1 or mes == 3 or mes == 5 or mes == 7  or mes == 10 or mes == 12:
        return 31
    elif mes == 4 or mes == 6 or mes == 8 or mes == 9 or mes == 11 :
        return 30
    elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 and mes == 2:
        return 29
    else: return 28


def data_valida(data):
    """Recebe uma string no formato dd/mm/aaaa e informa
        um valor lógico indicando se a data é válida ou não.
        Verifica se ano é bissexto e outros detalhes.
        Confira os testes no final do arquivo para mais detalhes.

    Argumentos:
        data (string): data no formato "dd/mm/aaaa".

    Retorna:
        bool: True ou False, indicando se a datá é válida ou não.
    """

    d, m, a = data.split("/")
    if int(d) == 0 or int(m) == 0 or int(a) == 0:
        return False
    elif int(m) == 4 or int(m) == 6 or int(m) == 8 or int(m) == 9 or int(m) == 10 or int(m) == 11 and int(d) == 31:
        return False
    elif int(m) == 4  and int(d) == 30:
        return True
    elif int(d) > 31 or int(m) > 12:
        return False
    else: 
        return True

def delta(a, b, c):
    """Calcula delta, que é utilizado na fórmula de báskara.
    delta = b ** 2 - (4 * a * c)

    Args:
        a (float): coeficiente da função
        b (float): coeficiente da função
        c (float): coeficiente da função

    Retorna:
        (float): o valor do delta
    """

    delta = (b * b) - (4*a*c)
    return delta


def baskara(a, b, c):
    """Calcule as raízes de uma equação do segundo grau, na forma
    ax2 + bx + c. A função recebe a, b e c e faz as consistências,
    informando ao usuário nas seguintes situações:
    - Se o usuário informar o valor de A igual a zero é uma equaçao do 1o grau.
    - Se o delta calculado for negativo, a equação não possui raizes reais.
    Devolva uma tupla vazia.
    - Se o delta calculado for igual a zero a equação possui apenas uma
    raiz real. Devolva uma tupla com um único valor.
    - Se o delta for positivo, a equação possui duas raiz reais.
    Devolva uma tupla com dois valores.

    Argumentos:
        a (float): valor a da equação;
        b (float): valor b da equação;
        c (float): valor c da equação;

    Retorna:
        tupla de floats: uma tupla, contando os valores das raízes, sendo
        uma raiz, duas raízes ou uma tupla vazia caso não existam raízes.
    """

    import math
    delta = (b * b) - (4*a*c)

    if a == 0:
        return (-c/b,)
    elif delta < 0:
        return ( )
    elif delta == 0:
        return ((-b + math.sqrt(delta)) / 2*a, )
    elif delta > 0:
        conta1 = (-b + math.sqrt(delta)) / (2*a)
        conta2 = (-b - math.sqrt(delta)) / (2*a)
        return (conta1, conta2)





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
    print("Acréscimo BB:")
    test(acrescimo_nota_bb(1, 10), 2.2)
    test(acrescimo_nota_bb(7, 6), 0.0)
    test(acrescimo_nota_bb(0, 10), 2.5)
    test(acrescimo_nota_bb(6.9, 7.1), 0.0)

    print("Maior de 3 valores:")
    test(maior3(3, 2, 1), 3)  # primeiro é o maior
    test(maior3(3, 1, 2), 3)  # primeiro é o maior
    test(maior3(1, 3, 2), 3)  # segundo é o maior
    test(maior3(2, 3, 1), 3)  # segundo é o maior
    test(maior3(1, 2, 3), 3)  # terceiro é o maior
    test(maior3(2, 1, 3), 3)  # terceiro é o maior
    test(maior3(1.01, 1.1, 1.02), 1.1)  # teste com números float
    test(maior3(0, -1, -2), 0)  # teste com zero e negativos
    test(maior3(-100, 0, 100), 100)  # teste com zero e negativos

    print("Menor de 3 valores:")
    test(menor3(3, 2, 1), 1)  # primeiro é o maior
    test(menor3(3, 1, 2), 1)  # primeiro é o maior
    test(menor3(1, 3, 2), 1)  # segundo é o maior
    test(menor3(2, 3, 1), 1)  # segundo é o maior
    test(menor3(1, 2, 3), 1)  # terceiro é o maior
    test(menor3(2, 1, 3), 1)  # terceiro é o maior
    test(menor3(1.01, 1.02, 1.1), 1.01)  # teste com números float
    test(menor3(0, -1, -2), -2)  # teste com zero e negativos
    test(menor3(-100, 0, 100), -100)  # teste com zero e negativos

    print("Triângulos:")
    test(testa_lados(7, 1, 2), "Não forma um triângulo")
    test(testa_lados(7, 2, 1), "Não forma um triângulo")
    test(testa_lados(1, 7, 2), "Não forma um triângulo")
    test(testa_lados(1, 2, 7), "Não forma um triângulo")
    test(testa_lados(2, 1, 7), "Não forma um triângulo")
    test(testa_lados(2, 7, 1), "Não forma um triângulo")
    test(testa_lados(2, 2, 2), "Triângulo equilátero")
    test(testa_lados(3, 3, 3), "Triângulo equilátero")
    test(testa_lados(2, 3, 4), "Triângulo escaleno")
    test(testa_lados(2, 4, 3), "Triângulo escaleno")
    test(testa_lados(3, 4, 2), "Triângulo escaleno")
    test(testa_lados(3, 2, 4), "Triângulo escaleno")
    test(testa_lados(2, 3, 3), "Triângulo isósceles")
    test(testa_lados(3, 2, 2), "Triângulo isósceles")
    test(testa_lados(3, 3, 2), "Triângulo isósceles")
    test(testa_lados(3, 2, 3), "Triângulo isósceles")

    print("Ano bissexto:")
    test(ano_bissexto(ano=1000), False)
    test(ano_bissexto(ano=1200), True)
    test(ano_bissexto(ano=1004), True)
    test(ano_bissexto(ano=1040), True)
    test(ano_bissexto(ano=2012), True)
    test(ano_bissexto(ano=2014), False)

    print("Maior dia do mês:")
    test(maior_dia_do_mes(mes=1, ano=2014), 31)
    test(maior_dia_do_mes(mes=3, ano=2014), 31)
    test(maior_dia_do_mes(mes=4, ano=2014), 30)
    test(maior_dia_do_mes(mes=5, ano=2014), 31)
    test(maior_dia_do_mes(mes=6, ano=2014), 30)
    test(maior_dia_do_mes(mes=7, ano=2014), 31)
    test(maior_dia_do_mes(mes=9, ano=2014), 30)
    test(maior_dia_do_mes(mes=10, ano=2014), 31)
    test(maior_dia_do_mes(mes=11, ano=2014), 30)
    test(maior_dia_do_mes(mes=12, ano=2014), 31)
    test(maior_dia_do_mes(mes=2, ano=2014), 28)
    test(maior_dia_do_mes(mes=2, ano=2016), 29)

    print("Valida datas:")
    test(data_valida(data="01/01/2014"), True)
    test(data_valida(data="31/01/2014"), True)
    test(data_valida(data="00/00/0000"), False)
    test(data_valida(data="30/04/2014"), True)
    test(data_valida(data="31/04/2014"), False)
    test(data_valida(data="30/09/2014"), True)
    test(data_valida(data="31/09/2014"), False)
    test(data_valida(data="30/06/2014"), True)
    test(data_valida(data="31/06/2014"), False)
    test(data_valida(data="30/11/2014"), True)
    test(data_valida(data="31/11/2014"), False)
    test(data_valida(data="32/01/2014"), False)
    test(data_valida(data="01/01/0000"), False)
    test(data_valida(data="01/13/2014"), False)
    test(data_valida(data="01/00/2014"), False)
    test(data_valida(data="29/02/2014"), False)
    test(data_valida(data="29/02/2016"), True)

    print("Delta:")
    test(delta(4, 4, 4), -48)  # delta menor que zero
    test(delta(1, 4, 4), 0)  # delta igual a zero, uma raiz
    test(delta(1, 5, 4), 9)  # delta maior que zero, duas raizes

    print("Báskara:")
    test(baskara(0, 4, 2), (-0.5,))  # a igual zero, equação de 1o grau
    test(baskara(4, 4, 4), ())  # delta menor que zero, sem raizes reais
    test(baskara(1, 4, 4), (-2.0,))  # delta igual a zero, uma raiz
    test(baskara(1, 5, 4), (-1.0, -4.0))  # delta maior que zero, duas raizes


if __name__ == "__main__":
    main()
    print(
        f"\n{total} Testes, {acertos} Ok, {total - acertos} Falhas: Nota {round(acertos * 100 / total)}"
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")