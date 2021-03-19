mode = int(input("Enter mode\n1: cipher\n2: decipher\n"))
lang = int(input("Enter language\n1: RU (32 letters)\n2: EN\n"))
word = input("Enter message: ").lower()
key = int(input("Enter key: "))


def shift(word, key, module, start):
    new_word = ''
    for i in range(len(word)):
        new_word += chr((((ord(word[i]) - start) + key) % module) + start)
    return new_word


if lang == 1:
    module = 32
    start = ord('а')
elif lang == 2:
    module = 26
    start = ord('a')

if mode == 2:
    key = 0 - key

answer = shift(word, key, module, start)

if mode == 1:
    print(answer.upper())
else:
    print(answer)
