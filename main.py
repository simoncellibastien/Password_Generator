import algo

if __name__ == "__main__":
    # master, domain = algo.getInfo()
    master = "this is a master password test"
    domain = "facebook.com"
    
    concat = algo.concatInfo(master, domain)
    hex_str = algo.convertToHex(concat)
    secret_key = algo.madeCipherKey(hex_str)
    algo.keySchedule(secret_key,1)
    