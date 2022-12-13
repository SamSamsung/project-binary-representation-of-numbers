from entiers import *


def est_representable_bin(n, b) :
    """
    Vérifie si l'entier n est représentable en binaire sur b bits
    :param n:
    Un nombre entier quelconque
    :param b:
    Un nombre de bits
    :return:
    Vrai si la représentation en binaire du nombre est inférieur à b bits
    Et Faux si la représentation en binaire du nombre est supérieur à b bits
    """
    L = dec_vers_bin(n)
    return len(L) <= b


def est_representable_signe(n, b) :
    """
    Vérifie si l'entier n est représentable en binaire signé sur b bits
    :param n:
    Un nombre entier relatif quelconque
    :param b:
    Un nombre de bits
    :return:
    Vrai si la représentation en binaire signé du nombre est inférieur à b bits
    Et Faux si la représentation en binaire signé du nombre est supérieur à b bits
    """
    L = dec_vers_bin(n)
    return len(L) + 1 <= b


def est_representable_comp2(n, b) :
    """
    Vérifie si l'entier n est représentable en complément à deux sur b bits
    :param n:
    Un nombre entier relatif quelconque
    :param b:
    Un nombre de bits
    :return:
    Vrai si la représentation en complément à deux du nombre est inférieur à b bits
    Et Faux si la représentation en complément à deux du nombre est supérieur à b bits
    """
    L = dec_vers_bin_machine(n, b)
    if n < 0:
        L = compl1(L)
        L = addition_binaire(L, [1])
    return len(L) <= b


def addition_binaire_machine(L1, L2, b) :
    """
    Additionne deux listes sur un maximum de b bits
    :param L1:
    Une liste de chiffres binaires quelconques
    :param L2:
    Une deuxième liste de chiffres binaires quelconques
    :param b:
    Un nombre de bits
    :return:
    Le résultat de l'addition sur b bits
    """
    L = addition_binaire(L1, L2)
    while len(L) < b:
        L.reverse()
        L.append(0)
        L.reverse()
    if len(L) > b :
        L3 = []
        for j in range(b) :
            L3.append(L[j])
        return L3
    return L


def dec_vers_bin_machine(n, b) :
    """
    Convertit un nombre décimal en binaire sur b bits
    :param n:
    Un nombre décimal quelconque
    :param b:
    Un nombre de bits
    :return:
    Une liste contenant des chiffres binaires avec un maximum de b bits
    """
    L = dec_vers_bin(n)
    L.reverse()
    while len(L) < b :
        L.append(0)
    L.reverse()
    return L


def bin_vers_dec_machine(L) :
    """
    Convertit un nombre binaire en décimal
    :param L:
    Une liste contenant des chiffres binaires quelconques
    :return:
    Le nombre entier décimal correspondant à la liste
    """
    L = bin_vers_dec(L)
    return L


def dec_vers_bin_signe(n, b) :
    """
    Convertit un nombre décimal en nombre binaire signé
    :param n:
    Un nombre décimal quelconque
    :param b:
    Un nombre de bits
    :return:
     Une liste contenant des chiffres binaires signés avec un maximum de b bits
    """
    L = dec_vers_bin(abs(n))
    L.reverse()
    while len(L) + 1 < b :
        L.append(0)
    if n >= 0 :
        L.append(0)
    else :
        L.append(1)
    L.reverse()
    return L


def bin_signe_vers_dec(L) :
    """
    Convertit un nombre binaire signé en décimal
    :param L:
    La liste des chiffres binaires signés
    :return:
    Le nombre entier en décimal correspondant à la liste
    """
    if L[0] == 0 :
        dec = bin_vers_dec(L)
    else : 
        dec = bin_vers_dec(L)
        dec = 0 - dec
    return dec
    
    
def compl1(L) :
    # fonction en plus pour faire le complément à 1
    for i in range(len(L)) :
        if L[i] == 0 :
            L[i] = 1
        else :
            L[i] = 0
    return L


def dec_vers_comp2 (n, b) :
    """
    Convertit un nombre décimal en complément à deux sur un nombre maximum de b bits
    :param n:
    :param b:
    :return:
    """
    L = dec_vers_bin_machine(n, b)
    if n < 0 :
        L = compl1(L)
        L = addition_binaire(L, [1])
    if len(L) > b :
        L1 = []
        for i in range (b) :
            L1.append(L[i])
        L1.reverse()
        return L1
    return L


def compl2_vers_dec (L) :
    """
    Convertit un nombre binaire en compl2 en dec
    :param L:
    Liste binaire en complément à 2
    :return:
    Son entier correspondant
    """
    if L[0] == 0:
        dec = bin_vers_dec(L)
    else :
        L = compl1(L)
        L = addition_binaire(L, [1])
        dec = bin_vers_dec(L)
        dec = 0 - dec
    return dec


assert compl1([1,0,0,1]) == [0,1,1,0]
assert not compl1([1,0,0,1]) == [1,1,1,1,1,1,1,1]

assert est_representable_bin(7, 5)
assert not est_representable_bin(53, 2)

assert est_representable_signe(24, 8)
assert not est_representable_signe(15, 4)

assert est_representable_comp2(38, 20)
assert not est_representable_comp2(526, 3)

assert addition_binaire_machine([1, 0, 1, 1, 0], [1, 1, 0, 0, 0, 1, 1], 8) == [0, 1, 1, 1, 1, 0, 0, 1]
assert not addition_binaire_machine([1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 1, 1], 6) == [1, 1, 1, 0, 1]

assert dec_vers_bin_machine(83, 9) == [0,0,1, 0, 1, 0, 0, 1, 1]
assert not dec_vers_bin_machine(74, 4) == [1, 0, 0, 0, 1, 1]

assert bin_vers_dec_machine([1, 1, 0, 1, 1, 0]) == 54
assert not bin_vers_dec_machine([1, 0, 1, 1, 0]) == 67

assert dec_vers_bin_signe(29, 8) == [0, 0, 0, 1, 1, 1, 0, 1]
assert not dec_vers_bin_signe(-7, 5) == [0, 0, 1, 1, 1]

assert bin_signe_vers_dec([0, 1, 0, 1, 1, 1, 1, 1]) == 95
assert not bin_signe_vers_dec([0, 1, 1, 0, 0, 0]) == -24

assert dec_vers_comp2(-2, 5) == [1, 1, 1, 1, 0]
assert not dec_vers_comp2(7, 6) == [1, 1, 0]

assert compl2_vers_dec([1, 1, 1, 1, 1, 1, 1, 1]) == -1
assert not compl2_vers_dec([1, 0, 1]) == 0