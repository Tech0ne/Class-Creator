from core import *
from lire_un_ficher_excel import *

excelfile = lecture_ficher_excel("data.xlsx")
__import__("pickle").dump(excelfile, open("excel_but_not_excel.pkl", 'wb+'))

# excel_file = read_excel_file("/home/clementp/Téléchargements/classes.xlsx")
student = Student("Dupont", "Jean", "g", "Cateperdrix", 1, 3, 2, 1, 0, 0, "Espagnole", "", "", [], [], "")

# webapp_run()
