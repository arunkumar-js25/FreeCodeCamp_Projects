import socket

# Socket Object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Declare hostname and port to listen
host = socket.gethostname()
port = 5500

#bind serversocket object with host and port
serversocket.bind((host,port))  #host will be replaced with IP, if changed and not running on host

#Starting TCP listener   (3) -- no of users
serversocket.listen(3)

while True:
    #Open connection
    clientsocket, address = serversocket.accept()

    print("Received connection from: %s" %str(address))

    #Notify client with message
    message = "thank you for connecting..." + "\r\n"
    clientsocket.send(message.encode('ascii'))

    #Close connection
    clientsocket.close()