from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("COVID-19 Data API") \
    .getOrCreate()


# Define the request handler class
class RequestHandler(BaseHTTPRequestHandler):
    
    # Define the response headers
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
    
    # Define the GET method to handle requests
    def do_GET(self):
        # Set response headers
        self._set_response()
        
        # Read the CSV file into a Pandas DataFrame
        covid_data = spark.read.csv('covid_data.csv', header=True)
        
        # Select only the required fields (country, cases, deaths)
        selected_data = covid_data.select("country", "cases", "deaths")
        
        # Convert DataFrame to JSON format
        json_data = selected_data.toJSON().collect()
        
        # Convert JSON string to Python dictionary
        json_dict = [json.loads(row) for row in json_data]
        
        # Send the JSON response with pretty formatting
        self.wfile.write(json.dumps(json_dict, indent=4).encode('utf-8'))

# Define the server address
server_address = ('', 8000)

# Create and run the HTTP server
with HTTPServer(server_address, RequestHandler) as httpd:
    print('Server started on port 8000...')
    httpd.serve_forever()

#API CREATED
# http://localhost:8000/covid-data