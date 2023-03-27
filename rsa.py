import generate_key as key

def alphabet_position(letter):
    letter = letter.lower()
    number = 0
    if(letter >= '0' and letter <= '9'):
        return ord(letter) - ord('0') 
    elif(letter >= 'a' and letter <= 'z'):
        return ord(letter) - ord('a') + 10
    else: number = 36
    return number

def inverse_alphabet_position(number):
    if(number >= 0 and number <= 9):
        return chr(number + ord('0'))
    elif(number >= 10 and number <= 35):
        return chr(number + ord('a') - 10)
    return ' '



def encode(plain_text):
    list = [plain_text[i:i+5] for i in range(0, len(plain_text), 5)]
    encoded_list = []
    for l in list:
        num = 0
        for i in range(len(l)):
            num += alphabet_position(l[i]) * (37 ** (5 - i - 1))
        encoded_list.append(num)
    return encoded_list

def decode(encoded_list):
    plain_text = ""
    for num in encoded_list:
        l = ""
        for i in range(5):
            char = inverse_alphabet_position((num // (37 ** (5 - i - 1))) % 37)
            l += char
        plain_text += l
    return plain_text

def encrypt(M, e,n):
    return pow(M, e, n)


def decrypt(C, d, n):
    return pow(C, d, n)


def group_encrypt(M, e, n):
    return [encrypt(m, e, n) for m in M]

def group_decrypt(C, d, n):
    return [decrypt(c, d, n) for c in C]





# (e, n), (d, n) = key.generate_key(10)

# text = 'hello world'
# encoded = encode(text)
# encrypted = group_encrypt(encoded, e, n)
# decrypted = group_decrypt(encrypted, d, n)
# decoded = decode(decrypted)
# print(decoded)