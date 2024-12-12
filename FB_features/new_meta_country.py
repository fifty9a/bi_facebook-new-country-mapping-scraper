import requests as r
import pandas as pd
import numpy as np
from threading import Thread

from FB_features.system import System

class NewMetaCountryMapping():
    def __init__(self):
        self.access_token  = System().get_access_token()
        self.base_url      = 'https://graph.facebook.com/v21.0/search'
        self.count         = 0


    def check_compatibility_zipcode(self, country_code, popular_zipcode):
        params = {
            'type': 'adgeolocation',
            'location_types': ['zip'],
            'country_code': country_code,
            'q': popular_zipcode,
            'access_token': self.access_token,
        }

        response = r.get(self.base_url, params=params).json().get('data')
        if response == None or len(response) < 1:
            print(f"No data was found for:\n-> zipcode: {popular_zipcode}\n-> country: {country_code}\n\nEither Meta doesn't support zipcodes for this country or try a different popular zipcode")
        else:
            print(f"Results for zipcode: {popular_zipcode}\n\n{pd.DataFrame(response).head(5).to_string()}")


    def check_compatibility_city(self, country_code, popular_city):
        params = {
            'type': 'adgeolocation',
            'location_types': ['city'],
            'country_code': country_code,
            'q': popular_city,
            'access_token': self.access_token,
        }

        response = r.get(self.base_url, params=params).json().get('data')
        if response == None or len(response) < 1:
            print(f"No data was found for:\n-> city: {popular_city}\n-> country: {country_code}\n\nEither Meta doesn't support cities for this country or try a different popular city")
        else:
            print(f"Results for city: {popular_city}\n\n{pd.DataFrame(response).head(5).to_string()}")

    def __get_data(self, country_code, geo_level, postcodes):
        global count
        
        for postcode in postcodes:
            self.count += 1
            results = r.get(f'https://graph.facebook.com/v21.0/search?access_token=&type=adgeolocation&location_types=%5B%22{geo_level}%22%5D&q={postcode}&country_code={country_code}&access_token={self.access_token}')
            results = results.json()
            print(results)
            
            for data in results['data']:
                self.geo_results.append(data)
        
            print(f"Completed {self.count} / {len(self.xandr_mapping)}")

    def start_scrape(self, threads,country_code, geo_level, xandr_mapping, geo_column):
        self.xandr_mapping = xandr_mapping

        xandr_mapping   = xandr_mapping[geo_column].to_list()
        locations_split = np.array_split(xandr_mapping, threads)
        self.geo_results= []

        threads_array = []

        for i in range(threads):
            threads_array.append(Thread(target=self.__get_data,args=(country_code, geo_level, locations_split[i],)))

        for thread in threads_array:
            thread.start()
        
        for thread in threads_array:
            thread.join()

        df_geo_results = pd.DataFrame(self.geo_results)
        df_geo_results = df_geo_results.drop_duplicates(subset='key')
        df_geo_results.to_json(f'./{country_code}_{geo_level}.json',orient='records')
        print("Saved copy as .json file")
        return df_geo_results






