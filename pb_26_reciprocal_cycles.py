def cycleLength(d):
    # convert fraction to float
    decimal = 1.0/d
    s = str(decimal)
    s=s[2:]
    l=[]
    i=int(s[0])
    # until we bump into a digit that was found before
    while i not in l:
        l.append(i)       
        s=s[1:]
        if len(s)<1:
            return 1
        else:
            i=s[0]
    # i is the number that appears twice
    a=l.index(i)
    return len(l)-a

def largestNbForCycle(n):
    maxCycle=0
    d=0
    for i in range(1,n):
        length = cycleLength(i)
        if length>maxCycle:
            maxCycle = length
            d = i
    return d

print largestNbForCycle(1000)
