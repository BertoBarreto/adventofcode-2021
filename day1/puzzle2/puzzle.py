with open("input.txt", "r") as fh:
    contents = fh.read()

mesurements = contents.split('\n')
counter = 0
lastSum = 0

for i in range(1, len(mesurements)):
    if i+1 < len(mesurements) and i+2 < len(mesurements):
        currSum = int(mesurements[i]) + int(mesurements[i+1]) + int(mesurements[i+2])
        if currSum > lastSum:
            counter += 1
        lastSum = currSum

print(counter)
