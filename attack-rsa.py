import time
import rsa
import numpy as np
import matplotlib.pyplot as plt
import generate_key as key

text = 'h'
decrypt_time = []
for i in range(0,10):
    (e, n), (d, n) = key.generate_key(i)
    encoded = rsa.encode(text)
    encrypted = rsa.group_encrypt(encoded, e, n)
    decrypted = rsa.group_decrypt(encrypted, d, n) # real decryption
    decoded = rsa.decode(decrypted)
    #-----------------Attack-----------------
    start = time.time()
    d_init = 1
    while decrypted != rsa.group_decrypt(encrypted, d_init, n):
        d_init += 1
    end = time.time()
    print(f"Execution time: {round(end - start, 4)} seconds , i = {i}")
    decrypt_time.append(round(end - start, 4))
    #----------------------------------------

x = np.linspace(5, 20, 1)
plt.plot(x,decrypt_time)
plt.xlabel('Key size')
plt.ylabel('Decryption Time')
plt.show()