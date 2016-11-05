import request

def reverse(): 

  #url that gives access to the string that needs to be reversed 
  url = "http://challenge.code2040.org/api/reverse"

  #My personal token
  myToken = "0b051b7208115ccaaa141dc38779ec45f"

  #url that must be returned to validate the reversed string
  urlValidate = "http://challenge.code2040.org/api/reverse/validate"

  tokenReg = requests.post(url, data = myToken)

  #String is reversed by this function
  String = tokenReg.content
  revString = String[::-1]

  #Dictionary that needs to be returned
  newdictionary = {"token": myToken, "string" : revString}

  tokenVal = requests.post(urlValidate, data = newdictionary)

return tokenVal
 
reverse()
