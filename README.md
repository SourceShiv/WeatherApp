# WeatherApp
This project uses a weather API to inform us of the weather internationally.

## Features
- Requests library
- Web APIs
- env files to store API keys for security - using gitignore to ignore this key (invalid expired key uploaded as well just in case)
- API code error catching
- Conditional statements and loops
- Unicode, ANSI, and special escape characters to improve graphical side of the console app

## Tech stack
- Python
- Python requests library
- WeatherAPI

## How to Run

1. Make sure Python 3 is installed
2. Clone the repository
4. Create a .env file with the API key, the file should only have this in it: " WEATHERAPI_KEY = "<key>" " - may need to navigate to https://api.weatherapi.com to retrieve a valid key
5. Open a terminal in the project folder
6. Install dependencies:

```bash
pip install -r requirements.txt
```
6. Run:

```bash
python main.py
```
Tested on Python 3.11.9
