def isPrime(n):
    if n==0 or n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
    return True

cornerNumber=1
numberOfPrimes = 0
# 1, not counted in the while loop
numberOfNonPrimes = 1
ratio = 1.0
width = 1
# width is the current wigth of the spiral
while ratio>=0.1:
    width += 2
    for i in range(0,4):
        cornerNumber = cornerNumber + width-1
        if isPrime(cornerNumber) == True:
            numberOfPrimes += 1
        else:
            numberOfNonPrimes += 1
    ratio = float(numberOfPrimes)/(numberOfNonPrimes+numberOfPrimes)
print "width=", width