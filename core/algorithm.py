from .log import *

from json import loads as jloads
from pickle import loads as ploads

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