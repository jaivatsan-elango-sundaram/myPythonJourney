#idea and ascii art by angela yu on udemy
#all other code by jai sundaram 
print('''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
      ''')

anotherOne = True
askAnother = ""
option = ""
while anotherOne == True:
    #function for encrypting the word 
    def encrypt(word, shift_number):
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        wordList = []
        encryptedList = []
        encryptedWord = ""
        index = 0
        newLetter = ""
        for i in range(0, len(word)):
            wordList.append(word[i])
            encryptedList.append("x")
        for i in range(0, len(word)):   
            if wordList[i] in letters:
                newLetter = word[i]
                index = letters.index(newLetter)
                if index + shift_number > len(letters) -1:
                    encryptedList[i] = letters[(index + shift_number) - (len(letters))]
                else:
                    encryptedList[i] = letters[index + shift_number]
            else:
                encryptedList[i] = wordList[i]
        encryptedWord = "".join(encryptedList)
        print(f"Your encrypted word is: {encryptedWord}")
    def decrypt(word, shift_number):
        #function for decrypting the word
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        wordList = []
        decryptedList = []
        decryptedWord = ""
        index = 0
        newLetter = ""
        for i in range(0, len(word)):
            wordList.append(word[i])
            decryptedList.append("x")
        for i in range(0, len(word)):
            if wordList[i] in letters:
                newLetter = word[i]
                index = letters.index(newLetter)
                if index - shift_number < 0:
                    decryptedList[i] = letters[(index - shift_number) + (len(letters))]
                else:
                    decryptedList[i] = letters[index + shift_number]
                decryptedList[i] = letters[index - shift_number]
            else:
                decryptedList[i] = wordList[i]
        decryptedWord = "".join(decryptedList)
        print(f"Your encrypted word is: {decryptedWord}")
    option = input("Would you like to encrypt or decrypt? (e/d): ")
    userWord = input("What is the word you would like to encrypt/decrypt?: ")
    userWord = userWord.lower()
    user_shift_number = int(input("Please enter the shift number: "))
    user_shift_number = user_shift_number % 26
    if option == "e":
        encrypt(userWord, user_shift_number)
    else:
        decrypt(userWord, user_shift_number)
    askAnother = input("Would you like to perform another encryption/decryption? (y/n)")
    if askAnother == "n":
        anotherOne = False
        print("Thanks for using this application!")