import requests 
from iss import ISS
import json

class Weather(): 
    def __init__(self, query = ISS.get_data):
        '''
        This function sets up the weather API URL with the query set to the ISS current coordinates.
        Args: self, (tuple) ISS current coordinates with lat and long as (str)
        Return: None 
        '''
        self.url = f'http://api.weatherstack.com/current?access_key=b7d65f84a4bc06f7b261e84d3d10a169&query={query}'
    def get(self): 
        '''
        This function loads the data from the API and uses JSON to parse the data for the necessary attributes. 
        Args: self
        Returns: (list) results, containing the city(str), country(str), precipitation coverage(float), UV index(int), and temperature in Celsius(int)
        '''
        data = requests.get(self.url).text
        parse_json = json.loads(data)
        city = str(parse_json["location"]["region"])
        country = str(parse_json["location"]["country"])
        precipitation = float(parse_json["current"]["precip"])
        uv_index = int(parse_json["current"]["uv_index"])
        temperature = int(parse_json["current"]["feelslike"])
        results = [city, country, precipitation, uv_index, temperature]
        return results
    def convert_to_F(self, tempc):
        '''
        This function converts Celsius to Fahrenheit. 
        Args: self, int(tempc) temperature in Celsius 
        Returns: int(tempf) temperature in Fahrenheit
        '''
        tempf = tempc * (1.8) + 32
        return tempf
        

        

