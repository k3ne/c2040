import requests


def register():

    #Website
    url =  "http://challenge.code2040.org/api/registration"

    #Set ups dictionary with proper values to post
    dictionary = {"token": "0b051b7208115ccaaa141dc3879ec45f", "github" : "https://github.com/k3ne/c2040"}

    #Post Request to the website
    tokenReg = requests.post(url, data = dictionary)

    print tokenReg
    return tokenReg



register()
