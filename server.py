import socket
LocalHost=socket.gethostname()
port=5000
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((LocalHost,port))
server.listen(1)
print("Server is started")
print("Waiting for client request")
while True:
    clientConnection,clientAddress=server.accept()
    print("Connected client",clientAddress)
    name=clientConnection.recv(1024)
    print("Name:",name.decode())
    adult=clientConnection.recv(1024)
    print("No of adults:",adult.decode())
    print(type(adult))
    ad1=int(adult)
    child=clientConnection.recv(1024)
    print("No of children:",child.decode())
    cd1=int(child)
    ac=ad1+cd1
    clientConnection.send(str(ac).encode('utf8'))
    cost=(ad1*1000)+(cd1*350)
    clientConnection.send(str(cost).encode('utf8'))


