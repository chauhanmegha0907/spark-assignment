# File: api_requests.py
import requests
import csv

def fetch_covid_data():
    url = "https://disease.sh/v3/covid-19/countries/"

    query_countries = ["USA", "India", "Brazil", "Russia", "France", "Germany", "UK", "Italy", "Turkey", "Argentina",
                       "Spain", "Colombia", "Poland", "Iran", "Mexico", "Ukraine", "Peru", "South Africa", "Netherlands", "Indonesia"]

    for country in query_countries:
        response = requests.get(url + country)
        data = response.json()


# Example data and country name
data = {'Date': '2024-05-01', 'Cases': 1000, 'Deaths': 50}
country = 'USA'

# Specifying the full path where you want to save the CSV file
file_path = '/Users/meghasingh/Desktop/Spark assignment/api_folder'

# Constructing the filename with the full path
filename = f"{file_path}{country.lower()}_covid_data.csv"

# Write data to CSV
with open(filename, 'w', newline='') as csvfile:
    fieldnames = data.keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(data)

if __name__ == "__main__":
    fetch_covid_data()
