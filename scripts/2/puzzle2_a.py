#puzzle wants a check sum that counts the occurrence in a list of strings of letters. Only needs to record letters that appear 2 or 3 times


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

#objects to track for solution
twos = 0
threes = 0

#for loop to count if 2's or 3's exist in string
for string in l:
	if '2' in string:
		twos += 1
	if '3' in string:
		threes += 1
	else:
		continue

#display solution
print('twos: ' + str(twos))
print('threes: ' + str(threes))
print('checksum: ' + str(twos * threes))


		
