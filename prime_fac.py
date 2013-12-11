import math
end = int(math.sqrt(600851475143))

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for n in range(2,end+1):
    if 600851475143%n==0:
        if isPrime(n):
            max=n
print max
        
