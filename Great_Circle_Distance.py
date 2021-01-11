#!/usr/bin/python3

import sys
import csv
import random
import math

DEGREES_IN_RADIAN = 57.29577
MEAN_EARTH_RADIUS_KM = 6371

filename = 'places.csv'

############################################### Generate Data ###############################################										

# Read in command line argument or from places.csv and initilize dataset 
if len(sys.argv) == 2:								# If command line input is given
	#TODO: Check that input is int
	# print('Randomly generating', sys.argv[1], 'data points')

	n = int(sys.argv[1])
	D = [] 											# Initialize Data into a list
	for i in range(n): 								# Add n number of random locations to list 
		loc = 'Random Loc ' + str(i)
		lat = round(random.uniform(-90, 90), 5)
		lon = round(random.uniform(-180, 180), 5)
		temp = (loc,lat,lon)
		D.append(temp)

	# print(*D, sep = "\n") 
	# print(D[1])



elif len(sys.argv) == 1:							# Using place.csv file for data
	# print ('Using places.csv')
	D = []
	with open(filename,'r') as data: 				# Add each row from places.csv to Dictionary 
	   csv_reader = csv.reader(data)
	   next(csv_reader)								# Skip first line of .csv file

	   for line in csv_reader: 
	            D.append(line)
	
	# print(*D, sep = "\n")

else:
	print ('Error: Incorrect input')
	sys.exit(0)

############################################### Calculate the air distance ###############################################
results = []
i = 0
average = 0

while i < len(D):	
	j = i + 1
	while j < len(D):
		loc1, lat1, lon1 = D[i]
		loc2, lat2, lon2 = D[j]

		# Convert degrees to radians
		lat1 = math.radians(float(lat1))
		lon1 = math.radians(float(lon1))
		lat2 = math.radians(float(lat2))
		lon2 = math.radians(float(lon2))

		# Haversine formula  
		# https://medium.com/python-in-plain-english/calculating-great-circle-distances-in-python-cf98f64c1ea0
		dlon = abs(lon2 - lon1)  
		dlat = abs(lat2 - lat1) 
		a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
		c = 2 * math.asin(math.sqrt(a))

		# convert from radians to km
		dist = round(c * MEAN_EARTH_RADIUS_KM, 5)

		# Store results
		average += dist
		temp = (loc1,loc2,dist)
		results.append(temp)

		#print(loc1,loc2,dist)
			
		j += 1

	i += 1	

############################################### Sort and Print results ###############################################
sorted_results = sorted(results, key=lambda tup: tup[2])

for row in sorted_results:
	print("{: <25} {: <25} {: <25}".format(*row))



print("Average distance:",average/len(sorted_results), "km. Closest pair:", sorted_results[0][0] , "–", sorted_results[0][1], sorted_results[0][2], "km.")