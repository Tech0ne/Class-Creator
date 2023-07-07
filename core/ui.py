from .algorithm import *

from flask import Flask, request, abort, send_file
from os.path import isfile
from os import remove

from .log import *

STILL_RUNNING = True

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
    sort_students(process_content(ccontent), process_content(dispose))
    send_file("classes.xlsx", attachment_filename="classes.xlsx")

@webapp.teardown_request
def teardown(_):
    if not STILL_RUNNING:
        sys.exit(0)

def webapp_run():
    webapp.run(host="127.0.0.1", port=3456, debug=False)