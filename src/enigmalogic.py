import string

alphabet=list(chr(i) for i in range(48, 58))+list(string.ascii_uppercase)+list(string.ascii_lowercase)

DEFRULES={'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,
            'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19,
            'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26, 'a':27, 'b':28,
            'c':29, 'd':30, 'e':31, 'f':32, 'g':33, 'h':34, 'i':35, 'j':36, 'k':37,
            'l':38, 'm':39, 'n':40, 'o':41, 'p':42, 'q':43, 'r':44, 's':45, 't':46,
            'u':47, 'v':48, 'w':49, 'x':50, 'y':51, 'z':52}
tempRules=DEFRULES.copy()

def Gen_Code (code):
    if code.isdigit()==True:
        intList=[int(i) for i in str(code)]
    else:
        intList=[]
        for char in code:
            if char in tempRules:
                intList.append(tempRules[char])
            else:
                try:
                    intList.append(int(char))
                except:
                    pass
    return intList
 
def Set_Rule(myRules):
    tempRules.update(myRules)
    return tempRules

def Reset_Rule():
    tempRules=DEFRULES
    return tempRules

def Caesar_Encrypt (words, codes):
    sentence=''.join(words)
    newCodes = [codes[i % len(codes)] for i in range(len(sentence))]
    encryptedMsg = []
    for char, secNum in zip(sentence, newCodes):
        if char in alphabet:
           encryptedMsg .append(alphabet[(alphabet.index(char)+ secNum) % len(alphabet)])
        else:
            encryptedMsg .append(char)
    return encryptedMsg 

def Print_Msg (secPhrase):
    secStr="".join([str(element) for element in secPhrase])
    print(secStr)

def Caesar_Decrypt (words, codes):
    sentence=''.join(words)
    newCodes = [codes[i % len(codes)] for i in range(len(sentence))]
    decryptedMsg = []
    for char, secNum in zip(sentence, newCodes):
        if char in alphabet:
           decryptedMsg .append(alphabet[(alphabet.index(char)- secNum) % len(alphabet)])
        else:
           decryptedMsg .append(char)
    return decryptedMsg 

def Layer_Encrypt (words, codes): 
    sentence=''.join(words)
    newCodes = [codes[i % len(codes)] for i in range(len(sentence))]
    tempCode = []
    tempValue = 0
    for code in newCodes:
        tempValue += code
        tempCode.append(tempValue)
    encryptedMsg = []
    for char, secNum in zip(sentence, tempCode):
        if char in alphabet:
           encryptedMsg .append(alphabet[(alphabet.index(char)+ secNum) % len(alphabet)])
        else:
            encryptedMsg .append(char)
    return encryptedMsg 
 

def Layer_Decrypt (words, codes):
    sentence=''.join(words)
    newCodes = [codes[i % len(codes)] for i in range(len(sentence))]
    tempCode = []
    tempValue = 0
    for code in newCodes:
        tempValue += code
        tempCode.append(tempValue)
    decryptedMsg = []
    for char, secNum in zip(sentence, tempCode):
        if char in alphabet:
            decryptedMsg.append(alphabet[(alphabet.index(char)- secNum) % len(alphabet)])
        else:
            decryptedMsg.append(char)
    return decryptedMsg

def Read_File(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
        L=[]
        if lines is not None:
            for word in lines:
                L.append(word)
            L.append(" \n")
        return L
    except FileNotFoundError:
        print(f"File not found.")
        return None
    
def Write_File(path, words):
    try:
        with open(path, 'w') as file:
            for word in words:
                file.write(str(word))
    except Exception as e:
        print(f"An error occurred: {e}")

def To_Dict(string):
    key, value = string.split(':')
    key = key.strip()
    value = value.strip()
    try:
        value = int(value)
    except ValueError:
        pass 
    return {key: value}

def process_file(path):
        with open(path, 'r') as f:
            for line in f:   
                return line

def compare(s):
    s.replace('(','').replace(')','').strip()
    return eval(s)
# rule={'a':10,'b':20}
# myrule1=Set_Rule(rule)
# # code1=Gen_Code(secCode2)
# print (myrule1)
# secMsg=Partial_Encrypt(line, code1)
# Print_Msg(secMsg)
# realMsg=Partial_Decrypt(secMsg, code1)
# Print_Msg(realMsg)
# secMsg=Layer_Encrypt(line, code1)
# Print_Msg(secMsg)
# realMsg=Layer_Decrypt(secMsg,code1)
# Print_Msg(realMsg)
    