import socket
import rsa
import generate_key as key


host = '127.0.0.1'
port = 5000

s = socket.socket()
s.connect((host,port))


(e2, n2), (d2, n2) = key.generate_key(80)

def send_int(data):
    s.sendall(bytes(str(data), 'utf-8'))
    int(s.recv(1024))

def rcv_int():
    data = int(s.recv(1024))
    s.sendall(bytes(str(data), 'utf-8'))
    return data

e1 = rcv_int()
n1 = rcv_int()
send_int(e2)
send_int(n2)

def send(data,e,n):
    encoded = rsa.encode(data)
    encrypted = rsa.group_encrypt(encoded, e, n)
    send_int(len(encrypted))
    for i in encrypted:
        send_int(i)

def receive(d,n):
    length = rcv_int()
    cipher_list = []
    for i in range(length):
        cipher_list.append(rcv_int()) 
    decrypted = rsa.group_decrypt(cipher_list, d, n)
    decoded = rsa.decode(decrypted)
    return decoded

while True:
    data = input("Enter data to be sent:")
    send(data,e1,n1)
    
    data = receive(d2,n2)
    print("Received : " + data)

    