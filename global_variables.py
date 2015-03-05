"""
This file defines all the variables used in the project in a class based format from easy cross module access
"""


class Session:
    def __init__(self):
        self.count = 0  # number of active connections
        self.running = False    # is the backend running?
        self.in_progress = False    # Data of the currently running session

all_data = Session()
