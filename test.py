import hashlib
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
    res = hashlib.shake_256(b"toto").hexdigest(length*4)
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

""" Execute the given functions """
def executeProgram():
    master, domain = "test test test test test test", "www.facebook.com"
    concat = concatInfo(master, domain)
    h = hash(concat)
    msg, key = getMsgAndKey(h)
    length_Key = chooseKeyLength(key)
    msg = cutString(msg, length_Key)
    key = cutString(key, length_Key)
    tab_msg = stringToHexMatrix(msg, length_Key)
    tab_key = stringToHexMatrix(key, length_Key)
    for list in tab_msg:
        print(list)
    
""" Main function """
if __name__ == "__main__":
    executeProgram()