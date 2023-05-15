lines = []
while True:
	loopInput = input()
	if loopInput == "done":
		break
	else:
		lines.append(loopInput)

lst = list(int(i[2:]) if i[0] == 'D' else -int(i[2:]) for i in lines)
print(sum(lst))
