l = [-6, 3, 8, 5, -6]
deltas = [l[0] + l[1]]

deltas_set = set(deltas)


sequence = 2
while len(deltas) == len(deltas_set):
	if sequence > len(l)-1:
		sequence = 0
		deltas.append(deltas[-1] +l[sequence])
		deltas_set = set(deltas)
		sequence += 1
	if sequence <= len(l) - 1:
		deltas.append(deltas[-1] + l[sequence])
		deltas_set = set(deltas)
		sequence += 1
print(deltas)
print(deltas_set)
print(deltas[-1])
		
	
