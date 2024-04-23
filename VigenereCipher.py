import os, time
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
detail = False
def decode():
    global detail
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
            if detail:
                print(add)
            if add < 0:
                add = len(alphabet) + add
            final.append(add)
            if detail:
                print(final)
            i += 1
        except ValueError:
            final.append(" ")
            i += 1
    translated = ""
    for i in final:           
        if detail:
            print(i)
        if i == " ":
            translated += " "
        else:
            translated += alphabet[int(i)]
    if detail:
        print("Index 1: ")
        print(unlocked)    
        print("Index 2: ")
        print(unlockerstring)
        print("Final: ")
        print(final)
    return "Result: " + translated
def encode():
    global detail
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
            if detail:
                print(add)
            if add >= len(alphabet):
                add = add - len(alphabet)
            final.append(add)
            if detail:
                print(final)    
            i += 1
        except ValueError:
            final.append(" ")
            i += 1
    translated = ""
    if detail:
        print(final)
    for i in final:   
        if detail:        
            print(i)
        if i == " ":
            translated += " "
        else:
            translated += alphabet[int(i)]
    if detail:
        print("Index 1: ")
        print(unlocked)    
        print("Index 2: ")
        print(unlockerstring)
        print("Final: ")
        print(final)
    return "Result: " + translated
def cls():
    os.system("cls")
def main():
    global detail
    while True:
        cls()
        action = input("1 ENCODE | 2 DECODE \n").lower()
        if action == "1":
            cls()
            input(encode())
        elif action == "2":
            cls()
            input(decode())
        elif action == "d":
            match(detail):
                case True:
                    detail = False
                    print("DEBUG OFF")
                    time.sleep(0.2)
                    cls()
                case False:
                    detail = True
                    print("DEBUG ON")
                    time.sleep(0.2)
                    cls()
main()
