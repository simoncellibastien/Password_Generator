import key, encryption, utils, variables

""" Ask the user to enter the master password and the domain name """
def getInfo():
    master_pwd = input("Master password : ")
    domain = input("Domain name : ")
    return master_pwd, domain

""" Concatenate master password and domain name """
def concatInfo(master_pwd, domain):
    concat = master_pwd.replace(" ","") + domain.replace(".", "")
    return concat
    
""" Convert string into an hex string """
def convertToHex(string):
    str_hex_list = []
    str_hex_list_sub = []
    count = 1
    for char in string:
        str_hex_list_sub.append(format(ord(char), "x"))
        if count%6 == 0:
            str_hex_list.append(str_hex_list_sub)
            str_hex_list_sub = []
        count += 1
    return str_hex_list

""" Create the cipher key (288 bits) based on master password and domain """
def madeCipherKey(string_hex):
    cipher_key = []
    cipher_key.append(string_hex[5])
    cipher_key.append(string_hex[2])
    cipher_key.append(string_hex[4])
    cipher_key.append(string_hex[1])
    cipher_key.append(string_hex[0])
    cipher_key.append(string_hex[3])
    return cipher_key

""" Generate nbr_round sub key from cipher_key """
def keySchedule(cipher_key, nbr_round):
    list_of_key = []
    list_of_key.append(cipher_key)
    tmp_list = []
    for i in range(0, nbr_round):
        #utils.displayMatrix(cipher_key)
        for j in range(0, len(cipher_key)):
            if j == 0:
                piece_of_key = key.rotWord(list_of_key[i])
                sub_bytes_key = key.subBytes(piece_of_key)
                tmp_list.append(key.addingXor(sub_bytes_key, list_of_key[i],variables.rcon[i], j))
            else:
                tmp_list.append(key.addingXorForOthers(tmp_list[j-1],list_of_key[i],j))
        list_of_key.append(utils.rotateMatrix(tmp_list))
        tmp_list = []
    return list_of_key

""" First round only addRoundKey with cypher key """
def initialRound(password, key):
    return encryption.addRoundKey(password,key)

""" 9 main rounds : subBytes, shiftRows, mixColumns, addRoundKey """
def mainRound(password, list_of_key):
    for i in range(0,9):
        password = encryption.subBytes(password)
        password = encryption.shiftRows(password)
        password = encryption.mixColumns(password)
        password = encryption.addRoundKey(password,list_of_key[i+1])
    return password

""" Last round : subBytes, shiftRows, addRoundKey """
def finalRound(password, key):
    password = encryption.subBytes(password)
    password = encryption.shiftRows(password)
    password = encryption.addRoundKey(password,key)
    return password

def cipherPassword(cipher_text):
    cipher_password = ""
    for i in range(len(cipher_text)):
        for j in range(len(cipher_text[i])):
            hex_number = cipher_text[i][j]
            decimal = int(hex_number,16)%127
            if decimal >= 33:
                character = chr(decimal)
                cipher_password = cipher_password + character
    return cipher_password