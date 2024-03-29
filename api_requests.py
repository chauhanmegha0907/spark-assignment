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

        # Write data to CSV
        filename = f"{country.lower()}_covid_data.csv"
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = data.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(data)

if __name__ == "__main__":
    fetch_covid_data()
