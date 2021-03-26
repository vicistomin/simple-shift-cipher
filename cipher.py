# defaults:
key, key1, key2, module, start = [0] * 5

cipher = int(input("Enter mode\n1: shift\n2: affine\n"))
mode = int(input("Enter mode\n1: Encryption\n2: Decryption\n"))
lang = int(input("Enter language\n1: RU (33 letters)\n2: RU (32 letters)\n3: EN\n"))
word = input("Enter message: ").lower()

# Shift cipher
if cipher == 1:
    key = int(input("Enter key: "))

# Affine cipher
elif cipher == 2:
    key1 = int(input("Enter 1st (multiplicative) key: "))
    key2 = int(input("Enter 2nd (additive) key: "))


def shift(index, key, module):
    shifted_index = []
    for i in range(len(word)):
        shifted_index.append((index[i] + key) % module)
    return shifted_index


def affine(index, key1, key2, module, mode):
    new_index = []

    # Encryption
    if mode == 1:
        for i in range(len(word)):
            new_index.append((((index[i] * key1) % module) + key2) % module)

    # Decryption
    else:
        for i in range(len(word)):
            # check this:
            new_index.append(((index[i] - key2) % module), pow(key1, -1, module), module)
    return new_index


indexes = []
jo_shift = ord('ё') - ord('е') - 1

# Russian with Ё (33 letters)
if lang == 1:
    module = 33
    start = ord('а')

    for i in range(len(word)):
        index = ord(word[i])
        if index == ord('ё'):
            indexes.append(index - jo_shift - start)
        elif index <= ord('е'):
            indexes.append(index - start)
        elif index > ord('е'):
            indexes.append(index - start + 1)

# Russian w/out Ё (32 letters)
elif lang == 2:
    word = word.replace('ё', 'е')

    module = 32
    start = ord('а')
    for i in range(len(word)):
        indexes.append(ord(word[i]) - start)

# English
elif lang == 3:
    module = 26
    start = ord('a')
    for i in range(len(word)):
        indexes.append(ord(word[i]) - start)

# Key manipulation for decipher mode (affects only shift cipher)
if mode == 2:
    key = 0 - key

answer = ''

# Shift cipher
if cipher == 1:
    new_indexes = shift(indexes, key, module)

# Affine cipher
elif cipher == 2:
    new_indexes = affine(indexes, key1, key2, module, mode)

e_shift = ord('е')-ord('а')

if lang == 1:
    for i in range(len(new_indexes)):
        if new_indexes[i] == e_shift + 1:  # Ё
            answer += chr(new_indexes[i] + jo_shift + start)
        elif new_indexes[i] <= e_shift:
            answer += chr(new_indexes[i] + start)
        elif new_indexes[i] > e_shift:
            answer += chr(new_indexes[i] + start - 1)

elif lang == 2 or 3:
    for i in range(len(new_indexes)):
        answer += chr(new_indexes[i] + start)

if mode == 1:
    print(answer.upper())
else:
    print(answer)
