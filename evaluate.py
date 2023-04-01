from random import randint
from matplotlib import pyplot as plt
import algo

# Convert a binary string into a string
def binToString(bin, tab):
    cpt = 0
    new_str = ""
    for len_cara in tab:
        nbr = ""
        for i in range(cpt, cpt+len_cara):
            nbr += bin[i]
        new_str += chr(int(nbr, 2))
        cpt += len_cara
    return new_str

# Convert a string into a string of binary
def stringToBinString(master):
    my_str = ""
    tab_char = [] # permit to store length of each character
    for character in master:
        tab_char.append(len(bin(ord(character))[2:]))
        my_str += bin(ord(character))[2:]
    return my_str, tab_char

# Perform the evaluation between 2 passwords generated
def performEvaluation(modify_password, real_password):
    modify_str_binary, modify_tab = stringToBinString(modify_password)
    real_str_binary, real_tab = stringToBinString(real_password)
    diff = 0 
    choose_range = min(len(modify_str_binary), len(real_str_binary)) # Get the min legth between the two strings
    for i in range (choose_range):
        if modify_str_binary[i] != real_str_binary[i]:
            diff += 1
    diff += abs(len(modify_str_binary) - len(real_str_binary)) # Add the absolute value of the subtraction of the length of the 2 strings
    max_length = max(len(modify_str_binary), len(real_str_binary))
    percent = (diff/max_length)*100
    return percent, max_length

# All bits to 0
def onlyBit0(master, domain):
    my_str, tab_char = stringToBinString(master) # Convert the password into a string of binary
    my_str = my_str.replace("1","0")

    # binary string to string of char
    master = binToString(my_str, tab_char)
    # Call performEncryption function
    result = algo.performEncryption(master, domain)
    return result

# All bits to 1
def onlyBit1(master, domain):
    my_str, tab_char = stringToBinString(master) # Convert the password into a string of binary
    my_str = my_str.replace("0","1")

    # Decode to string
    master = binToString(my_str, tab_char)
    # Call performEncryption function
    result = algo.performEncryption(master, domain)
    return result

# Bit in sequence of 0 and 1
def seq0and1(master, domain):
    my_str, tab_char = stringToBinString(master) # Convert the password into a string of binary
    
    new_str = ""
    for i in range(0, len(my_str)):
        if i%2 == 0:
            new_str += '0'
        else:
            new_str += '1'
    
    # Decode to string
    master = binToString(new_str, tab_char)
    # Call performEncryption function
    result = algo.performEncryption(master, domain)
    return result

# Change a random bit into master password
def changeBit(master, domain):
    my_str, tab_char = stringToBinString(master) # Convert the password into a string of binary
    choose_rand = randint(0, len(my_str)-1)
        
    # Change into list to modify the character
    temp = list(my_str)
    
    # Modify the bit
    if my_str[choose_rand] == '0':
        temp[choose_rand] = '1'
    else:
        temp[choose_rand] = '0'
    
    # List to string
    my_str = "".join(temp)
    
    # Decode to string
    master = binToString(my_str, tab_char)
    
    # Call performEncryption function
    result = algo.performEncryption(master, domain)
    return result, choose_rand

def getRandomString(length):
    random_str = ""
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(length):
        random_int = randint(0, len(letters)-1)
        random_str += letters[random_int]
    return random_str

def madeHistogram(percent_list):
    length_list = [4,5,6,7,8,9,10,11,12]
    plt.hist(length_list, bins=len(length_list), weights=percent_list)
    plt.xlabel("Length of input password")
    plt.ylabel("Average percentage of bits changed between the two passwords generated")
    plt.show()


def runOver20Times():
    domain = "www.facebook.com"
    master_list = ['abri', 'véron', 'baggie', 'étudier', 'éternuer', 'wagonnier', 'affectueux', 'androphobie', 'tranquillité']
    
    percent_list = []
    for pswd in master_list:
        cpt_percent = 0 # Store percentage difference between the 2 generated passwords
        output = algo.performEncryption(pswd, domain) # Real password
        for i in range (20):
            output_modify, choose_rand = changeBit(pswd, domain) # Password modify
            percent, length = performEvaluation(output_modify, output) # Difference of bits between them
            cpt_percent += percent/20
        percent_list.append(cpt_percent)
    madeHistogram(percent_list)