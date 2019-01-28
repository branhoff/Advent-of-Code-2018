
#Day 1: Solution 2
file = open("C:/Users/bhoff01/Desktop/python_scripts/Advent of Code/materials/1",'r')


l =[]

for item in file:
	item = item.rstrip('\n')
	l.append(int(item))

deltas = [l[0] + l[1]]
deltas_set = set(deltas)
sequence = 2
while len(deltas) == len(deltas_set):
	if sequence > len(l)-1:
		sequence = 0
		deltas.append(deltas[-1] + l[sequence])
		deltas_set = set(deltas)
		sequence += 1
	if sequence <= len(l) - 1:
		deltas.append(deltas[-1] + l[sequence])
		deltas_set = set(deltas)
		sequence += 1
print(deltas[-1])



