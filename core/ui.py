from flask import Flask, request
from os.path import isfile

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

@webapp.route("/static/css/<path:name>")
def get_some_css(name):
    path = "static/css/" + name.replace("..", '')
    return readfile(path)

@webapp.route("/static/html/<path:name>")
def get_some_css(name):
    path = "static/html/" + name.replace("..", '')
    return readfile(path)

@webapp.route("/static/js/<path:name>")
def get_some_css(name):
    path = "static/js/" + name.replace("..", '')
    return readfile(path)


@webapp.route("/stopme")
def tryandstop():
    raise RuntimeError("SERVER_SHUTDOWN")

@webapp.teardown_request
def teardown(_):
    if not STILL_RUNNING:
        sys.exit(0)

def webapp_run():
    webapp.run(host="127.0.0.1", port=3456, debug=False)