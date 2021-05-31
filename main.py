import math
from copy import copy
from typing import List


# Turn a string into a list of integers denoting unicode characters
def encode(chrs) -> List[int]:
    return [ord(c) for c in chrs]


# Turn a list of integers denoting unicode characters, into a string
def decode(ords: List[int]) -> str:
    return ''.join([chr(o) for o in ords])


# Repeat key to match length of message
def expand(k: List[int], n: int) -> List[int]:
    long_k: List = []

    while len(long_k) < n:
        index = len(long_k) % len(k)
        point = k[index]
        long_k.append(point)

    return long_k


# Encrypt message with key
def encrypt(m: List[int], k: List[int]) -> List[int]:
    result: List[int] = []

    for i in range(len(m)):
        result.append(m[i] + k[i])

    return result


# Decrypt message with key
def decrypt(m: List[int], k: List[int]) -> List[int]:
    result: List[int] = []

    for i in range(0, len(m)):
        mt = copy(m[i])
        kt = copy(k[i])
        result.append(mt - kt)

    return result


f = open('dutch.txt')
wordlist = f.read()
f.close()


def has_common_word(s: str):
    for w in s.split(' '):
        if w in wordlist:
            return True

    return False


def brute_force(m: List[int]) -> List[int]:
    DIGIT_MIN: int = 0
    DIGIT_MAX: int = 122 + 1

    amount_of_digits: int = 0

    while True:
        i = 0

        limit = DIGIT_MAX + 1
        combinations = (limit ** amount_of_digits) - 1

        while i < combinations:
            k = [
                math.floor(i / ((DIGIT_MAX + 1) ** n)) % (DIGIT_MAX + 1)
                for n in range(0, amount_of_digits)
            ]
            k_long = expand(k, len(m))
            dec = decrypt(m, k_long)
            text = decode(dec)

            print('--')
            print(f'tried encoded key: {k}')
            print(f'tried decoded key: {decode(k)}')
            print('--')

            if has_common_word(text):
                return k

            i += 1

        amount_of_digits += 1


message: str = 'deze fietsen zijn rood'
key: List[int] = encode('a')

encoded_message: List[int] = encode(message)
encoded_key: List[int] = expand(key, len(message))

encrypted: List[int] = encrypt(encoded_message, encoded_key)
decrypted: List[int] = decrypt(encrypted, encoded_key)

decoded_message: str = decode(decrypted)

brute_key = brute_force(encrypted)

print(f'plain message       : {message}')
print(f'plain key           : {key}')
print(f'encrypted message   : {encrypted}')
print(f'decrypted message   : {decrypted}')
print(f'decoded message     : {decoded_message}')
print(f'encoded brute key   : {brute_key}')
print(f'decoded brute key   : {decode(brute_key)}')



# print(words)
# for c in cipher:
