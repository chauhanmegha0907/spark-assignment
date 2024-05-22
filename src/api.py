import http.server,socketserver,json,os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum
from pyspark.sql.types import *
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'config', '.env')
load_dotenv(dotenv_path)

# Initialize SparkSession
spark = SparkSession.builder.appName("CovidDataAnalyzer").getOrCreate()

schema = StructType([
    StructField("Country", StringType(), nullable=True),
    StructField("Total_Death", LongType(), nullable=True),
    StructField("Total_Recovered", LongType(), nullable=True),
    StructField("Total_Cases", LongType(), nullable=True),
    StructField("Critical", LongType(), nullable=True)
])

# Load the CSV file into a PySpark DataFrame
df= spark.read.option("header", "true").schema(schema).csv("my_file.csv")
# basic data cleansing 
df = df.filter(~col('Country').isin(['All', 'Europe', 'Oceania', 'North-America','South-America','R&eacute;union','MS-Zaandam','Diamond-Princess','Caribbean-Netherlands','Sint-Maarten','CAR','French-Guiana','DPRK','Asia']))
df = df.filter(df['Total_Recovered'].isNotNull()).filter(df['Total_Cases'].isNotNull()).filter(df['Total_Death'].isNotNull())

# Calculate required metrics
def collected_data():
    return df.collect()

# created separate functions (memory cleanup) 
def most_affected_country():
    return  df.withColumn("affected_ratio", col("Total_Death") / col("Total_Cases")) \
    .orderBy(col("affected_ratio").desc()) \
    .select("Country", "affected_ratio") \
    .limit(1) \
    .collect()
def least_affected_country():
    return df.withColumn("affected_ratio", col("Total_Death") / col("Total_Cases")) \
    .orderBy(col("affected_ratio")) \
    .select("Country", "affected_ratio") \
    .limit(1) \
    .collect()
def highest_cases_country():
    return df.orderBy(col("Total_Cases").desc()) \
    .select("Country", "Total_Cases") \
    .limit(1) \
    .collect()
def minimum_cases_country():
    return df.orderBy(col("Total_Cases")) \
    .select("Country", "Total_Cases") \
    .limit(1) \
    .collect()

def total_cases():
    return df.agg(sum("Total_Cases")).collect()[0][0]

def most_efficient_country():
    return df.withColumn("efficiency", col("Total_Recovered") / col("Total_Cases")) \
    .orderBy(col("efficiency").desc()) \
    .select("Country", "efficiency") \
    .limit(1) \
    .collect()

def least_efficient_country():
    return  df.withColumn("efficiency", col("Total_Recovered") / col("Total_Cases")) \
    .orderBy(col("efficiency")) \
    .select("Country", "efficiency") \
    .limit(1) \
    .collect()
def least_suffering_country():
    return df.filter(col('Critical').isNotNull()).orderBy(col("Critical")) \
    .select("Country", "Critical") \
    .limit(1) \
    .collect()
def most_suffering_country():
    return df.filter(col('Critical').isNotNull()).orderBy(col("Critical").desc()) \
    .select("Country", "Critical") \
    .limit(1) \
    .collect()

# added one to one mapping to reduce code redundancy
data_map = {
    '/collected_data': collected_data,
    '/most_affected_country': most_affected_country,
    '/least_affected_country': least_affected_country,
    '/highest_cases_country': highest_cases_country,
    '/minimum_cases_country': minimum_cases_country,
    '/total_cases': total_cases,
    '/most_efficient_country': most_efficient_country,
    '/least_efficient_country': least_efficient_country,
    '/least_suffering_country': least_suffering_country,
    '/most_suffering_country': most_suffering_country
}

# Define a HTTP request handler class
class CovidDataHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # added a dataMap to remove code redundancy
        # Check if the requested path exists in the data map
        if self.path in data_map:
            data = data_map[self.path]()
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data, indent=4).encode())
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('static/covid_data.html', 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

# Set up the HTTP server
# added global constant variable in dotenv file with default value as 8001            
PORT = int(os.getenv("PORT", 8001)) 
# added try catch to handle exceptions
try:
    with socketserver.TCPServer(("", PORT), CovidDataHandler) as httpd:
        print(f"Server running on port {PORT}")
        httpd.serve_forever()
except Exception as e:
    print(f"Error occurred: {e}")

