import algo, cgi, json

def main():
    # Get content of master and domain from javascript
    # form = cgi.FieldStorage()

    # master = form.getvalue("master")
    # domain = form.getvalue("domain")

    master = "My password"
    domain = "www.facebook.com"
    result = algo.performEncryption(master, domain)

    response = {"result": result}
    print('Content-Type: application/json')
    print('')
    print(json.dumps(response))

""" Main function """
if __name__ == "__main__":
    main()