lst = []
while True:
    s = input().split(',')
    if not s[0]:                          
        break
    lst.append(tuple(s))

lst.sort(key= lambda x:(x[0],int(x[1]),int(x[2])))  
print(lst)
