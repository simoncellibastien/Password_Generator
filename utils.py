""" Display a matrix to be more readable"""
def displayMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def rotateMatrix(matrix):
    final_list = []
    for i in range(0,6):
        final_list.append([matrix[0][i],matrix[1][i],matrix[2][i],matrix[3][i],matrix[4][i],matrix[5][i]])
    return final_list

def displayKeys(matrix):
    for i in range(len(matrix)):
        displayMatrix(matrix[i])
        if i != len(matrix)-1:
            print('\n')
        