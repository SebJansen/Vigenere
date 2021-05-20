from copy import copy
from typing import List, Union

message: str = 'deze fietsen zijn rood'
key: str = 'abc'

f = open('dutch.txt')
wordlist = f.read()
f.close()


# Turn a string into a list of integers denoting unicode characters
def encode(chrs: Union[str, List[str]]) -> List[int]:
    return [ord(c) for c in chrs]


# Turn a list of integers denoting unicode characters, into a string
def decode(ords: List[int]) -> str:
    return ''.join([chr(o) for o in ords])


# Repeat key to match length of message
def expand_key(k: str, n: int) -> str:
    long_k = ""

    while len(long_k) < n:
        long_k += k

    return long_k[:n]


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


encoded_message: List[int] = encode(message)
encoded_key: List[int] = encode(expand_key(key, len(message)))

encrypted: List[int] = encrypt(encoded_message, encoded_key)
decrypted: List[int] = decrypt(encrypted, encoded_key)

decoded_message: str = decode(decrypted)


def is_correct(s: str):
    # print(wordlist)

    for w in s.split(' '):
        if w in wordlist:
            return True

    return False


def brute_force(m: List[int]):
    start: int = 0
    end: int = ord('z')
    k: List[int] = [0]
    layers_exhausted = 0

    while not is_correct(
            decode(
                decrypt(
                    m,
                        encode(expand_key(
                            decode(k), len(m),
                        )
                    ),
                )
            )
    ):
        print(f'{k} is not correct')
        latest = k[layers_exhausted]

        print(f'latest is {latest}')
        print(f'end is {end}')

        if latest == end or layers_exhausted == len(k):
            if latest == end:
                print('level increased')
                layers_exhausted += 1
            if layers_exhausted == len(k):
                # zeroing out, to start over with one extra level deeper
                k = [0 for _ in range(0, layers_exhausted+1)]
                print(k)
                k[layers_exhausted] = 0
                layers_exhausted = 0
                print('next level')
        k[layers_exhausted] += 1
    if is_correct(decode(decrypt(m, k))):
        decoded_key = decode(k)
        print(f'key is {decoded_key}')

print(message)
print(key)
print(encrypted)
print(decrypted)
print(decoded_message)

brute_force(encrypted)

# print(words)
# for c in cipher:
