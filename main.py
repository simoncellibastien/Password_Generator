import algo

if __name__ == '__main__':
    
    master = "My password"
    domain = "www.facebook.com"
    # output_modify, choosen_rand = algo.ChangeBit(master, domain)
    # print("After changing bit number", choosen_rand)
    # print(output_modify)
    # print("--------------------------------------------------------------------------------------------------------------------------------")
    # output_modify = algo.onlyBit0(master, domain)
    # print("After changing all bit to 0")
    # print(output_modify)
    # print("--------------------------------------------------------------------------------------------------------------------------------")
    # output_modify = algo.onlyBit1(master, domain)
    # print("After changing all bit to 1")
    # print(output_modify)
    # print("--------------------------------------------------------------------------------------------------------------------------------")
    output_modify = algo.seq0and1(master, domain)
    print("After changing password with sequence of 0 and 1")
    print(output_modify)
    print("--------------------------------------------------------------------------------------------------------------------------------")
    output = algo.performEncryption(master, domain)
    print("Result password without any change")
    print(output)
    print("--------------------------------------------------------------------------------------------------------------------------------")