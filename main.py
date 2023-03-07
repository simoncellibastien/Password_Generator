import algo

""" To commit on github :
    git add --all
    git commit -m 'Un autre commit'
    git push
"""

""" Main function """
if __name__ == "__main__":
    #master, domain = algo.getInfo()
    master = "My password"
    domain = "www.facebook.com" 
    result = algo.performEncryption(master, domain)
    print("Password :",'\n',result,'\n',"=> length pwd :",len(result))