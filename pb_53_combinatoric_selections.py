import math
import time

beginning = time.time()

def combinatoricsGreater(value,rangeForN):
    res=0
    FactN=math.factorial(rangeForN[0])
    for n in rangeForN:
        r=n/2
        C_n_r = FactN/((math.factorial(r))*math.factorial(n-r))
        while C_n_r > value:
            if n%2==0 and r==n/2:
                res+=1
            else:
                res+=2
            C_n_r = C_n_r * r / (n-r+1)
            r=r-1
        FactN=FactN*(n+1)
    return res

print combinatoricsGreater(1000000,range(23,101))

end = time.time()
print end-beginning
