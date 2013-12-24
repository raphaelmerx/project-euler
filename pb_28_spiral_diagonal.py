sum=1
base=1
# n is the current wigth of the spiral
for n in range(3,1002,2):
    for i in range(0,4):
    	# base is the number in the corner
        base = base+ n-1
        sum = sum + base
print sum
