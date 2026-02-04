#Weather App (API Integration)
#import requests library
import requests
#define base url from free weather api
base_url = "http://api.weatherapi.com/v1/current.json"
#after signup, recieve api key and import from environment file (env)
#import dotenv module to hide API key
from dotenv import load_dotenv
import os  
load_dotenv()
api_key = os.getenv("WEATHERAPI_KEY") 

#define get weather data function with parameter input location.
def getweather(location):
    #format/define full url based on variables and inputs (formatting details from weatherapi website)
    url = f"{base_url}?key={api_key}&q={location}&aqi=no"
    #get() method to read url data
    response = requests.get(url)
    #if url is found, the api code 200 will be pushed through so continue code
    if response.status_code == 200:
        #generate dictionary response using json()
        weather_data = response.json()
        #return large dictionary to main code
        return weather_data
    else:
        #if failed, let user know
        return "Data failed to retrieve!"

#welcome to user with sunny cloud emojis
print("\U0001F324\U0000FE0F   Welcome to Weather App! \U0001F324\U0000FE0F")
#loop to continue use of application till finished
while True:
    #menu with ANSI escape code formatting 
    choice = input("""\nPlease choose an option:
\033[91m1. \033[0mCheck Weather
\033[91m2. \033[0mExit 
Your choice: """)
    #if the user enters 1, reformat the input to match api sites style and find data
    if choice == '1':
        ul = input("\n\U0001F30E Please enter a location: ")
        ul = ul.title()
        weatherdata = getweather(ul)
        #return location details, temperature in celsius and condition from large dictionary
        if isinstance(weatherdata, str) == False:
            print(f"\n\U0001F4CD Location: {weatherdata['location']['name']}, {weatherdata['location']['region']}, {weatherdata['location']['country']}\n\U0001F321\U0000FE0F  Temperature: {weatherdata['current']['temp_c']} °C\n\U00002601\U0000FE0F  Condition: {weatherdata['current']['condition']['text']}")
        #if function getweather() threw an error and returned a string, print the message instead
        else:
            print(weatherdata)
    #if option was 2, break the loop stopping the program and finish
    elif choice == '2':
        print("\nThank you for using Weather App!")
        break
    else:
        #alert user for invalid option inputs
        print("\nInvalid input, please try again!")
