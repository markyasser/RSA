import time
import rsa
import numpy as np
import matplotlib.pyplot as plt
import generate_key as key

decrypt_time = []
bit_count = []
plain_text = 'hello'


def init_attack(i):
    (e, n), (d, n) = key.generate_key(i)
    if(len(bit_count) > 0 and bit_count[-1] >= n.bit_length()):
        print(f'Skipped smaller n size previous: {bit_count[-1]} , current: {n.bit_length()}')
        i += 1
        return i
    elif(len(bit_count) > 0 and bit_count[-1]+2 <= n.bit_length()):
        print(f'Skipped large jump size previous: {bit_count[-1]} , current: {n.bit_length()}')
        i-=1
        return i
    encoded = rsa.encode(plain_text)
    encrypted = rsa.group_encrypt(encoded, e, n)

    # In the following section trying to find the d(private key) value by brute force attack
    # Given e(public key), n(public key), cypher text, plaintext
    #-----------------Attack-----------------
    d_init = e // 100 # this initial value is used to reduce the time taken to find the d value
    dec = rsa.group_decrypt(encrypted, d_init, n)
    decoded = rsa.decode(dec)
    print(f"Initiating attack : e = {e},  d = {d}, d_init = {d_init}, d-d_init = {d-d_init}")
    start = time.time()
    while plain_text != decoded:
        d_init += 1
        dec = rsa.group_decrypt(encrypted, d_init, n)
        decoded = rsa.decode(dec)
        if(d_init % 5000000 == 0):
            print(f"d_init = {d_init}, d-d_init = {d-d_init}")
    end = time.time() 
    print(decoded) 
    time_taken = round(end - start, 4)
    print(f"Execution time: {time_taken} seconds , i = {i} , n = {n.bit_length()} bits , d = {d} , d_init = {d_init}")
    #----------------------------------------


    decrypt_time.append(time_taken)
    bit_count.append(n.bit_length())
    return i + 1



# iterate over key size from 22 to 36
start = 22
end = 36
decrypt_time = []
bit_count = []
i = start
while i < end + 1:
    i = init_attack(i)
    print('decrypted time : ',decrypt_time,'\nnumber of bits : ',bit_count)


# Display the breaking time vs key size
x = np.linspace(5, 20, 1)
plt.plot(x,decrypt_time)
plt.xlabel('Key size')
plt.ylabel('Decryption Time')
plt.show()