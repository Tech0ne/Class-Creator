from .log import *

from pickle import load, dump

def to_bool(string: str):
    final = string.split(" ")[0].split("\t")[0].split("\n")[0]
    final = final.lower()
    if final in ("y", "yes", "yeah", "yea", "o", "oui", "true", "accept", "1"):
        return True
    if final in ("n", "no", "non", "nop", "false", "refuse", "0"):
        return False
    fatal(f"Could not resolve \"{string}\" as a boolean input")

def to_sex(string: str):
    final = string.split(" ")[0].split("\t")[0].split("\n")[0]
    final = final.lower()
    if final in ("g", "guy", "garcon", "garçon", "men", "homme", "man", "mec"):
        return "G"
    if final in ("f", "girl", "femme", "fille", "women", "lol_i_wont_end_my_jok"):
        return "F"
    fatal(f"Could not resolve \"{string}\" as a sex input")

def to_int(string: str):
    final = string.split(" ")[0].split("\t")[0].split("\n")[0]
    if not final.isalnum():
        return -1
    return int(final)

class Student(object):
    def __init__(self, name, first_name, sex, origin, results, attendance, care, pap, pai, pps, lv2, option_1, option_2, want_with: list, without: list, remarks):
        self.name =         name
        self.first_name =   first_name
        self.full_name =    f"{name};{first_name}"
        self.sex =          to_sex(str(sex))
        self.origin =       origin
        self.results =      to_int(str(results))
        self.attendance =   to_int(str(attendance))
        self.care =         to_int(str(care))
        self.pap =          to_bool(str(pap))
        self.pai =          to_bool(str(pai))
        self.pps =          to_bool(str(pps))
        self.lv2 =          lv2
        self.option_1 =     option_1
        self.option_2 =     option_2
        self.remarks =      remarks
        self.want_with =    want_with
        self.without =      without

    def __getattribute__(self, __name: str):
        obj = super(Student, self).__getattribute__(__name)
        if type(obj) == str and __name != "sex":
            return obj.capitalize().replace(' ', '_').replace('\t', '_').replace('\n', '_')
        return obj

    def __repr__(self) -> str:
        return f"{self.name} {self.first_name}, {'girl' if self.sex == 'g' else 'boy'} comming from {self.origin}"
    
    def can_be_added_to_the_class(self, classe: list) -> bool:
        for student in classe:
            if type(student) != Student:
                fatal("Non-Student objects found in a Student list")
            if student.full_name in self.without:
                return False
        return True