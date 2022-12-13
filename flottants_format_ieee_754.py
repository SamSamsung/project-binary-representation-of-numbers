from non_entiers import *
from entiers_en_machine import *


def forme_normalisee(n):
    """
    Convertit un nombre entier quelconque en forme IEEE
    :param n:
    Nombre entier quelconque
    :return:
    La forme IEEE correspondante
    """
    m = []
    fract = fractionnaire_dec_vers_bin(n, 23)
    s = fract["signe"]
    e = len(fract["entiers"]) - 1
    for i in range(fract["entiers"][1], len(fract["entiers"])):
        m.append(fract["entiers"][i])
    for j in range(len(fract["fractionnaire"])):
        m.append(fract["fractionnaire"][j])
    return s, e, m


def exposant(n):
    """
    Convertit l'exposant en binaire
    :param n:
    Un nombre entier quelconque
    :return:
    L'exposant sous forme binaire
    """
    exp = forme_normalisee(n)[1]
    exp = exp + 127
    return dec_vers_bin_machine(exp, 8)


def mantisse(n):
    """
    Convertit la mantisse en binaire
    :param n:
    Un nombre entier quelconque
    :return:
    La mantisse sous forme binaire
    """
    mant = forme_normalisee(n)[2]
    while len(mant) < 23:
        mant.append(0)
    return mant


def signe(n):
    """
    Convertit le signe en binaire
    :param n:
    Un nombre entier quelconque
    :return:
    Le signe sous forme binaire
    """
    if n >= 0:
        return 0
    else:
        return 1


def dec_vers_ieee(n):
    """
    Convertit un nombre entier quelconque en dictionnaire IEEE
    :param n:
    Un nombre entier quelconque
    :return:
    Le dictionnaire sous forme binaire
    """
    return {"Signe":signe(n),"Exposant en excédent 127":exposant(n),"Mantisse sans le premier 1":mantisse(n)}


def ieee_vers_dec(n):
    """
    Convertit un dictionnaire IEEE en nombre entier
    :param n:
    Un dictionnaire sous forme binaire quelconque quelconque
    :return:
    Le nombre entier lui correspondant
    """
    p = []
    e = bin_vers_dec(n["Exposant en excédent 127"]) - 127
    m_ent = [1]
    m_fract = []
    for i in range(e):
        m_ent.append(n["Mantisse sans le premier 1"][i])
    m_ent = bin_vers_dec(m_ent)
    n["Mantisse sans le premier 1"].reverse()
    for j in range(23-e):
        m_fract.append(n["Mantisse sans le premier 1"][j])
    m = 0
    for l in range(len(m_fract)):
        a = m_fract[l] * 2 ** - (len(m_fract) - l)
        m += a
    return (-1)**n["Signe"]*(m_ent+m)


def afficher_ieee(IEEE):
    """
    Affiche la forme IEEE des nombres binaires
    :param IEEE:
    Nombres binaires
    :return:
    Nombres binaires affichés avec espaces
    """
    print(IEEE['Signe'], "|", end="")
    for i in range(len(IEEE['Exposant en excédent 127'])):
        print(IEEE['Exposant en excédent 127'][i], end="")
    print("|", end="")
    for i in range(len(IEEE['Mantisse sans le premier 1'])):
        print(IEEE['Mantisse sans le premier 1'][i],end="")
    print("|")


assert forme_normalisee(-100.25) == (1, 6, [1, 0, 0, 1, 0, 0, 0, 1])
assert not forme_normalisee(85) == (1,6,[1,0,1,0,1,0])

assert exposant(-100.25) == [1, 0, 0, 0, 0, 1, 0, 1]
assert not exposant(587) == [1,0,0,1,0,0]

assert mantisse(850) == [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert not mantisse(850) == [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

assert dec_vers_ieee(250) == {'Signe': 0, 'Exposant en excédent 127': [1, 0, 0, 0, 0, 1, 1, 0], 'Mantisse sans le premier 1': [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
assert dec_vers_ieee(-289.5) == {'Signe': 1, 'Exposant en excédent 127': [1, 0, 0, 0, 0, 1, 1, 1], 'Mantisse sans le premier 1': [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
assert not dec_vers_ieee(250) == {'Signe': 1, 'Exposant en excédent 127': [1, 0, 1, 0, 0, 0, 1, 0], 'Mantisse sans le premier 1': [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

assert ieee_vers_dec({'Signe': 1, 'Exposant en excédent 127': [1, 0, 0, 0, 0, 1, 0, 0], 'Mantisse sans le premier 1': [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]}) == -50.19999694824219
assert ieee_vers_dec({'Signe': 1, 'Exposant en excédent 127': [1, 0, 0, 0, 0, 1, 1, 1], 'Mantisse sans le premier 1': [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}) == -400.75
assert not ieee_vers_dec({'Signe': 1, 'Exposant en excédent 127': [1, 0, 0, 0, 0, 1, 0, 0], 'Mantisse sans le premier 1': [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]}) == -96.52

