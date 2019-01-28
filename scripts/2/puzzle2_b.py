#puzzle wants to read lines of code and fine two ids that are only one character different and return the same character
#I think using the Levenshtein Distance is the best way to go about doing this
#I want to build the code from scatch - here's a link to reference https://www.python-course.eu/levenshtein_distance.php

from collections import Counter

with open("C:/Users/bhoff01/Desktop/python_scripts/Advent_of_Code/materials/2/box_ids.txt",'r') as file_object:
	contents = file_object.readlines()

#for loop to clean data and combine count of letters into string
l = []
for line in contents:
	s = ''
	line = line.rstrip('\n')
	counts = Counter(line)
	for keys, values in counts.items():
		s += str(values)
	l.append(s)



		
