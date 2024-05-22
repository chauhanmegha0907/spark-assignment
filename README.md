# SparkAssignment

Steps to run the spark project in localhost:
  1. Run the connect.py file .
  2. Run the api.py file.
  3. go to localhost 8000 .


## Files Description
  ### CONNECT.PY 
      The program retrieves COVID data for all countries from the Rapid API and saves the data in a file named "my_csv".
  ### API.py
      The script utilizes the "my_csv" file to generate a DataFrame. It employs core Spark to address all inquiries using built-in Spark       functions. Additionally, it utilizes the http.server module to establish a REST API for handling all queries.
  ### Covid_data.html
      The script incorporates an HTML file named "covid_data.html" to provide a user-friendly graphical interface for navigating through       solutions to various queries.
  ### my_file.csv
      Initally this file will not be present.
      Just run connect.py and this csv file will be created.
      This is the dataset that contains all covid-19 data for all countries.
  ### requirements.txt
      Run the command <pip install -r requirements.txt> to install all dependencies
      