from flask      import Flask, request, abort, send_file
from pickle     import loads as ploads
from json       import loads as jloads
from os         import remove, system
from datetime   import datetime
from os.path    import isfile
from time       import time

import pandas as pd
import requests
import random
import sys

SEED = int(time())
random.seed

#region logging

def log(*data, pre='', end='\n'):
    print(pre, end='')
    print(datetime.now().strftime("[%Y-%m-%d %H:%M:%S]"), *data, end='')
    print(end=end)

def debug(*data):
    data = ("DEBUG : \33[2m", *data)
    log(*data)

def info(*data):
    data = ("INFO : ", *data)
    log(*data)

def warning(*data):
    data = ("WARNING : \33[93m", *data)
    log(*data)

def error(*data):
    data = ("ERROR : \33[91m", *data)
    log(*data)

def fatal(*data, error_code=1):
    data = ("FATAL ERROR : \33[91m", *data)
    log(*data, pre="/!\\", end="/!\\\n")
    sys.exit(error_code)

#endregion

def weighted_choice(values: list):
    # need to be a list of dict like :
    # [
    #   {
    #     "obj": anything (the actual thing to be chosen)
    #     "val": int -> the weight
    #   }
    # ]
    total_weight = sum([int(v["val"]) for v in values])
    chosen_value = random.randint(0, total_weight)
    curent_value = 0
    for obj in values:
        curent_value += obj["val"]
        if curent_value >= chosen_value:
            return obj["obj"]
    return values[values.keys()[-1]]["obj"]

def from_list_to_excel(classes: list):
    classes = [
        [student.full_name for student in classe] for classe in classes
    ]
    excel = pd.DataFrame(classes, columns=[f"Seconde {x + 1}" for x in range(len(classes))])
    excel.to_excel("classes.xlsx", sheet_name="Seconds", index=False)

def process_content(raw_content):
    try:
        return jloads(raw_content)
    except:
        pass
    try:
        return ploads(raw_content)
    except:
        fatal("Could not read input data !")

def sort_students(content, dispo):
    # the actual algo
    return None

class Student(object):
    def __init__(self, name: str, first_name: str, sex: str, lv2: str, origin: str, doubling: bool, is_good: bool, why_not: list, pap: bool, pps: bool, pai: bool, option1: str, option2: str, wanna_be_with: list):
        self.name           = name
        self.first_name     = first_name
        self.id             = f"{name.upper()}.{first_name.capitalize()}"
        self.sex            = sex
        if self.sex.lower() not in ('gf'):
            fatal("Invalid sex value")
        self.lv2            = lv2
        self.origin         = origin
        self.repeat         = doubling
        self.is_good        = is_good
        self.why_not        = why_not
        self.pap            = pap
        self.pps            = pps
        self.pai            = pai
        self.option1        = option1
        self.option2        = option2
        self.wanna_be_with  = wanna_be_with

    def __repr__(self) -> str:
        return  f"\n{self.id.replace('.', ' ')}, a {'girl' if self.sex == 'g' else 'boy'} comming "\
                f"from {self.origin}. Doing {self.lv2} in LV2.{' Did repeat one class.' if self.repeat else ''}"\
                f"{' Quite not academic.' if not self.is_good else ''}"\
                f"{' Not academic because of : {}.'.format(', '.join(self.why_not)) if self.why_not else ''}"\
                f"{' Has a PAP.' if self.pap else ''}{' Has a PPS.' if self.pps else ''}"\
                f"{' Has a PAI.' if self.pai else ''}{' His Option 1 is {}.'.format(self.option1) if self.option1 else ''}"\
                f"{' His Option 2 is {}.'.format(self.option2) if self.option2 else ''}"\
                f"{' He want to be with : {}.'.format(', '.join(self.wanna_be_with)) if self.wanna_be_with else ''}\n"
    
    def get_weight(self, requirements: list, actual_class: list):
        # Requirements format :
        # [
        #   {
        #     "type": "max",
        #     "val": 30 # max students
        #   }
        #   {
        #     "type": "lv",
        #     "val": "ALL" # for german
        #   },
        #   {
        #     "type": "option",
        #     "val": "CIT" # idk wtf is that
        #   }
        # ]
        pass

webapp = Flask(__name__)

def readfile(path):
    if not isfile(path):
        return readfile("static/html/error.html").replace("ERROR", "The requested ressource does not exist !")
    with open(path, 'r') as f:
        return f.read()

@webapp.errorhandler(500)
def internal_error(error):
    return readfile("static/html/error.html").replace("ERROR", str(error))

@webapp.route("/")
def webhome():
    return readfile("static/html/main.html")

@webapp.route("/process", methods=["POST"])
def process_input_file():
    if isfile("classes.xlsx"):
        remove("classes.xlsx")
    if not "class" in request.files or not "dispo" in request.files:
        abort(500, description="No input file !")
    classes = request.files["class"]
    dispose = request.files["dispo"]
    if classes.filename == '' or dispose.filename == '':
        abort(500, description="No input file !")
    ccontent = classes.stream.read()
    dcontent = dispose.stream.read()
    sort_students(process_content(ccontent), process_content(dcontent))
    return send_file("classes.xlsx", attachment_filename="classes.xlsx")

def try_and_update() -> bool:
    url = "https://raw.githubusercontent.com/Tech0ne/Class-Creator/main/main.pyw"
    online_code = requests.get(url).text
    with open(sys.argv[0], 'r') as f:
        local_data = f.read()
    if local_data == online_code:
        return False
    with open(sys.argv[0], 'w+') as f:
        f.write(online_code)
    return True

def webapp_run():
    webapp.run(host="127.0.0.1", port=3456, debug=False)

def main():
    if not "--no-update" in sys.argv:
        if try_and_update():
            sys.exit(system(''.join(sys.argv) + " --no-update"))
    webapp_run()

def run():
    students    = ploads(open("students.pkl", 'rb'))
    compo       = ploads(open("compo.pkl", 'rb'))
    print(f"Our seed is : {SEED}. Please not it")
    classes = [[] * len(compo)]

class StudentType:
    def __init__(self, lv2, option1, option2):
        self.lv2 = lv2
        self.option1 = option1
        self.option2 = option2