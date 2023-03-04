import variables, utils, copy

""" xor text and round key """
def addRoundKey(text, round_key):
    final_text = []
    tmp_text = []
    tmp_key = []
    tmp_list = []
    for i in range(len(text)):
        for j in range(len(text)):
            tmp_text.append(text[j][i])
            tmp_key.append(round_key[j][i])
        for z in range(len(tmp_text)):
            xor = int(tmp_text[z],16)^int(tmp_key[z],16)
            xor = format(ord(chr(xor)), "x").upper()
            if len(xor) != 2:
                xor = '0'+xor
            tmp_list.append(xor)
        final_text.append(tmp_list)
        tmp_text = []
        tmp_key = []
        tmp_list = []
    return final_text

""" Substitute a bytes with bytes in sbox """
def subBytesMsg(msg):
    sub_list = []
    for list_hexa in msg:
        sub_sub_list = []
        for hexa in list_hexa:
            i = int(hexa[0], 16)
            j = int(hexa[1], 16)
            sub_sub_list.append(variables.Sbox[i][j])
        sub_list.append(sub_sub_list)
    return sub_list

""" Shift by one byte for the second line, two bytes for the third line, three bytes for the last line and so on and so on """
def shiftLines(msg):
    for i in range(0, len(msg)):
        msg = offset(msg, i)
    return msg

""" Shift a row """
def offset(matrix, nbr):
    for i in range(0,nbr):
        byte = matrix[nbr].pop(0)
        matrix[nbr].append(byte)
    return matrix

def madeRijndaelMixColumns(length):
    sub_list = []
    values = ['02', '01', '01', '03']
    rijndael = ['02', '01', '01', '03']
    length_rijndael = len(rijndael)
    # Add rijndael pattern as long as the key length is not reached
    while length_rijndael < length:
        for x in values:
            rijndael.append(x)
        length_rijndael = len(rijndael)
    # Cut to suits the key length
    rijndael = rijndael[0:length]
    # Make a shift for each lines to suits Rijndael's Galois field
    for i in range(length):
        sub_list.append(offsetRijndael(copy.deepcopy(rijndael), i))
    return sub_list

def offsetRijndael(sub_list, j):
    for i in range(0,j):
        hexa = sub_list.pop(-1)
        sub_list.insert(0, hexa)
    return sub_list

""" Mul rijandael by each column in msg """
def mixColumns(msg, rijndael):
    msg_list = []
    final_msg = []
    tmp_list = []
    
    for j in range(len(msg)):
        for i in range(len(msg)):
            msg_list.append(msg[i][j])
        for list in rijndael:
            tmp_list.append(firstColumn(msg_list, list))
        final_msg.append(tmp_list)
        msg_list = []
        tmp_list = []
    
    return final_msg
    
def firstColumn(column, list):
    byte_list = []
    for byte in column:
        """ Convert hex to bin """
        byte_list.append("{0:08b}".format(int(byte, 16)))
    
    byte_xor = '00011011'
    
    tmp_list = []
    for i in range(len(list)):
        if list[i] == '01':
            tmp_list.append(format(int(byte_list[i],2), 'x').upper())
        elif list[i] == '02':
            """ xor with byte_xor if the leftmost is a 1 before shift"""
            if byte_list[i][0] == '1':
                tmp_list.append(format(int(leftShiftOne(byte_list[i]),2)^int(byte_xor,2), 'x').upper())
            else: 
                tmp_list.append(format(int(leftShiftOne(byte_list[i]),2), 'x').upper())
        elif list[i] == '03':
            """ xor with byte_xor if the leftmost is a 1 before shift"""
            if byte_list[i][0] == '1':
                tmp_list.append(format(int(leftShiftOne(byte_list[i]),2)^int(byte_xor,2)^int(byte_list[i],2), 'x').upper())
            else:
                tmp_list.append(format(int(leftShiftOne(byte_list[i]),2)^int(byte_list[i],2), 'x').upper())
    
    res = format(int(tmp_list[0],16)^int(tmp_list[1],16)^int(tmp_list[2],16)^int(tmp_list[3],16), 'x').upper()
    if len(res) != 2:
        res = '0'+res
    return res

def leftShiftOne(binary):
    binary = list(binary)
    binary.pop(0)
    binary.append('0')
    return ''.join(binary)