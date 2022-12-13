from entiers import *
from non_entiers import *
from entiers_en_machine import *
from flottants_format_ieee_754 import *
from parametres import *


def saisir_nombre():
    """
    Vérifie si un nombre est bien dans la base donnée par l'utilisateur
    :return:
    Le nombre sous forme de liste, sa base, et sous sa forme entière
    """
    liste = []
    n_base = int(input("Veuillez saisir en chiffre la base de l'entier :"))
    if n_base == 16:
        Lettre = input("Veuillez saisir le nombre en héxadécimal")
        Lettre = list(Lettre)
        for i in range(len(Lettre)):
            if isinstance(Lettre[i],str):
                while Lettre[i] != "A" and Lettre[i] != "B" and Lettre[i] != "C" and Lettre[i] != "D" and Lettre[i] != "E" and Lettre[i] != "F" and Lettre[i] != "9" and Lettre[i] != "8" and Lettre[i] != "7" and Lettre[i] != "6" and Lettre[i] != "5" and Lettre[i] != "4" and Lettre[i] != "3" and Lettre[i] != "2" and Lettre[i] != "1" and Lettre[i] != "0":
                    Lettre[i] = str(input("Veuillez ressaisir seulement la/les lettre(s) correctes en majuscules"))
                Lettre[i] = SYMB_HEX_VERS_DEC[Lettre[i]]
        return Lettre,n_base
    else:
        Chiffre = int(input("Veuillez saisir l'entier choisi"))
        VS = abs(Chiffre)
        while VS > 0:
            Chiffre2 = VS % 10
            VS = VS // 10
            liste.append(Chiffre2)
        liste.reverse()
        if n_base == 2:
            while Chiffre % 10 != 0 and Chiffre % 10 != 1:
                Chiffre = int(input("Veuillez resaisir votre nombre en forme binaire"))
            return liste,n_base, Chiffre
        elif n_base == 10:
            while Chiffre % 10 != 0 and Chiffre % 10 != 1 and Chiffre % 10 != 2 and Chiffre % 10 != 3 and Chiffre % 10 != 4 and Chiffre % 10 != 5 and Chiffre % 10 != 6 and Chiffre % 10 != 7 and Chiffre % 10 != 8 and Chiffre % 10 != 9:
                Chiffre = input("Veuillez resaisir votre nombre en forme décimal")
            return liste, n_base, Chiffre
        elif n_base == 8:
            while Chiffre % 10 != 0 and Chiffre % 10 != 1 and Chiffre % 10 != 2 and Chiffre % 10 != 3 and Chiffre % 10 != 4 and Chiffre % 10 != 5 and Chiffre % 10 != 6 and Chiffre % 10 != 7:
                Chiffre = int(input("Veuillez resaisir votre nombre en forme octale"))
            return liste, n_base, Chiffre


def convertir():
    """
    Menu d'affichage pour toutes les fonctions
    :return:
    Les nombres convertis saisis par l'utilisateur
    """
    n = saisir_nombre()
    if n[1] == 2:
        print("""
        Voici la liste des convertions possibles en binaire : 
        1. bin -> dec
        2. bin -> hex
        3. bin -> chaine
        4. bin -> entier
        5. Addition binaire
        6. Fractionnaire_bin -> dec
        7. Addition binaire en machine
        8. bin -> dec en machine
        9. bin_signe -> dec
        10. compl2 -> dec
        11. ieee -> dec
        12. ieee -> format ieee
              """)
        numero = int(input())
        if numero == 1:
            print(bin_vers_dec(n[0]))
        elif numero == 2:
            print(bin_vers_hex(n[0]))
        elif numero == 3:
            print(bin_vers_chaine(n[0]))
        elif numero == 4:
            print(bin_vers_entier(n[0]))
        elif numero == 5:
            bin2 = int(input("Saisir un deuxième nombre binaire "))
            bin2 = list(bin2)
            print(addition_binaire(n[0],bin2))
        elif numero == 8:
            bin2 = int(input("Saisir un deuxième nombre binaire"))
            bin2 = list(bin2)
            p = int(input("Veuillez saisir un maximum de bits a ne pas franchir"))
            print(addition_binaire_machine(n[0], bin2,p))
        elif numero == 8:
            print(bin_vers_dec_machine(n[0]))
        elif numero == 9:
            print(bin_signe_vers_dec(n[0]))
        elif numero == 10:
            print(compl2_vers_dec(n[0]))

    elif saisir_nombre()[1] == 8 or saisir_nombre()[1] == 16:
        print("""
                Voici la liste des convertions possibles en octal et en héxadécimal : 
                1. oct -> dec
                2. hex -> dec
                3. hex -> bin
                4. hex -> chaine

                      """)
        numero = int(input())
        if numero == 1:
            print(oct_vers_dec(n[0]))
        elif numero == 2:
            print(hex_vers_dec(n[0]))
        elif numero == 3:
            print(hex_vers_bin(n[0]))
        elif numero == 4:
            print(hexa_vers_chaine(n[0]))
    elif n[1] == 10:
        print("""
                Voici la liste des convertions possibles en décimal : 
                1. dec -> bin
                2. dec -> oct
                3. dec -> hex
                4. fractionnaire_dec -> bin
                5. dec -> bin_signee
                6. dec -> compl2
                7. dec -> forme normalisee
                8. dec -> exposant
                9. dec -> mantisse
                10. dec -> ieee
                11. dec -> bin en machine
                Vérifications :
                11. est_représentable_dec -> bin
                12. est_représentable_dec -> bin_signe
                13. est_représentable_dec -> compl2
                      """)
        numero = int(input())
        if numero == 1:
            print(dec_vers_bin(n[2]))
        elif numero == 2:
            print(dec_vers_oct(n[2]))
        elif numero == 3:
            print(dec_vers_hex(n[3]))
        elif numero == 4:
            print(fractionnaire_dec_vers_bin(n[2]))
        elif numero == 5:
            p = int(input("Veuillez saisir un maximum de bits a ne pas franchir"))
            print(dec_vers_bin_signe(n[2],p))
        elif numero == 6:
            p = int(input("Veuillez saisir un maximum de bits a ne pas franchir"))
            print(dec_vers_comp2(n[2]),p)
        elif numero == 7:
            print(forme_normalisee(n[2]))
        elif numero == 8:
            print(exposant(n[2]))
        elif numero == 9:
            print(mantisse(n[2]))
        elif numero == 10:
            print(dec_vers_ieee(n[2]))
        elif numero == 11:
            p = int(input("Veuillez saisir un maximum de bits a ne pas franchir"))
            print(dec_vers_bin_machine(n[2],p))
        elif numero == 12:
            p = int(input("Veuillez saisir un maximum de bits a ne pas franchir"))
            print(est_representable_bin(n[2], p))
        elif numero == 13:
            p = int(input("Veuillez saisir un maximum de bits a ne pas franchir"))
            print(est_representable_signe(n[2], p))
        elif numero == 14:
            p = int(input("Veuillez saisir un maximum de bits a ne pas franchir"))
            print(est_representable_comp2(n[2], p))

convertir()

