seq = input().split(',') 
lst = [int(i) for i in seq]
def flt(i):                                           
    return i % 2 != 0
result_l = [str(i * i) for i in filter(flt,lst)]      
print(",".join(result_l))
