def prefix(): 

    #url that gives access to the dictionary 
    url = "http://challenge.code2040.org/api/prefix"
    #My personal token
    myToken = "0b051b7208115ccaaa141dc38779ec45f"
    #url that must be returned to validate the array
    urlValidate = "http://challenge.code2040.org/api/prefix/validate"
    #Receives the arrays per requests
    tokenReg = requests.post(url, data = myToken)

    #Converts the format of the array
    lookup = tokenReg.json()

    #Finds the prefix that needs to found
    pre_array = lookup ["prefix"]
    #Setups the array based on "array"
    new_array = lookup ["array"]
    #Creates an empty list to contain the word 
    new_list = []

    #The loop iterates through the array and adds words that do not contain the prefix 
    for value in new_array: 
      if value.find(pre_array) == -1;
        new_list.append(value)



    #Dictionary that needs to be returned
    newdictionary = {"token": myToken, "array" : new_list}

    tokenVal = requests.post(urlValidate, data = newdictionary)

    return tokenVal
 
prefix()
