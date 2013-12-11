import math

def getDigits(n):
    l=[]
    i=1
    while(math.pow(10,i-1) < n):
        a = n%math.pow(10,i)
        a=int(a/math.pow(10,i-1))
        l.append(a)
        i=i+1
    return l

def isPalindrome(n):
    l=getDigits(n)
    while (len(l)>1):
        if l.pop(0) == l.pop():
            continue
        else:
            return False
    return True

max=0
for x in range(100,1000):
    for y in range(100,1000):
        a = x*y
        if (a>max and isPalindrome(a)):
            max=a
            b=x
            c=y
print [max,b,c]
