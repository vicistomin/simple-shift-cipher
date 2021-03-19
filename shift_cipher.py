mode = int(input("Enter mode\n1: cipher\n2: decipher\n"))
lang = int(input("Enter language\n1: RU (33 letters)\n2: EN\n"))
word = input("Enter message: ").lower()
key = int(input("Enter key: "))


def shift(index, key, module):
    encrypted_index = []
    for i in range(len(word)):
        encrypted_index.append(((index[i]) + key) % module)
    return encrypted_index


indexes = []
jo_shift = ord('ё') - ord('е') - 1

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

elif lang == 2:
    module = 26
    start = ord('a')
    for i in range(len(word)):
        indexes.append(ord(word[i]) - start)

if mode == 2:
    key = 0 - key

answer = ''

new_indexes = shift(indexes, key, module)
e_shift = ord('е')-ord('а')

if lang == 1:
    for i in range(len(new_indexes)):
        if new_indexes[i] == e_shift + 1:  # Ё
            answer += chr(new_indexes[i] + jo_shift + start)
        elif new_indexes[i] <= e_shift:
            answer += chr(new_indexes[i] + start)
        elif new_indexes[i] > e_shift:
            answer += chr(new_indexes[i] + start - 1)

elif lang == 2:
    for i in range(len(new_indexes)):
        answer += chr(new_indexes[i] + start)

if mode == 1:
    print(answer.upper())
else:
    print(answer)
