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
    secret_key = [['2B','28','AB','09'],['7E','AE','F7','CF'],['15','D2','15','4F'],['16','A6','88','3C']]
    list_of_key = algo.keySchedule(secret_key,2)
    utils.displayKeys(list_of_key)