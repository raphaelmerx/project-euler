f = open('pb_79_passcode_derivation.txt','r')
l=f.readlines()
for s in l:
    i=l.index(s)
    s=s[0:3]
    l[i]=int(s)

digitsAfter = {}
for i in range(0,10):
    digitsAfter[i]=set()
for n in l:
    s=str(n)
    first=int(s[0])
    second=int(s[1])
    third=int(s[2])
    digitsAfter[first].add(second)
    digitsAfter[second].add(third)
print digitsAfter

for d in range(0,10):
    for digitToDelete in digitsAfter[d]:
        for otherDigit in range(0,10):
            # look at other sets only
            if d in digitsAfter[otherDigit] and digitToDelete in digitsAfter[otherDigit] and otherDigit!=d:
                digitsAfter[otherDigit].remove(digitToDelete)
print digitsAfter
