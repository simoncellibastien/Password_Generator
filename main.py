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
    
    # concat = algo.concatInfo(master, domain)
    # hex_str = algo.convertToHex(concat)
    # secret_key = algo.madeCipherKey(hex_str)
    #text = [['04','E0','48','28'],['66','CB','F8','06'],['81','19','D3','26'],['E5','9A','7A','4C']]
    #secret_key = [['2B','28','AB','09'],['7E','AE','F7','CF'],['15','D2','15','4F'],['16','A6','88','3C']]
    #secret_key = [['A0','88','23','2A'],['FA','54','A3','6C'],['FE','2C','39','76'],['17','B1','39','05']]
    #password = [['19','A0','9A','E9'],['3D','F4','C6','F8'],['E3','E2','8D','48'],['BE','2B','2A','08']]
    secret_key = [['2B','28','AB','09'],['7E','AE','F7','CF'],['15','D2','15','4F'],['16','A6','88','3C']]
    text = [['32','88','31','E0'],['43','5A','31','37'],['F6','30','98','07'],['A8','8D','A2','34']]
    list_of_key = algo.keySchedule(secret_key,10)
    password = algo.initialRound(text,secret_key)
    password = algo.mainRound(password, list_of_key)
    cipher_text = algo.finalRound(password, list_of_key[-1])
    print(cipher_text)