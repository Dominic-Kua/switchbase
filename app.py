import flask
import os
import sys
folder = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))

DEBUG = False or os.environ["FLASK_DEBUG"]

app = flask.Flask(__name__)

def main():
    app.run(debug=DEBUG)

@app.route("/")
def hello_world():
    return "<h1>The Switch Database</h1>"