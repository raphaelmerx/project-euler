import math
import time

begin = time.time()

def getDivisors(n):
    div= set([])
    div.add(1)
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            div.add(i)
            div.add(n/i)
    return div
def isAbundant(n):
    div=getDivisors(n)
    if sum(div)>n:
        return True
    else:
        return False
    
# list of whether numbers are abundant or not
def listAbundants(n):
    l={}
    l[0]=False
    for i in range(1,n):
        if isAbundant(i)==True:
            l[i]=True
        else:
            l[i]=False
    return l
def isNOTSumTwoAbundants(n, Abundant):
    for i in range(1,n):
        j=n-i
        if Abundant[i] and Abundant[j]:
            return False
    return True
def calculateSum():
    sum=0
    Abundant = listAbundants(28125)
    for n in range(1,28124):
        if isNOTSumTwoAbundants(n,Abundant)==True:
            sum+=n
    return sum

t=calculateSum()
print t

def getAbundants(n):
    l=[]
    for i in range(1,n):
        if isAbundant(i):
            l.append(i)
    return l
def sumsInList(l):
    s=[]
    for x in l:
        for y in range(1,x+1):
            if x+y not in s:
                s.append(x+y)

end = time.time()
print end-begin

        
