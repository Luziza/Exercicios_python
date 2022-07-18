# Marco André <marcoandre@gmail.com>
# Lista de exercícios de Fixação 5a

# Nessa lista você pode resolver os problemas utilizando o que você preferir:
# if, else, elif, for, while, métodos da lista e string, métodos embutidos no Python.

# Tente usar if ternário e outras formas de resolver com menos linhas de código.

# O objetivo é fixar todo o conteúdo já visto e desenvolver a lógica e o
# raciocínio com problemas novos.


def dormir(dia_semana, feriado):
    """
    dia_semana é True para dias na semana
    feriado é True nos feriados
    você pode ficar dormindo quando é feriado ou não é dia semana
    retorne True ou False conforme você vá dormir ou não
    """

    if dia_semana == False and feriado == False:
        return True
    elif dia_semana == True and feriado == False:
        return False
    elif dia_semana == False and feriado == True:
        return True
    elif dia_semana == True and feriado == True:
        return True       


def alunos_problema(a_sorri, b_sorri):
    """
    temos dois alunos a e b
    a_sorri e b_sorri indicam se a e b sorriem
    temos problemas quando ambos estão sorrindo ou ambos não estão sorrindo
    retorne True quando houver problemas
    """

    if a_sorri == True and b_sorri == True or a_sorri == False and b_sorri == False:
        return True
    else: 
        return False


def soma_dobro(a, b):
    """
    dados dois números inteiros retorna sua soma
    porém se os números forem iguais retorna o dobro da soma
    soma_dobro(1, 2) -> 3
    soma_dobro(2, 2) -> 8
    """

    if a != b:
        return a + b
    elif a == b:
        return (a + b) * 2


def diff21(n):
    """
    dado um inteiro n retorna a diferença absoluta entre n e 21
    porém se o número for maior que 21 retorna o dobro da diferença absoluta
    diff21(19) -> 2
    diff21(25) -> 8
    dica: abs(x) retorna o valor absoluto de x
    """

    diferenca = 21 - n
    if n < 21:
        return diferenca
    else:
        return abs(diferenca * 2)


def papagaio(falando, hora):
    """
    temos um papagaio que fala alto
    hora é um parâmetro entre 0 e 23
    temos problemas se o papagaio estiver falando antes da 7 ou depois das 20
    """

    if falando == True and hora < 7 or falando == True and hora > 20:
        return True
    else:
        return False



def dez(a, b):
    """
    dados dois inteiros a e b
    retorna True se um dos dois é 10 ou a soma é 10
    """

    if a == 10 or b == 10 or a + b == 10:
        return True
    else: 
        return False


def dista10(n):
    """
    seja um inteiro n
    retorna True se a diferença absoluta entre n e 100 ou n e 200
    for menor ou igual a 10
    dista10(93) -> True
    dista10(90) -> True
    dista10(89) -> False
    """

    if abs(100 - n) <= 10 or abs(200 - n) <= 10:
        return True
    else:
        return False

def apaga(s, n):
    """
    seja uma string s e um inteiro n
    retorna uma nova string sem a posição n
    apaga('kitten', 1) -> 'ktten'
    apaga('kitten', 4) -> 'kittn'
    """

    return s[:n] + s[n + 1:]


def troca(s):
    """
    seja uma string s
    se s tiver tamanho <= 1 retorna ela mesma
    caso contrário troca a primeira e última letra
    troca('code') -> 'eodc'
    troca('a') -> 'a'
    troca('ab') -> 'ba'
    """

    if len(s) <= 1:
        return s
    else:
        final = len(s)
        meio = s[1: final - 1]
        return s[-1] + meio + s[0]


def multi_string(s, n):
    """
    Seja uma string s e um inteiro positivo n
    retorna uma string com n cópias da string original
    multi_string('Oi', 2) -> 'OiOi'
    """

    return (s * n)


def explode_string(s):
    """
    explode_string('Code') -> 'CCoCodCode'
    explode_string('abc') -> 'aababc'
    explode_string('ab') -> 'aab'
    """
    ia = 0
    tamanho = len(s)
    palavra = ''
    for i in range(tamanho):
        palavra += s[:ia + 1]
        ia += 1
    return palavra


def conta_noves(nums):
    """Conta quantas vezes aparece o 9 numa lista nums."""

    return nums.count(9)


def nove_na_frente(nums):
    """
    verifica se pelo menos um dos quatro primeiros itens é nove
    nove_na_frente([1, 2, 9, 3, 4]) -> True
    nove_na_frente([1, 2, 3, 4, 9]) -> False
    nove_na_frente([1, 2, 3, 4, 5]) -> False
    """
    
    return 9 in nums[:4]


def alo_nome(nome):
    """
    Seja uma string nome
    alo_nome('Bob') -> 'Alô Bob!'
    alo_nome('Alice') -> 'Alô Alice!'
    alo_nome('X') -> 'Alô X!'
    """

    return "Alô " + nome + "!"


