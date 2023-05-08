import requests
import json
class ISS(): 
    def __init__(self, iss_code = "25544"): 
        '''
        This function sets up the weather API URL with the query the ISS satelite code.
        Args: self, (str) iss_code is the ISS satelite code.
        Return: None 
        '''
        self.url = f"https://api.wheretheiss.at/v1/satellites/{iss_code}"
    def get_data(self): 
        '''
        This function uses json to parse the data for latitude and longitude of the ISS. 
        Args: self
        Return: (tuple) iss_lat(str), iss_long(str) this is the latitide and longitude of the ISS
        '''
        data = requests.get(self.url)
        json_data = data.json() 
        iss_lat = json_data["latitude"]
        iss_long = json_data["longitude"]
        return (iss_lat, iss_long)
   

