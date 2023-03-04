import variables

""" Change the location of the bytes """
def rotWord(list_key):
    hexa = list_key.pop(0)
    list_key.append(hexa)
    return list_key

""" Substitute a byte with sbox """
def subBytes(piece_of_key):
    sub_list = []
    for bytes in piece_of_key:
        i = int(bytes[0], 16)
        j = int(bytes[1], 16)
        sub_list.append(variables.Sbox[i][j])
    return sub_list

""" Allow to xor 3 hex """
def adding3Xor(wi4, wi, rcon):
    final_list = []
    for i in range(len(wi)):
        if i == 0:
            result = int(wi4[i], 16) ^ int(wi[i] ,16) ^ int(rcon, 16)
        else:
            result = int(wi4[i], 16) ^ int(wi[i] ,16) ^ int('00', 16)
        result = format(ord(chr(result)), "x").upper()
        if len(result) != 2:
            result = '0' + result
        final_list.append(result)
    return final_list

""" Allow to xor 2 hex """
def adding2Xor(wi4, wi):
    final_list = []
    for i in range(len(wi)):
        result = int(wi4[i], 16) ^ int(wi[i] ,16)
        result = format(ord(chr(result)), "x").upper()
        if len(result) != 2:
            result = '0' + result
        final_list.append(result)
    return final_list