from entiers import *


def fractionnaire_dec_vers_bin(n, p) :
    """
    Convertit un nombre décimal (à virgule) en binaire
    :param n:
    Un entier en décimal (à virgule)
    :param p:
    le nombre de bits maximum après la virgule
    :return:
    Un dictionnaire avec le signe, la partie entière et la partie fractionnaire
    """
    L = []
    if n < 0:
        signe = 1
    else:
        signe = 0
    n = abs(n)
    ent = dec_vers_bin(int(n))
    dec = n - int(n)
    cpt = 0
    if dec == 0:
        return ({"signe": signe, "entiers": ent, "fractionnaire": L})
    while dec != 1 and cpt < p:
        fract = dec * 2
        if fract < 1:
            L.append(0)
        elif fract > 1:
            L.append(1)
        else:
            L.append(1)
            return ({"signe": signe,"entiers":ent,"fractionnaire":L})
        if len(L) == p:
            return ({"signe": signe, "entiers": ent, "fractionnaire": L})
        dec = fract - int(fract)
        cpt += 1


def fractionnaire_bin_vers_dec(n):
    """
    Convertit un nombre binaire décimal (avec virgule) en décimal (base 10)
    :param n:
    Le dictionnaire contenant le signe, la partie entière et la partie fractionnaire
    :return:
    """
    ent = bin_vers_dec(n['entiers'])
    dec = 0
    for i in range(len(n['fractionnaire'])):
        a = n['fractionnaire'][i] * 2 ** - (len(n['fractionnaire'])-i)/2
        dec += a
    return ent + dec


assert fractionnaire_dec_vers_bin(10.1,8) == {'signe': 0, 'entiers': [1, 0, 1, 0], 'fractionnaire': [0, 0, 0, 1, 1, 0, 0, 1]}
assert not fractionnaire_dec_vers_bin(15.8,9) == {'signe': 0, 'entiers': [1, 0, 1, 0], 'fractionnaire': [0, 0, 0, 1, 1, 0, 0, 1]}

assert fractionnaire_bin_vers_dec({'entiers':[1,1], 'fractionnaire':[0,1,1]}) == 3.375
assert not fractionnaire_bin_vers_dec({'entiers':[1,1], 'fractionnaire':[0,1,1]}) == 45

