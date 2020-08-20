from flask import Flask,render_template, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
from getDashSegments import getDashSegments
from concurrent.futures import ThreadPoolExecutor
import os, sys

executor = ThreadPoolExecutor(1)

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return "dash-dwnld-py is ready!"
    if request.method == 'POST':
        content = request.get_json()
        executor.submit(getDashSegments,content)
        return "files downloaded"
    else:
        return "No valid Method"

@app.route('/status', methods=['GET'])
def status_exec():
    if request.method == 'GET':
        f = open('out.log', "r")
        return render_template('status.html',output=f.readlines())

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("out.log", "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass    


if __name__ == '__main__':
    sys.stdout = Logger()
    app.run()


