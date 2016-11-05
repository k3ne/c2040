import request

def dating(): 

      #url that gives access to the dictionary 
      url = "http://challenge.code2040.org/api/dating"
      #My personal token
      myToken = "0b051b7208115ccaaa141dc38779ec45f"
      #url that must be returned to validate the array
      urlValidate = "http://challenge.code2040.org/api/dating/validate"
      #Receives the arrays per request
      tokenReg = requests.post(url, data = myToken)

      #Converts the format of the array
      lookup = tokenReg.json()

      #Finds date inside of the dictionary
      date = lookup ["datestamp"]
      #Finds the time interval that needs to be added to "datestamp"
      interval = lookup ["interval"]

      #Converts the string into the proper date and time form
      formatDate = dateutil.parser.parse(date)

      #Adds seconds to the date format
      timeDate = formatDate + datetime.timedelta(seconds = interval)

      #Returns the string in the proper ISO 8601 format
      finalDate = timeDate.isoformat()

      #Removes "+00.00" and replaces it with "Z"
      data = timeDate.replace("+00.00", "Z")


      #Dictionary that needs to be returned
      newdictionary = {"token": myToken, "datestamp" : data}

      tokenVal = requests.post(urlValidate, data = newdictionary)

      return tokenVal
 
dating()
