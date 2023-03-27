import time
import rsa
import generate_key as key
(e, n), (d, n) = key.generate_key(9)

text = 'hello world'
encoded = rsa.encode(text)
encrypted = rsa.group_encrypt(encoded, e, n)

#-----------------Attack-----------------
decrypted = rsa.group_decrypt(encrypted, d, n)
decoded = rsa.decode(decrypted)
start = time.time()
d_init = d - 100000
while decrypted != rsa.group_decrypt(encrypted, d_init, n):
    d_init += 1
end = time.time()
print(f"Execution time: {round(end - start, 4)} seconds")
#----------------------------------------

decrypted = rsa.group_decrypt(encrypted, d, n)
decoded = rsa.decode(decrypted)