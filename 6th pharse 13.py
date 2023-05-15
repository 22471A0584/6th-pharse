sen = input("").split(" ")
alp, digit = 0, 0

for item in sen:
    lst = [char for char in item]
    for j in lst:
        if 64 < ord(j) < 123:
            alp += 1
        if j.isdigit():
            digit += 1
print(f"LETTERS : {alp} \n DIGITS : {digit}")

