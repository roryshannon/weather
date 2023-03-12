#well that was kinda easy i guess? need to check if the key resets tomorrow though
import requests
import sys
from datetime import date
 


import json
  
#oh also regardless I need to make a date var
place = "London"
date = date.today()

place = input("Type a location!")

response = requests.request("GET", f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{place}/{date}/{date}?unitGroup=us&elements=name%2Ctemp%2Cprecip%2Cwindspeed%2Cpressure%2Csunrise%2Cicon&include=current&key=E6NN76EW4SM8X265MB757RJAU&contentType=json")
if response.status_code!=200:
  print('sorry, could not find weather for', place)
  sys.exit()  


# Parse the results as JSON
jsonData = response.json()
        

        
#fucking farenheit so like -32 x 5/9?
wrongTemp = jsonData['days'][0]['temp']
temp = round(((wrongTemp-32) * (5/9)), 1)              
print(f"the temperature in {place} today is " + str(temp))
