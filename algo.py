import key, message, utils, variables, hashlib
from math import sqrt

""" Ask the user to enter his master password and the domain name """
def getInfo():
    master_pwd = input("Master password : ")
    domain = input("Domain name : ")
    return master_pwd, domain

""" Concatenate master password and domain """
def concatInfo(master_pwd, domain):
    concat = master_pwd + domain
    return concat 

""" hash the master password and domain and resize the result by 4 """
def hash(concat):
    length = len(concat)
    res = hashlib.shake_256(concat.encode()).hexdigest(length*4)
    return res

""" Cut the hash into two parts: the msg and the key """
def getMsgAndKey(hash):
    length_over2 = int(len(hash)/2)
    msg = hash[0:length_over2]
    key = hash[length_over2:]
    return msg, key

""" According to the key length, return a nearest length to suit a square matrix """
def chooseKeyLength(key):
    length_for_key = None
    list_of_lengths = []
    # Permit to choose a length to have a square matrix
    for i in range(8,41):
        list_of_lengths.append(i*i)
    for length in list_of_lengths:
        if length < len(key):
            length_for_key = length
        else:
            break
    if not length_for_key: # if key too small => affect 64 for length
        length_for_key = 64
    return length_for_key

""" Cut a string to size a length """
def cutString(string, length):
    return string[0:length]

""" Take as input a string and return an hex matrix """
def stringToHexMatrix(string, length):
    nbr = int(sqrt(length))
    str_hex_list = []
    str_hex_list_sub = []
    count = 1
    for i in range(len(string)):
        str_hex_list_sub.append(format(ord(string[i]), "x"))
        if count%nbr == 0:
            str_hex_list.append(str_hex_list_sub)
            str_hex_list_sub = []
        count += 1
    return str_hex_list

""" Generate nbr_round sub key from cipher_key """
def keySchedule(master_key, nbr_round):
    list_of_key = []
    list_of_key.append(master_key)
    for i in range(nbr_round-1):
        tmp_list = []
        for j in range(len(master_key)):
            if j == 0:
                piece_of_key = key.rotWord(list_of_key[i][-1])
                piece_of_key = key.subBytes(piece_of_key)
                piece_of_key = key.adding3Xor(list_of_key[i][j],piece_of_key,variables.rcon[i])
                tmp_list.append(piece_of_key)
            else:
                piece_of_key = key.adding2Xor(list_of_key[i][j],tmp_list[j-1])
                tmp_list.append(piece_of_key)
        list_of_key.append(tmp_list)
    return list_of_key

def executeRound(msg, list_of_key):
    print("Initial msg : ",msg)
    print("")
    for i in range(len(list_of_key)):
        msg = message.subBytesMsg(msg)
        print("Msg after SubBytes : ",msg)
        print("")
        msg = message.shiftLines(msg)
        print("Msg after shiftLines : ",msg)
        print("")
        rijndael = message.madeRijndaelMixColumns(len(msg))
        msg =  message.mixColumns(msg, rijndael)
        print("Msg after mixColumns : ",msg)
        print("")
    msg = utils.rotateMatrix(msg)
    return msg

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
    h = hash(concat)
    msg, key = getMsgAndKey(h)
    length_Key = chooseKeyLength(key)
    msg = cutString(msg, length_Key)
    key = cutString(key, length_Key)
    tab_msg = stringToHexMatrix(msg, length_Key)
    tab_key = stringToHexMatrix(key, length_Key)
    list_key = keySchedule(tab_key,10)
    msg = executeRound(tab_msg, list_key)
    result = cipherPassword(msg)
    return result