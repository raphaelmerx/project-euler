def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

n=1
prime=2
while(n<2):
    maybePrime=prime+1
    while(isPrime(maybePrime)==False):
        maybePrime=maybePrime+1
    prime=maybePrime
    n=n+1
print prime
