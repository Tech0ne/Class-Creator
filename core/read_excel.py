from .log import *
import openpyxl

def read_excel_file(path):
    try:
        excel_obj = openpyxl.load_workbook(path)
    except Exception as e:
        fatal("An error occured :", str(e))
    sheet_obj = excel_obj.active
    cell_obj = sheet_obj.cell(row=9, column=4)
    print(cell_obj.value)