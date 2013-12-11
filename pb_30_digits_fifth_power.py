'''
total=0
for a in range(0,10):
    A = a**5
    for b in range(0,10):
        B = b**5
        for c in range(0,10):
            C=c**5
            for d in range(0,10):
                D=d**5
                for e in range(0,10):
                    E=e**5
                    for f in range(0,10):
                        F=f**5
                        sum = A+B+C+D+E+F
                        digits = int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f))
                        if sum==digits and sum!=0 and sum!=1:
                            total+=sum
print total

'''

def prob30(x):
    s = 0
        for i in range(2,1000000):
                t = 0
                for a in str(i):
                        t += int(a)**x
                if t == i:
                        s += t
        print s
prob30(5)
                    


                    
                
