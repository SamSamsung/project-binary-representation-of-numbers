from parametres import *


def afficher_binaire(n, espace = 4):
    n = str(n)[::-1]
    itterator = 1
    result = ""
    for i in n:
        result += i
        if itterator % espace == 0:
            result += " "
        itterator += 1
    return result[::-1]


def bin_vers_dec(L):
    """
    Convertit un nombre binaire en décimal
    :param L:
    La liste contenant les chiffres binaires
    :return:
    L'entier correspondant a la liste en décimal
    """
    dec = 0
    for i in range(len(L)):
        a = L[i] * 2 ** (len(L)-i)//2
        dec += a
    return dec


def dec_vers_bin(n):
    """
    Convertit un nombre décimal en binaire
    :param n:
    Un entier quelconque en décimal
    :return:
    La liste contenant les chiffres binaires correspondant à l'entier
    """
    n = abs(n)
    L = []
    q = 1
    while q != 0:
        q = n // 2
        bits = n % 2
        n = q
        L.append(bits)
    L.reverse()
    return L


def oct_vers_dec(L):
    """
    Convertit un nombre octal en décimal
    :param L:
    La liste contenant les chiffres octaux
    :return:
    Un entier en décimal correspondant à la liste
    """
    b = 0
    for i in range(len(L)):
        a = L[i] * 8 ** (len(L) - i) // 8
        b += a
    return b


def dec_vers_oct(n):
    """
    Convertit un nombre décimal en octal
    :param n:
    Un entier en décimal quelconque
    :return:
    La liste contenant les chiffres octaux correspondant à l'entier
    """
    q = 1
    L = []
    while q != 0:
        q = n // 8
        r = n % 8
        n = q
        L.append(r)
    L.reverse()
    return L


def hex_vers_dec(L):
    """
    Convertit un nombre hexadécimal en décimal
    :param L:
    La liste contenant les chiffres héxadécimaux
    :return:
    Un entier en décimal correspondant à la liste
    """
    for i in range(len(L)):
        L[i] = SYMB_HEX_VERS_DEC[L[i]]
    b = 0
    for i in range(len(L)):
        a = L[i] * 16 ** (len(L) - i) // 16
        b += a
    return b


def dec_vers_hex(n):
    """
    Convertit un nombre décimal en héxadécimal
    :param n:
    Un nombre décimal quelconque
    :return:
    La liste contenant les chiffres héxadécimaux correspondant à l'entier
    """
    q = 1
    L = []
    while q != 0:
        q = n // 16
        r = n % 16
        n = q
        if r >= 10:
            r = SYMB_DEC_VERS_HEX[r]
        L.append(r)
    L.reverse()

    return L


def bin_vers_hex(L) :
    """
    Convertit un nombre binaire en héxadécimal
    :param L:
    Une liste contenant des chiffres binaire quelconques
    :return:
    La liste contenant les chiffres héxadécimaux correspondant à la liste
    """
    n = bin_vers_dec(L)
    return dec_vers_hex(n)


def hex_vers_bin(L) :
    """
    Convertit un nombre héxadécimal en binaire
    :param L:
    Une liste contenant des chiffres héxadécimaux quelconques
    :return:
    La liste contenant les ciffres binaires correspondant à la liste
    """
    dec = hex_vers_dec(L)
    return dec_vers_bin(dec)


def bin_vers_chaine(L) :
    """
    Convertit un nombre binaire dans une chaine de caractères
    :param L:
    Une liste contenant des chiffres binaires quelconques
    :return:
    La liste contenant les ciffres binaires correspondant à la liste sous la forme d'une chaine de caractères
    """
    result = ""
    for bit in(L) :
        result += str(bit)
    return result


def bin_vers_entier(L) :
    """
    Convertit un nombre binaire dans sa représentation en entier décimal n'ayant que des 0 et des 1
    :param L:
    Une liste contenant des chiffres binaires quelconques
    :return:
    La liste contenant les ciffres binaires correspondant à la liste en représentation décimal (avec des 0 et des 1)
    """
    return int(bin_vers_chaine(L))


def hexa_vers_chaine(L) :
    """
    Convertit un nombre héxadécimal dans une chaine de caractère
    :param L:
    Une liste contenant des chiffres héxadécimaux quelconques
    :return:
    La liste contenant les ciffres héxadécimaux correspondant à la liste sous la forme d'une chaine de caractères
    """
    result = ""
    for c_h in(L) :
        result += str(c_h)
    return result


def addition_binaire(L1, L2) :
    """
    Additione deux listes en binaire
    :param L1:
    La première liste
    :param L2:
    La deuxième liste
    :return:
    L'additon de ces deux listes
    """
    somme = []
    L1.reverse()
    L2.reverse()
    while len(L1) != len(L2) :
        if len(L1) > len(L2) :
            L2.append(0)
        else :
            L1.append(0)
    L1.append(0)
    L2.append(0)
    for i in range(len(L1)) :
        if L1[i] + L2[i] == 0 :
            somme.append(0)
        elif L1[i] + L2[i] == 1 :
            somme.append(1)
        elif L1[i] + L2[i] == 2 :
            somme.append(0)
            L1[i + 1] = L1[i + 1] + 1
        elif L1[i] + L2[i] == 3 :
            somme.append(1)
            L1[i + 1] = L1[i + 1] + 1
    somme.reverse()
    return somme


assert afficher_binaire(101101011) == str("1 0110 1011")
assert not afficher_binaire(1001011001) == str("100 110 1010")

assert bin_vers_dec([1, 1, 1]) == 7
assert not bin_vers_dec([1, 1, 0]) == 8

assert dec_vers_bin(7) == [1, 1, 1]
assert not dec_vers_bin(8) == [1, 1, 0]

assert oct_vers_dec([1, 2, 5]) == 85
assert not oct_vers_dec([3, 4, 2]) == 26

assert dec_vers_oct(85) == [1, 2, 5]
assert not dec_vers_oct(26) == [3, 4, 2]

assert hex_vers_dec([9, 2, 8]) == 2344
assert not hex_vers_dec([7, 5, 1]) == 1475

assert dec_vers_hex(2344) == [9, 2, 8]
assert not dec_vers_hex(1475) == [7, 5, 1]

assert bin_vers_hex([1, 1, 0, 1, 1, 1]) == [3, 7]
assert not bin_vers_hex([1, 0, 1, 1, 0]) == [2, 4]

assert hex_vers_bin([3, 7]) == [1, 1, 0, 1, 1, 1]
assert not hex_vers_bin([2, 4]) == [1, 0, 1, 1, 0]

assert bin_vers_chaine([1, 0, 0, 0, 1]) == str(10001)                    # sous la forme d'une chaîne de caractères
assert not bin_vers_chaine([1, 0, 1, 1, 0]) == 1010101

assert bin_vers_entier([1, 0, 1, 0, 1, 1]) == 101011             # sous la forme d'un entier
assert not bin_vers_entier([1, 0, 0, 1, 0, 1]) == 101110       

assert hexa_vers_chaine([4, 2, 7]) == str(427)                        # sous la forme d'une chaîne de caractères
assert not hexa_vers_chaine([8, 5, 3]) == 279                

assert addition_binaire([1, 1, 0, 1, 0], [1, 0, 0, 1, 1, 1]) == [1, 0, 0, 0, 0, 0, 1]
assert not addition_binaire([1, 0, 1, 0, 0, 1], [1, 1, 0, 1, 1]) == [1, 0, 1, 1]