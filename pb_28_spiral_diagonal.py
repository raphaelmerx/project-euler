sum=1
base=1
for n in range(3,1002,2):
    for i in range(0,4):
        base = base+ n-1
        sum = sum + base
print sum
