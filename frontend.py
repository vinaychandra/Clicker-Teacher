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
        if not all_data.running:
            return render_template("home.html", running=all_data.running, ip="0.0.0.0")
        elif all_data.publish:
            return redirect("/in_progress")
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
        return render_template("multiple_choice_inp.html", mode=mode, btn="Start Poll")

    # Process the submit data
    if request.method == 'POST':
        if request.form['mode'] == 'quick':
            # Get the options...
            data = []
            any_answer = False  # Stores if at least one answer is provided
            question = request.form['question']
            for choice in ['a', 'b', 'c', 'd']:
                text = request.form['op' + choice.upper()]
                if str(choice + 'c') in request.form:
                    if request.form[choice + 'c'] == 'on':
                        any_answer = True
                        answer = True
                    else:
                        answer = False
                else:
                    answer = False
                if text != "":
                    data.append((text, answer))
            # setting in_progress
            all_data.in_progress = {'any_answer': any_answer, 'options': data, 'mode': "quick", 'question': question,
                                    'type': "mul_choice"}
            # mode is quick. Therefore publish
            all_data.publish = True
            return redirect('/in_progress')


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
