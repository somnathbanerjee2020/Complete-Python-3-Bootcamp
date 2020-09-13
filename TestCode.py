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