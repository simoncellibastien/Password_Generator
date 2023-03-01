import key, encryption, utils, variables
import hashlib

""" Ask the user to enter the master password, the domain name """
def getInfo():
    master_pwd = input("Master password : ")
    domain = input("Domain name : ")
    return master_pwd, domain

""" Concatenate master password and domain name """
def concatInfo(master_pwd, domain):
    concat = master_pwd.replace(" ","") + domain
    concat = hashlib.sha3_256(concat.encode('utf-8')).hexdigest()
    return concat
    
""" Convert string into an hex string """
def convertToHex(string):
    str_hex_list = []
    str_hex_list_sub = []
    count = 1
    for i in range(len(string)):
        str_hex_list_sub.append(format(ord(string[i]), "x"))
        if count%6 == 0:
            str_hex_list.append(str_hex_list_sub)
            str_hex_list_sub = []
        count += 1
        if i == 36:
            return str_hex_list
    return str_hex_list

""" Create the cipher key (288 bits) based on master password and domain """
def madeCipherKey(master, domain):
    len_master = int(len(master)/2)
    len_domain = int(len(domain)/2)
    
    secret = master[0:len_master] + domain[0:len_domain] + master[len_master:] + domain[len_domain:]
    
    hash = hashlib.sha3_256(secret.encode('utf-8')).hexdigest()
    cipher_key = convertToHex(hash)
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
                tmp_list.append(key.addingXor(sub_bytes_key, list_of_key[i],variables.rcon[i%10], j))
            else:
                tmp_list.append(key.addingXorForOthers(tmp_list[j-1],list_of_key[i],j))
        list_of_key.append(utils.rotateMatrix(tmp_list))
        tmp_list = []
    return list_of_key

""" First round  """
def initialRound(password, key):
    return encryption.addRoundKey(encryption.mixColumns(password),key)

""" 9 main rounds """
def mainRound(password, list_of_key):
    for i in range(1,len(list_of_key)-1):
        password = encryption.subBytes(password)
        password = encryption.shiftRows(password)
        password = encryption.mixColumns(password)
        password = encryption.addRoundKey(password,list_of_key[i])
    return password

""" Last round """
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
            decimal = int(hex_number,16)%125
            if decimal >= 33:
                character = chr(decimal)
            else:
                character = chr(decimal+33)
            cipher_password = cipher_password + character
    return cipher_password

def performEncryption(master, domain):
    concat = concatInfo(master, domain)
    text = convertToHex(concat)
    secret_key = madeCipherKey(master, domain)
    list_of_key = keySchedule(secret_key,10)
    password = initialRound(text,secret_key)
    password = mainRound(password, list_of_key)
    cipher_text = finalRound(password, list_of_key[-1])
    result = cipherPassword(cipher_text)
    return result