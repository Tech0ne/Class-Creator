"""
EP, le 04.07.23
Création du type Student, puis des fonctions pour transformer ce qu'on tire
du fichier csv en type Student.
"""

class Student(object):
    def __init__(self, valeur_nom, valeur_prenom, valeur_lv1, valeur_lv2,
                 valeur_etablissement, valeur_scolarite):
        """
        nom :
        """
        self.nom = valeur_nom
        self.prenom=valeur_prenom
        self.lv1=valeur_lv1
        self.lv2=valeur_lv2
        self.etablissement=valeur_etablissement
        self.scolarite=valeur_scolarite

def affiche_student(stud):
    """
    avec stud qui est de type Student
    """
    print(stud.nom, stud.prenom, stud.lv1, stud.lv2, stud.etablissement,
          stud.scolarite)

def transforme_en_student(liste):
    """
    avec une liste des caractéristiques du type Student (dans l'ordre)
    et le résultat est de type Student.
    """
    stud=Student(liste[0],liste[1],liste[2],liste[3],liste[4],liste[5])
    return stud


# test = un exemple de ce qui ressort de la fontion lecture_fichier
# avec des espaces vides pour les infos qu'on a pas encore).

test=['ACS;Lylou;AGL1;ESP2;PAUL ARENE;oui;non;non;non;non;non;non;;;;']
test2=test[0].split(";")
affiche_student(transforme_en_student(test2))
