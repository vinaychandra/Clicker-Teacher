# The main entry point for the application
from gevent.server import StreamServer
from thread import start_new_thread
from backend import *
from frontend import *

# Define server as a TCP server
server = StreamServer(('127.0.0.1', 1234), backend_handler)  # creates a new server

# Start the frontend
start_new_thread(app.run, ())

# Start the backend
server.serve_forever()
