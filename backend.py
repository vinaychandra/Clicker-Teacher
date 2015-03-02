from global_variables import all_data


def backend_handler(socket, address):
    """
    :type socket: gevent.socket.socket
    :type address: tuple(str, int)
    """

    all_data.count += 1
    print 'Accepting connection from ', address[0], ':', address[1]
    socket.send("Accept " + str(all_data.count))
    a = socket.recv(8)
    print a, address
