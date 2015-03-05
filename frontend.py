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
    """
    The wrapper function for checking if the application is running or not.
    If server is not running, we return the home page that displays that the server is not
    currently running.
    Also, if there is a poll that is currently going on, we redirect to the page of the
    live result data.

    :param function: The function on which the wrapper is being applied
    :type function: function
    """
    @wraps(function)
    def helper(*args, **kwargs):
        print "Val is ",all_data.running
        if not all_data.running:
            return render_template("home.html", running=all_data.running, ip="0.0.0.0")
        elif all_data.in_progress:
            return render_template("in_progress.html", data=all_data.in_progress)
        else:
            return function(*args, **kwargs)
    return helper


@app.route('/')
@run_check
def first_screen():
    """
    The main page router. Displays the main page for actions
    """
    return render_template("new_activity.html")


@app.route('/startServer')
def start_server():
    """
    The function that is used to indirectly start the backend.
    This function changes the all_data.running variable which in turn results in the running of the
    backend which is waiting exactly for this change
    """
    all_data.running = True
    print "Changing...."
    return "True"


@app.route('/mul_choice_inp/<mode>', methods=['GET', 'POST'])
@run_check
def mul_choice_inp(mode):
    """
    The input for multiple choice page. The mode here is used for quick and for saving data.

    :param mode: The mode of the input page
    """
    if mode not in ['quick']:
        return abort(404)
    if request.method == 'GET':
        return render_template("multiple_choice_inp.html", mode=mode)


@app.route('/int_inp/<mode>', methods=['GET', 'POST'])
@run_check
def int_type_inp(mode):
    """
    The input for integer answer page. The mode here is used for quick and for saving data.

    :param mode: The mode of the input page
    """
    if mode not in ['quick']:
        return abort(404)
    if request.method == 'GET':
        return render_template("integer_type_inp.html", mode="quick")


@app.route('/text_inp/<mode>', methods=['GET', 'POST'])
@run_check
def text_type_inp(mode):
    """
    The input for text answer page. The mode here is used for quick and for saving data.

    :param mode: The mode of the input page
    """
    if mode not in ['quick']:
        return abort(404)
    if request.method == 'GET':
        return render_template("text_type_inp.html", mode="quick")

if __name__ == '__main__':
    app.run()
