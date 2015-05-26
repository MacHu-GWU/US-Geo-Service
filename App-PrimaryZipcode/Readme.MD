#Zipcode Geometry Information Database

This project provides 29959 standard zipcode and it's lat, lng. In many location based service, we want to search xxx near a zipcode. This database enable you to do that. Plus, I write a fuzzy search engine enable developer to search zipcode by city and state. You can use 2-letter state short name or full name, and even the spelling doesn't has to be exactly right, the engine still able to return you all available results.

Source Data Download From: [http://federalgovernmentzipcodes.us/](http://federalgovernmentzipcodes.us/)

##Usage

Prerequisite

- [python3](https://www.python.org/)
- [angora](https://github.com/MacHu-GWU/Angora)
- [fuzzywuzzy](https://pypi.python.org/pypi/fuzzywuzzy)

The usage is very simple. Copy the util folder to your project directory. Extract data.zip to current directory. (StandardZipcode.sqlite is the database file)

	from util import lookup
	
	# search by zipcode
	for result in lookup.by_zipcode("20037")
		print(result)

	# search by city and state
	for result in lookup.by_zipcode("washington", "DC")
		print(result)

	# search by zipcode
	for result in lookup.by_zipcode("new york")
		print(result)