"""
This file defines all the variables used in the project in a class based format from easy cross module access
"""


class Session:
    def __init__(self):
        self.count = 0  # number of active connections
        self.running = False  # is the backend running?
        self.in_progress = False  # Data of the currently running session
        self.publish = False  # Publish
        self.results = [0, 0, 0, 0]  # Stores results for single questions
        self.mode = False  # quick or other modes
        self.type = False  # Numeric, Multiple Choice or Text type

    def publish_data(self):
        if self.in_progress is False:
            raise Exception("Called publish data without any available data")


all_data = Session()
