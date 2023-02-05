import variables, utils

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
    final_text = utils.rotateMatrix(final_text)
    return final_text

""" Substitute a bytes with bytes in sbox """
def subBytes(matrix):
    final_matrix = []
    tmp_list = []
    for list_bytes in matrix:
        for bytes in list_bytes:
            i = int(bytes[0], 16)
            j = int(bytes[1], 16)
            tmp_list.append(variables.Sbox[i][j])
        final_matrix.append(tmp_list)
        tmp_list = []
    return final_matrix

""" Shift by one byte for the second line, two bytes for the third line, three bytes for the last line """
def shiftRows(matrix):
    for i in range(0, len(matrix)):
        matrix = offset(matrix, i)
    return matrix

""" Shift a row """
def offset(matrix, nbr):
    for i in range(0,nbr):
        byte = matrix[nbr].pop(0)
        matrix[nbr].append(byte)
    return matrix

""" Mul rijandael by each column in matrix """
def mixColumns(matrix):
    matrix_list = []
    final_matrix = []
    tmp_list = []
    
    for j in range(len(matrix)):
        for i in range(len(matrix)):
            matrix_list.append(matrix[i][j])
        for list in variables.rijindael:
            tmp_list.append(firstColumn(matrix_list, list))
        final_matrix.append(tmp_list)
        matrix_list = []
        tmp_list = []
    
    final_matrix = utils.rotateMatrix(final_matrix)
    return final_matrix
    
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