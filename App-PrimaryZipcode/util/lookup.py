##encoding=utf-8

"""
A fuzzy search engine module to lookup zipcode detail info by zipcode, city, state.
city name and state name doesn't have to be exactly right.

Import Command
--------------
    from util.lookup import lookup
"""

try:
    from .constant import state_abbr
    from .database import engine, zipcodes
except: # for in-script unittest use only
    from constant import state_abbr
    from database import engine, zipcodes
from angora.SQLITE import *
from angora.STRING.stringmatch import smatcher

class LookUp():
    def __init__(self):
        self.state_abbr = dict()
        for key, value in list(state_abbr.items()):
            self.state_abbr[value] = key
        for key in state_abbr.keys():
            self.state_abbr[key] = key
        self.state_name = list(state_abbr.keys())
        self.state_name.sort()
        
    def validate_state(self, state):
        """fuzzy analysis and find the correct state name in 2-letter abbreviation format
        """
        correct_state = smatcher.choose(state, self.state_name) # fuzzy choose the correct state name
        if correct_state in self.state_abbr:
            return self.state_abbr[correct_state]
        else:
            raise Exception("%s is not a valid state name." % state)
        
    def by_zipcode(self, zipcode):
        """search by zipcode, take integer or string
        """
        if isinstance(zipcode, int): # if not string, convert to string
            zipcode = str(zipcode).zfill(5)
        results = list(engine.select_row(Select(zipcodes.all).where(zipcodes.zipcode == zipcode)))
        if len(results) == 0:
            print("No zipcode match '%s' in our database." % zipcode)
            return None
        elif len(results) == 1:
            return results[0]
   
    def by_city_state(self, city, state):
        """Fuzzy search city, state
        """
        correct_state = self.validate_state(state)
        city_list = engine.select_column(Select([zipcodes.city]).\
                                         where(zipcodes.state == correct_state))["city"]
        correct_city = smatcher.choose(city, city_list)

        results = list(engine.select_row(Select(zipcodes.all).\
                          where(zipcodes.city == correct_city, 
                                zipcodes.state == correct_state)))
        if len(results) == 0:
            print("No zipcode match city = '%s', state = '%s'." % (correct_city, correct_state))
            return None
        elif len(results) == 1:
            return results[0]
        else:
            return results
    
    def by_city(self, city):
        """Fuzzy search city
        """
        city_list = engine.select_column(Select([zipcodes.city]))["city"]
        correct_city = smatcher.choose(city, city_list)
        
        results = list(engine.select_row(Select(zipcodes.all).\
                          where(zipcodes.city == correct_city)))
        if len(results) == 0:
            print("No zipcode match city = '%s'." % correct_city)
            return None
        elif len(results) == 1:
            return results[0]
        else:
            return results
        
lookup = LookUp()

if __name__ == "__main__":
    for row in lookup.by_city("gaithersburg"):
        print(row)
    
