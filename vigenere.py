alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
code = "ymlok cp fbb ejv"
key = "dog"
#24 12 11 14 10   2  15   5  1  1    4  9  21

unlocker = [] # The cripto key
unlockerstring = [] # The key repeated to match the code lenght

def get_key(key):
    global unlockerstring, unlocked, translated_code, final
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
    translated_code = []
    i = 0
    o = 0
    final = ""
    for index in unlocked:
        # try:
        
        final += str(float(unlocked[i]) - float(unlockerstring[i]))
        final += " "
        i += 1
        print(final)
        # except ValueError:
        #     final += "spaço"

get_key(key)
print(unlocked)
print(unlockerstring)
print(final)
