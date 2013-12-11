import math

'''
# l list of a_i, i=0..9
l=[]
rest = 999999
for i in range(0,10):
    l.append(rest//math.factorial(9-i) - 1)
    rest = rest - l[i]* math.factorial(9-i)
print l
'''
    

n=1
for a_0 in range(0,10):
    l_1 = range(0,10)
    l_1.remove(a_0)
    for a_1 in l_1:
        l_2 = l_1[:]
        l_2.remove(a_1)
        for a_2 in l_2:
            l_3 = l_2[:]
            l_3.remove(a_2)
            for a_3 in l_3:
                l_4 = l_3[:]
                l_4.remove(a_3)
                for a_4 in l_4:
                    l_5 = l_4[:]
                    l_5.remove(a_4)
                    for a_5 in l_5:
                        l_6 = l_5[:]
                        l_6.remove(a_5)
                        for a_6 in l_6:
                            l_7 = l_6[:]
                            l_7.remove(a_6)
                            for a_7 in l_7:
                                l_8 = l_7[:]
                                l_8.remove(a_7)
                                for a_8 in l_8:
                                    l_9 = l_8[:]
                                    l_9.remove(a_8)
                                    for a_9 in l_9:
                                        if n==1000000:
                                            print a_0,a_1,a_2,a_3,a_4,a_5,a_6,a_7,a_8,a_9
                                            n=n+1
                                            break
                                        else:
                                            n=n+1



