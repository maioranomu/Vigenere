alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
code = "ymlok cp fbb ejv"
key = "dog"
#24 12 11 14 10   2  15   5  1  1    4  9  21

unlocker = [] # The cripto key
unlockerstring = [] # The key repeated to match the code lenght

def get_key(key):
    global unlockerstring, unlocked
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
    print(unlockerstring)
    while i < len(code):
        for word in code:
            for letter in word:
                i += 1
                if letter in alphabet:
                    unlocked.append(alphabet.index(letter) - int(unlockerstring[i]))
                else:
                    unlocked.append(letter)       
        
get_key(key)
print(unlocked)            
print("u")

# def decoder(code, key):
#     for word in code:
#         for letter in word:
#             if letter in alphabet:
#                 index = alphabet[alphabet.index(letter) - alphabet.index()]
#                 coderesult.append()
            