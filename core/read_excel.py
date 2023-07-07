from .log import *
import pandas as pd

import os

def from_list_to_excel(classes: list):
    # classes : [
    #   [
    #       student_a: Student,
    #       student_b: Student,
    #       student_c: Student,
    #   ],
    #   [
    #       student_d: Student,
    #       student_e: Student,
    #       student_f: Student,
    #   ]
    # ]
    classes = [
        [student.full_name for student in classe] for classe in classes
    ]
    excel = pd.DataFrame(classes, columns=[f"Seconde {x + 1}" for x in range(len(classes))])
    excel.to_excel("classes.xlsx", sheet_name="Seconds", index=False)
