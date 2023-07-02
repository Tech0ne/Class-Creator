"""
lire et ouvrir un fichier .csv
"""

import csv

def lecture_fichier(fichier, nbr_entete, sep, encod):
    """
    fichier : nom du fichier qu'on veut ouvrir
    nbr_entete :  nombre de ligne d'en-tête, qu'on met dans une liste à part
        pour pas polluer (vu qu'on les traite pas)
    sep : caractère de séparation
    encod : encodage du fichier à ouvrir (logique)
    """
    f=open(fichier, "r", encoding=encod)
    contenu=csv.reader(f, delimiter=sep)
    liste_entete=[]
    liste_coprs=[]
    for ligne in contenu:
        if(len(liste_entete)<nbr_entete):
            liste_entete.append(ligne)
        else:
            liste_coprs.append(ligne)
    return liste_entete, liste_coprs
