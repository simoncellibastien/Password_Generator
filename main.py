import algo, utils

""" To commit on github :
    git add --all
    git commit -m 'Un autre commit'
    git push
"""

""" Main function """
if __name__ == "__main__":
    # master, domain = algo.getInfo()
    master = "this is a master password test"
    domain = "facebook.com"
    
    concat = algo.concatInfo(master, domain)
    text = algo.convertToHex(concat)
    secret_key = algo.madeCipherKey(text)
    # secret_key = [['2B','28','AB','09'],['7E','AE','F7','CF'],['15','D2','15','4F'],['16','A6','88','3C']]
    # text = [['32','88','31','E0'],['43','5A','31','37'],['F6','30','98','07'],['A8','8D','A2','34']]
    list_of_key = algo.keySchedule(secret_key,10)
    password = algo.initialRound(text,secret_key)
    password = algo.mainRound(password, list_of_key)
    cipher_text = algo.finalRound(password, list_of_key[-1])
    result = algo.cipherPassword(cipher_text)
    print(result)