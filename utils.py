""" Display a matrix to be more readable"""
def displayMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def rotateMatrix(msg):
    rotated_msg = [list(row) for row in zip(*msg)]
    return rotated_msg

def displayKeys(matrix):
    for i in range(len(matrix)):
        displayMatrix(matrix[i])
        if i != len(matrix)-1:
            print('\n')
        