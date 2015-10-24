#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys; sys.path.insert(0, os.path.join("..", ".."))
import json
import csv

path='C:/Users/Salha/Desktop/flickR/2015/'

dirlist = os.listdir(path)

csvFile = csv.writer(open('flickr-shanghai-2015.csv', 'w+'), delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
csvFile.writerow(['userid', 'title', 'lat', 'lon', 'day', 'tags'])

for name in dirlist:
	if name.endswith("photos.json"): 
		data = open(path + name,'r').read().lstrip('jsonFlickrApi(').rstrip(')')

		dataJsonify = json.loads(data)

		day = name[:10]
		print day

		for photo in dataJsonify['photos']['photo']:
			userid = photo['owner']
			title = photo['title'].encode('utf-8')
			lat = photo['latitude']
			lon = photo['longitude']
			tags = photo['tags'].encode('utf-8') 
			csvFile.writerow([userid, title, lat, lon, day, tags])