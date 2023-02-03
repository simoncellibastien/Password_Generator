import key, utils

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

""" Generate x sub key from cipher_key """
def keySchedule(cipher_key, nbr_round):
    list_of_key = []
    list_of_key.append(cipher_key)
    for i in range(0, nbr_round):
        key.rotWord(list_of_key[i])