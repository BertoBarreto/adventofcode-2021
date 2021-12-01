with open("puzzle_1_input.txt", "r") as fh:
    contents = fh.read()

mesurements = contents.split('\n')
counter = 0
for i in range(1, len(mesurements)):
    if int(mesurements[i]) > int(mesurements[i - 1]):
        counter += 1

print(counter)
