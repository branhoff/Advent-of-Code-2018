
#Day 1: Solution 1
with open("C:/Users/bhoff01/Desktop/python_scripts/Advent_of_Code/materials/1/puzzle1_values.txt",'r') as file_object:
	contents = file_object.read()

l = []
aggregate = 0

for item in contents:
	item = item.rstrip('\n')
	l.append(item)
	if item[0] == '+':
		aggregate += int(item[1:len(item)])
	else:
		aggregate -= int(item[1:len(item)])
print(aggregate)
