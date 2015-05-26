##encoding=utf-8

from angora.GEO import *
from angora.SQLITE import *
from util.database import engine, zipcodes

google = GoogleGeocoder()
google.set_sleeptime(1.0)
 
zipcode_list = engine.select_column(Select([zipcodes.zipcode]))["zipcode"]
google.batch_geocode(zipcode_list)
