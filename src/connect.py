import requests,csv,os,pandas as pd
from dotenv import load_dotenv

# load.env file from the enviroment
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'config', '.env')
load_dotenv(dotenv_path)

RAPIDAPI_URL=os.getenv("RAPIDAPI_URL")
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")

# masked senstive information
url=RAPIDAPI_URL
headers = {
	"X-RapidAPI-Key": RAPIDAPI_KEY,
	"X-RapidAPI-Host": RAPIDAPI_HOST
}

# added try-catch block to handle exceptions during HTTP requests
try:
    response = requests.get(url, headers=headers)
    data=response.json()['response']
# my csv file name 
    csv_file="my_file.csv" 
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
    # Write header row
    # This will provide schema to dataframe later
        writer.writerow(['Country','Total_Death','Total_Recovered','Total_Cases','Critical'])
    # Iterate over jsonData and write each country data into csv file 
        for countryData in data:
                writer.writerow([countryData['country'],countryData['deaths']['total'],countryData['cases']['recovered'],
                              countryData['cases']['total'],countryData['cases']['critical']])
except requests.exceptions.RequestException as e:
    # Handle any exceptions that occurred during the request
    print("Error during HTTP request:", e)



            

