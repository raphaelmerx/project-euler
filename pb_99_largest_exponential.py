import math


f = open('pb_99_largest_exponential.txt', 'r')
maxi = 0
maxIndex = 0
lineIndex = 1
for line in f:
	line = line.split(',')
	base = int(line[0])
	exponent = int(line[1])
	toCompare = exponent*math.log(base)
	if toCompare > maxi:
		maxi = toCompare
		maxIndex = lineIndex
	lineIndex += 1
print "maxi, maxIndex = ", maxi, maxIndex
f.close()