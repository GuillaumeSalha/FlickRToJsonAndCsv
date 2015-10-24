
#Things we can do with flickr API
# Shanghai place woeid 2151849 http://www.flickr.com/places/info/2151849
# getinfo + top100 tags
# get children
# for all children get info + top100 tags + list all photos + title for each with semantic analysis
#
# 1 - get shanghai/paris bounding box
# 2 - flickr.places.placesForBoundingBox
# 3 - flickr.places.tagsForPlace for today (repeat everyday) for 2012 for each place
#	min_taken_date mysql datetime
#	max_taken_date mysql datetime
# 3 - top 100 tags for this day with date taken (2 month shift)
import os, sys; sys.path.insert(0, os.path.join("..", ".."))
import json
from datetime import datetime, date, timedelta
import time as t
import requests


path='C:/Users/Salha/Desktop/flickR/2011bis/'

# prepare for the ice age
d1 = date(2011, 1, 1)
oneDay = timedelta(days=1)
d2 = d1 + oneDay

# get 10 month worth of data
for i in range(1, 365):
	d2 = d1 + oneDay

	params = {'method': 'flickr.photos.search', 'format' : 'json', 'woe_id' : 2151849, 'api_key':'ENTER API KEY HERE', 'min_taken_date':str(d1), 'max_taken_date':str(d2), 'has_geo':1, 'extras':'geo,tags'}
	data = requests.get('https://api.flickr.com/services/rest/', params=params)

	dataFile = open(path + str(d1) + "-photos.json","w+")
	dataFile.write(data.text)
	dataFile.close()

	dataJSONified = json.loads(data.text.lstrip("jsonFlickrApi(").rstrip(')'))
	pages = dataJSONified["photos"]["pages"]

	for page in range(2,pages+1,1):
		params = {'method': 'flickr.photos.search', 'format' : 'json', 'woe_id' : 2151849, 'api_key':'ENTER API KEY HERE', 'min_taken_date':str(d1), 'max_taken_date':str(d2), 'has_geo':1, 'extras':'geo,tags', 'page':page}
		data = requests.get('https://api.flickr.com/services/rest/', params=params)

		dataFile = open(path + str(d1) + "-" + str(page) + "-photos.json","w+")
		dataFile.write(data)
		dataFile.close()


	print "\t" + str(d1) + " done"

	d1 = d1 + oneDay
	t.sleep(1)
	
