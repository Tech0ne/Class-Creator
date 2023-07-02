from datetime import datetime
import sys

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