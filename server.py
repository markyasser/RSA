import socket

host = '127.0.0.1'
port = 5000

s = socket.socket()
s.bind((host,port))

s.listen(1)
c, addr = s.accept()


def send(data):
    c.send(data.encode('utf-8'))

def receive():
    return c.recv(1024).decode('utf-8')

while True:
    data = receive()
    print("Received : " + data)


    data = input("Enter data to be sent:")
    send(data)
