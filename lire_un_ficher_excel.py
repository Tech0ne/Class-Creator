import pandas as pd

def lecture_ficher_excel(filename):
    all_sheets = pd.read_excel(filename, sheet_name=None)
    total_list = {}
    for k, v in all_sheets.items():
        total_list[k] = {}
        for e in v:
            total_list[k][e] = []
            for n in v[e]:
                total_list[k][e].append(n)
    return total_list