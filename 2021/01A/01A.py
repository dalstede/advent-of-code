currrentPing = 0
previousPing = -1
increaseCount = 0  

file = open("input.txt","r") 

for line in file:
	currentPing = int(line)
	if currentPing > previousPing:
		increaseCount += 1
	previousPing = currentPing

increaseCount -= 1 # first one doesn't count as there is no previous value

print(increaseCount)