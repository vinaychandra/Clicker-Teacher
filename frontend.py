"""
This file is used for serving the front end of the application.

Uses flask to create the lightweight web server which communicates with the
web browser front end running
"""
from functools import wraps
from global_variables import *
from flask import *

app = Flask(__name__)


def run_check(function):
    @wraps(function)
    def helper(*args, **kwargs):
        if not running:
            return render_template("home.html", running=running, ip="0.0.0.0")
        elif all_data.in_progress:
            return render_template("in_progress.html", data=all_data.in_progress)
        else:
            return function(*args, **kwargs)
    return helper


@app.route('/')
@run_check
def first_screen():
    return render_template("new_activity.html")


@app.route('/startServer')
def start_server():
    global running
    running = True
    return "True"


@app.route('/mul_choice_inp')
@run_check
def mul_choice_inp():
    return render_template("multiple_choice_inp.html", mode="quick")


@app.route('/int_inp')
@run_check
def int_type_inp():
    return render_template("integer_type_inp.html", mode="quick")


@app.route('/text_inp')
@run_check
def text_type_inp():
    return render_template("text_type_inp.html", mode="quick")

if __name__ == '__main__':
    app.run()
