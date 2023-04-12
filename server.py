import socket
import rsa
import generate_key as key

host = '127.0.0.1'
port = 5000

s = socket.socket()
s.bind((host,port))

s.listen(1)
c, addr = s.accept()


(e1, n1), (d1, n1) = key.generate_key(80)

def send_int(data):
    c.sendall(bytes(str(data), 'utf-8'))
    int(c.recv(1024))

def rcv_int():
    data = int(c.recv(1024))
    c.sendall(bytes(str(data), 'utf-8'))
    return data

send_int(e1)
send_int(n1)
e2 = rcv_int()
n2 = rcv_int()

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
    data = receive(d1,n1)
    print("Received : " + data)


    data = input("Enter data to be sent:")
    send(data,e2,n2)
    
