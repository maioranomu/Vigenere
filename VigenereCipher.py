import os
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# code = "mcf kuarz xeapl"
# key = "jyliq"
def decode():
    code = input("Code: ")
    key = input("Key: ")
    unlocker = []
    unlockerstring = []
    for letter in key:
        if letter in alphabet:
            unlocker.append(alphabet.index(letter))
        else:
            unlocker.append(letter)
    i = 0   
    for word in code:
        for letter in word:
            if letter in alphabet:
                if i > len(unlocker) - 1:
                    i = 0
                unlockerstring.append(unlocker[i])
                i += 1
            else:
                unlockerstring.append(letter)            
    unlocked = []
    i = 0
    while i < len(code):
        for word in code:
            for letter in word:
                i += 1
                if letter in alphabet:
                    unlocked.append(alphabet.index(letter))
                else:
                    unlocked.append(letter)
    i = 0
    final = []
    for index in unlocked:
        try:
            add = (float(unlocked[i]) - float(unlockerstring[i]))
            # print(add)
            if add < 0:
                add = len(alphabet) + add
            final.append(add)
            # print(final)
            i += 1
        except ValueError:
            final.append(" ")
            i += 1
    translated = ""
    for i in final:           
        # print(i)
        if i == " ":
            translated += " "
        else:
            translated += alphabet[int(i)]
    # print("Index 1: ")
    # print(unlocked)    
    # print("Index 2: ")
    # print(unlockerstring)
    # print("Final: ")
    # print(final)

    return "Result: " + translated

def encode():
    code = input("Text: ")
    key = input("Key: ")
    unlocker = []
    unlockerstring = []
    for letter in key:
        if letter in alphabet:
            unlocker.append(alphabet.index(letter))
        else:
            unlocker.append(letter)
    i = 0   
    for word in code:
        for letter in word:
            if letter in alphabet:
                if i > len(unlocker) - 1:
                    i = 0
                unlockerstring.append(unlocker[i])
                i += 1
            else:
                unlockerstring.append(letter)            
    unlocked = []
    i = 0
    while i < len(code):
        for word in code:
            for letter in word:
                i += 1
                if letter in alphabet:
                    unlocked.append(alphabet.index(letter))
                else:
                    unlocked.append(letter)
    i = 0
    final = []
    for index in unlocked:
        try:
            add = (float(unlocked[i]) + float(unlockerstring[i]))
            # print(add)
            if add > len(alphabet):
                add = add - len(alphabet)
            final.append(add)
            # print(final)
            i += 1
        except ValueError:
            final.append(" ")
            i += 1
    translated = ""
    for i in final:           
        # print(i)
        if i == " ":
            translated += " "
        else:
            translated += alphabet[int(i)]
    # print("Index 1: ")
    # print(unlocked)    
    # print("Index 2: ")
    # print(unlockerstring)
    # print("Final: ")
    # print(final)
    return "Result: " + translated

def cls():
    os.system("cls")

def main():
    while True:
        cls()
        action = input("1 ENCODE | 2 DECODE: ")
        if action == "1":
            input(encode())
        elif action == "2":
            input(decode())

main()
