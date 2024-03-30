In response to the global COVID-19 pandemic,the project aims at creating a comprehensive system for analyzing and presenting COVID-19 data from various countries. Leveraging Python, RapidAPI, Spark, and RESTful APIs, I developed a solution to collect, process, and analyze COVID-19 data for at least 20 countries. The project not only involves gathering raw data but also focuses on deriving meaningful insights to better understand the impact of the pandemic across different regions.

Data Collection:
Using the RapidAPI service, I accessed the 'https://disease.sh/v3/covid-19/countries/{country_name}' API to retrieve the latest COVID-19 data for a diverse set of countries. This data includes information such as total confirmed cases, total deaths, total recoveries, and critical cases. I meticulously compiled this data and organized it into a CSV file for further analysis.

Data Processing:
To efficiently process the collected data, I utilized Apache Spark to create a DataFrame, enabling fast and scalable data manipulation. 

Key Insights:
Through rigorous analysis of the COVID-19 data, I unearthed several key insights:

Most Affected Country: By calculating the ratio of total deaths to total confirmed cases, I identified the country that has been most severely impacted by the pandemic.

Least Affected Country: Conversely, I pinpointed the country that has experienced the least impact by determining the ratio of total deaths to total confirmed cases.

Country with Highest COVID Cases: I determined the country with the highest number of confirmed COVID-19 cases, providing valuable information on the severity of the outbreak in different regions.

Country with Minimum COVID Cases: Similarly, I identified the country with the minimum number of confirmed COVID-19 cases, shedding light on regions with relatively lower infection rates.

Total Cases: By aggregating the total number of confirmed COVID-19 cases across all countries, I obtained a comprehensive overview of the global situation.

Most Efficiently Handling Country: Through analysis of the ratio of total recoveries to total confirmed cases, I highlighted the country that has effectively managed the pandemic by maximizing recovery rates.

Least Efficiently Handling Country: Conversely, I identified the country that has struggled to contain the virus based on a low ratio of total recoveries to total confirmed cases.

Country Least Suffering from COVID: By examining the number of critical COVID-19 cases in each country, I identified regions with relatively fewer severe cases.

Country Still Suffering from COVID: On the other hand, I identified the country with the highest number of critical COVID-19 cases, signaling ongoing challenges in managing the pandemic.

Conclusion:
In conclusion,the project offers a comprehensive solution for analyzing and presenting COVID-19 data, providing valuable insights into the global impact of the pandemic. 





Link to access all the APIS - file:///Users/meghasingh/Desktop/Spark%20assignment/covid_apis.html
![alt text](https://github.com/chauhanmegha0907/spark-assignment/blob/main/Screenshot%202024-03-29%20at%2012.47.03%20PM.png)
