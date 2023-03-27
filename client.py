import socket


host = '127.0.0.1'
port = 5000

s = socket.socket()
s.connect((host,port))

def send(data):
    s.send(data.encode('utf-8'))

def receive():
    return s.recv(1024).decode('utf-8')

while True:
    data = input("Enter data to be sent:")
    send(data)
    
    data = receive()
    print("Received : " + data)

    