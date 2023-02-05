
import utils, variables

""" Change the location of the bytes """
def rotWord(last_key):
    sub_list = []
    for list in last_key:
        sub_list.append(list[-1])
    first = sub_list.pop(0)
    sub_list.append(first)
    return sub_list

""" Substitute a byte with sbox """
def subBytes(piece_of_key):
    sub_list = []
    for bytes in piece_of_key:
        i = int(bytes[0], 16)
        j = int(bytes[1], 16)
        sub_list.append(variables.Sbox[i][j])
    return sub_list

""" Xor 3 list of bytes for the first column of the key"""
def addingXor(sub_key, last_key, rcon, j):
    last_sub_key = []
    final_list = []
    for i in range(len(last_key)):
        last_sub_key.append(last_key[i][j])
    for i in range(0,len(last_key)):
        if i == 0:
            xor = int(sub_key[i],16)^int(last_sub_key[i],16)^int(rcon,16)
            xor = format(ord(chr(xor)), "x").upper()
            if len(xor) != 2:
                xor = '0'+xor
            final_list.append(xor)
        else:
            xor = int(sub_key[i],16)^int(last_sub_key[i],16)^int('00',16)
            xor = format(ord(chr(xor)), "x").upper()
            if len(xor) != 2:
                xor = '0'+xor
            final_list.append(xor)
    return final_list
    
""" Xor 2 list of bytes for the other columns of the key"""
def addingXorForOthers(last_key_1, last_key, j):
    last_sub_key = []
    final_list = []
    for i in range(len(last_key)):
        last_sub_key.append(last_key[i][j])
    
    for i in range(0,len(last_key)):
            xor = int(last_key_1[i],16)^int(last_sub_key[i],16)
            xor = format(ord(chr(xor)), "x").upper()
            if len(xor) != 2:
                xor = '0'+xor
            final_list.append(xor)
    return final_list