def cria_tags(tag, palavra):
    """
    cria_tags('i', 'Uhul'), '<i>Uhul</i>'
    cria_tags('i', 'Alô'), '<i>Alô</i>'
    cria_tags('cite', 'Uhul'), '<cite>Uhul</cite>'
    """
    return "<" + tag + ">" + palavra + "</" + tag + ">"


def final_extra(s):
    """
    Seja um string s com no mínimo duas letras,
    retorna três vezes as duas últimas letras.
    final_extra('Alô'), 'lololo'
    final_extra('ab'), 'ababab'
    final_extra('Oi'), 'OiOiOi'
    """

    if len(s) >= 2:
        penultimo = len(s) - 2
        return s[penultimo:] * 3


def primeira_metade(s):
    """
    Seja uma string s, retorna a primeira metade da string
    primeira_metade('papagaio') -> 'papa'
    primeira_metade('Lula') -> 'Lu'
    primeira_metade('abcdef') -> 'abc'
    """

    metade = round(len(s) / 2)
    return s[0 :metade]


def sem_pontas(s):
    """
    Seja uma string s de pelo menos dois caracteres,
    retorna uma string sem o primeiro e último caracter.
    sem_pontas('Beleza') -> 'elez'
    sem_pontas('Python') -> 'ytho'
    sem_pontas('codigo') -> 'odig'
    """

    tamanho = len(s)
    return s[1: tamanho - 1]




