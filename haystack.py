def haystack(): 

  #url that gives access to the dictionary 
  url = "http://challenge.code2040.org/api/haystack"
  #My personal token
  myToken = "0b051b7208115ccaaa141dc38779ec45f"
  #url that must be returned to validate the reversed string
  urlValidate = "http://challenge.code2040.org/api/haystack/validate"
  #Receives the arrays per requests
  tokenReg = requests.post(url, data = myToken)

  #Converts the format of the arrayy 
  lookup = tokenReg.json()

  #Setups the array based on "needle"
  need_array = lookup ["needle"]
  #Setups the array based on "haystack"
  hay_array = lookup ["haystack"]
  #Finds the index of the needle inside of the haystack array
  numNeedle = hay_array.index(need_array)


  #Dictionary that needs to be returned
  newdictionary = {"token": myToken, "needle" : numNeedle}

  tokenVal = requests.post(urlValidate, data = newdictionary)

  return tokenVal
 
haystack()
