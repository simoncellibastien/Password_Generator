import algo, evaluate

if __name__ == '__main__':
    
    # master = "My password"
    # domain = "www.facebook.com"
    # master, domain = algo.getInfo()
    # output_modify, choosen_rand = evaluate.changeBit(master, domain)
    # print("After changing bit number", choosen_rand)
    # print(output_modify)
    # print("--------------------------------------------------------------------------------------------------------------------------------")
    # output_modify = evaluate.onlyBit0(master, domain)
    # print("After changing all bit to 0")
    # print(output_modify)
    # print("--------------------------------------------------------------------------------------------------------------------------------")
    # output_modify = evaluate.onlyBit1(master, domain)
    # print("After changing all bit to 1")
    # print(output_modify)
    # print("--------------------------------------------------------------------------------------------------------------------------------")
    # output_modify = evaluate.seq0and1(master, domain)
    # print("After changing password with sequence of 0 and 1")
    # print(output_modify)
    # print("--------------------------------------------------------------------------------------------------------------------------------")
    # output = algo.performEncryption(master, domain)
    # print("Result password without any change")
    # print(output)
    # print("--------------------------------------------------------------------------------------------------------------------------------")
    # percent, length = evaluate.performEvaluation(output_modify, output)
    # print("Percentage difference between the 2 generated passwords :",percent,"% => for a password length max of", length,"bits")
    evaluate.runOver20Times()