def gira_esquerda_2(s):
    """
    Rodar à esquerda uma string s duas posições
    a string possui pelo menos 2 caracteres
    gira_esquerda_2('Beleza') -> 'lezaBe'
    gira_esquerda_2('Oi') -> 'Oi'
    """

    tamanho = len(s)
    return s[2: tamanho - 0] + s[:2]


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
    print("Oba! Hoje vou ficar dormindo!")
    test(dormir(False, False), True)
    test(dormir(True, False), False)
    test(dormir(False, True), True)
    test(dormir(True, True), True)

    print()
    print("Alunos problema")
    test(alunos_problema(True, True), True)
    test(alunos_problema(False, False), True)
    test(alunos_problema(True, False), False)
    test(alunos_problema(False, True), False)

    print()
    print("Soma dobro")
    test(soma_dobro(1, 2), 3)
    test(soma_dobro(3, 2), 5)
    test(soma_dobro(2, 2), 8)
    test(soma_dobro(-1, 0), -1)
    test(soma_dobro(0, 0), 0)
    test(soma_dobro(0, 1), 1)

    print()
    print("Diff21")
    test(diff21(19), 2)
    test(diff21(10), 11)
    test(diff21(21), 0)
    test(diff21(22), 2)
    test(diff21(25), 8)
    test(diff21(30), 18)

    print()
    print("Papagaio")
    test(papagaio(True, 6), True)
    test(papagaio(True, 7), False)
    test(papagaio(False, 6), False)
    test(papagaio(True, 21), True)
    test(papagaio(False, 21), False)
    test(papagaio(True, 23), True)
    test(papagaio(True, 20), False)

    print()
    print("Dez")
    test(dez(9, 10), True)
    test(dez(9, 9), False)
    test(dez(1, 9), True)
    test(dez(10, 1), True)
    test(dez(10, 10), True)
    test(dez(8, 2), True)
    test(dez(8, 3), False)
    test(dez(10, 42), True)
    test(dez(12, -2), True)

    print()
    print("Dista 10")
    test(dista10(93), True)
    test(dista10(90), True)
    test(dista10(89), False)
    test(dista10(110), True)
    test(dista10(111), False)
    test(dista10(121), False)
    test(dista10(0), False)
    test(dista10(5), False)
    test(dista10(191), True)
    test(dista10(189), False)
    test(dista10(190), True)
    test(dista10(200), True)
    test(dista10(210), True)
    test(dista10(211), False)
    test(dista10(290), False)

    print()
    print("Apaga")
    test(apaga("Hi", 0), "i")
    test(apaga("Hi", 1), "H")
    test(apaga("code", 0), "ode")
    test(apaga("code", 1), "cde")
    test(apaga("code", 2), "coe")
    test(apaga("code", 3), "cod")
    test(apaga("chocolate", 8), "chocolat")
    test(apaga("kitten", 1), "ktten")
    test(apaga("kitten", 0), "itten")
    test(apaga("kitten", 2), "kiten")
    test(apaga("tkitten", 3), "tkiten")

    print()
    print("Troca letras")
    test(troca("code"), "eodc")
    test(troca("a"), "a")
    test(troca("ab"), "ba")
    test(troca("abc"), "cba")
    test(troca(""), "")
    test(troca("Chocolate"), "ehocolatC")
    test(troca("nythoP"), "Python")
    test(troca("hello"), "oellh")

    print("Multi String")
    test(multi_string("Oi", 2), "OiOi")
    test(multi_string("Oi", 3), "OiOiOi")
    test(multi_string("Oi", 1), "Oi")
    test(multi_string("Oi", 0), "")
    test(multi_string("Oi", 5), "OiOiOiOiOi")
    test(multi_string("Oh Boy!", 2), "Oh Boy!Oh Boy!")
    test(multi_string("x", 4), "xxxx")
    test(multi_string("", 4), "")
    test(multi_string("code", 2), "codecode")
    test(multi_string("code", 3), "codecodecode")

    print("Explode string")
    test(explode_string("abc"), "aababc")
    test(explode_string("ab"), "aab")
    test(explode_string("x"), "x")
    test(explode_string("aqui"), "aaqaquaqui")
    test(explode_string("decai"), "ddedecdecadecai")
    test(explode_string("Beleza"), "BBeBelBeleBelezBeleza")
    test(explode_string("gago"), "ggagaggago")

    print("Conta noves")
    test(conta_noves([1, 99, 9]), 1)
    test(conta_noves([1, 9, 9]), 2)
    test(conta_noves([1, 9, 9, 3, 9]), 3)
    test(conta_noves([1, 2, 3]), 0)
    test(conta_noves([]), 0)
    test(conta_noves([4, 2, 4, 3, 1]), 0)
    test(conta_noves([9, 2, 99, 3, 1]), 1)

    print("Nove na frente")
    test(nove_na_frente([1, 2, 9, 3, 4]), True)
    test(nove_na_frente([1, 2, 3, 4, 9]), False)
    test(nove_na_frente([1, 2, 3, 4, 5]), False)
    test(nove_na_frente([9, 2, 3]), True)
    test(nove_na_frente([1, 9, 9]), True)
    test(nove_na_frente([1, 2, 3]), False)
    test(nove_na_frente([1, 9]), True)
    test(nove_na_frente([5, 5]), False)
    test(nove_na_frente([2]), False)
    test(nove_na_frente([9]), True)
    test(nove_na_frente([]), False)
    test(nove_na_frente([3, 9, 2, 3, 3]), True)

    print("Alô nome")
    test(alo_nome("Bob"), "Alô Bob!")
    test(alo_nome("Alice"), "Alô Alice!")
    test(alo_nome("X"), "Alô X!")
    test(alo_nome("Alô"), "Alô Alô!")

    print("Cria Tags")
    test(cria_tags("i", "Uhul"), "<i>Uhul</i>")
    test(cria_tags("i", "Alô"), "<i>Alô</i>")
    test(cria_tags("cite", "Uhul"), "<cite>Uhul</cite>")
    test(cria_tags("address", "aqui"), "<address>aqui</address>")
    test(cria_tags("body", "Coração"), "<body>Coração</body>")
    test(cria_tags("i", "i"), "<i>i</i>")
    test(cria_tags("i", ""), "<i></i>")

    print("Final extra")
    test(final_extra("Alô"), "lôlôlô")
    test(final_extra("ab"), "ababab")
    test(final_extra("Oi"), "OiOiOi")
    test(final_extra("Doce"), "cecece")
    test(final_extra("Beleza"), "zazaza")

    print("Primeira metade")
    test(primeira_metade("papagaio"), "papa")
    test(primeira_metade("Lula"), "Lu")
    test(primeira_metade("abcdef"), "abc")
    test(primeira_metade("ab"), "a")
    test(primeira_metade(""), "")
    test(primeira_metade("0123456789"), "01234")
    test(primeira_metade("buraco"), "bur")
    test(primeira_metade("joinville"), "join")

    print("Sem Pontas")
    test(sem_pontas("Beleza"), "elez")
    test(sem_pontas("Python"), "ytho")
    test(sem_pontas("codigo"), "odig")
    test(sem_pontas("sala"), "al")
    test(sem_pontas("ab"), "")
    test(sem_pontas("Chocolate!"), "hocolate")
    test(sem_pontas("cozinha"), "ozinh")
    test(sem_pontas("Uhull"), "hul")

    print("Gira Esquerda 2")
    test(gira_esquerda_2("Beleza"), "lezaBe")
    test(gira_esquerda_2("python"), "thonpy")
    test(gira_esquerda_2("Oi"), "Oi")
    test(gira_esquerda_2("code"), "deco")
    test(gira_esquerda_2("tio"), "oti")
    test(gira_esquerda_2("12345"), "34512")
    test(gira_esquerda_2("Chocolate"), "ocolateCh")
    test(gira_esquerda_2("tijolo"), "joloti")


if __name__ == "__main__":
    main()
    print(
        f"\n{total} Testes, {acertos} Ok, {total - acertos} Falhas: Nota {round(acertos * 100 / total)}"
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")