# The main entry point for the application
from gevent.server import StreamServer
from thread import start_new_thread
from backend import *
from frontend import *
from global_variables import all_data

# Define server as a TCP server
server = StreamServer(('127.0.0.1', 1234), backend_handler)  # creates a new server

# Start the frontend
start_new_thread(app.run, ())

# Start the backend
while all_data.running is False:
    pass

print "Starting... "
server.serve_forever()
