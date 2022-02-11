import requests

import sys
 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])

 
api_key = str(sys.argv[1])
#125a9f673322623d783984c5e6cdc621
#script to 
#url = "https://api.openweathermap.org/data/2.5/weather?lat=12.9&lon=77.5&appid=125a9f673322623d783984c5e6cdc621"
url= "https://api.openweathermap.org/data/2.5/weather?lat=12.9&lon=77.5&appid="+api_key

temperature_data = requests.get(url)
main = temperature_data.json()['main']
temperature = main['temp']
print("temp is ", temperature)
with open("temperatures.txt", "a") as file_handler:
    file_handler.write(str(temperature) + "\n")
