"""
def myfunc(incoming):
    l1=list(incoming)
    newStr=''
    for i in range(0, len(incoming)):
        if i % 2 == 0:
            pass
        else:
            l1[i] = l1[i].upper()
        
        newStr=newStr + l1[i]
    return newStr
    
    

k=myfunc('skyline')
print(k)

"""
import math
import  collections

"""
def do_sqr(x):
    return x**2

myList = [1,2,3,4,5,6,7,8,9]

#print(list(map(do_sqr, myList)))

print(list(map(lambda j: j**2, myList)))

print(list(filter(lambda x: x%2 == 0,myList)))
"""
"""

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'

lowCt=0
upCt=0

ct = collections.Counter(list(s))
print(ct)

for j in ct:
    if 97 <= ord(j) <= 122:
        lowCt += ct[j]
    elif 65 <= ord(j) <= 90:
        upCt += ct[j]

print(f'Uppercase count = {upCt}')
print(f'Lowercase count = {lowCt}')
"""


class Cone():
    pi = math.pi
    
    def __init__ (self, radius = 10)