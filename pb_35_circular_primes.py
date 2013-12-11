def rotations(n):
    res=[]
    s=str(n)
    for i in range(len(s)):
        digit=s[0]
        s=s[1:]
        s=s+digit
        res.append(int(s))
    return res

def isPrime(n):
    if n==0 or n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
    return True

def isCircularPrime(n):
    rot=rotations(n)
    for i in rot:
        if isPrime(i)==False:
            return False
    return True

def countCircularPrimes(l):
    n=0
    for i in range(1,len(l)+1):
        if l[i]==True:
            if rotationsInList(l,i):
                n=n+1
    return n

# everything is a reference in Python
def deleteNonPrimes(l):
    l[1]=False
    # l has to be so that l[i]=i or l[i]=0
    for i in range(2,len(l)):
        # if i is not the multiple of a previously seen number
        if l[i]==i and i>1:
            if isPrime(i)==False:
                l[i]=False
            else:
                l[i]=True
            # replace all multiples of i by 0
            k=2
            while i*k<=len(l):
                l[i*k]=False
                k=k+1
    return l

PrimeNb={}
for i in range(1,1000000):
    PrimeNb[i]=i
deleteNonPrimes(PrimeNb)

def rotationsInList(l,n):
    rot=rotations(n)
    for i in rot:
        if l[i]==False:
            return False
    return True

print countCircularPrimes(PrimeNb)
