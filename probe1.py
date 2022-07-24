a = input().split()
s = []
x = ''
for i in a:    
    if x != i:    
        s.append(list(i))    
    else:
        s[-1].append(i)      
    x = i    
print(s)    
