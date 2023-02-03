import utils

""" Change the location of the bytes """
def rotWord(last_key):
    utils.displayMatrix(last_key)
    sub_list = []
    for list in last_key:
        sub_list.append(list[-1])
    sub_list.insert(0,sub_list.pop())