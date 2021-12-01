with open("input.txt", "r") as fh:
    contents = fh.read()

mesurements = contents.split('\n')
counter = 0
cont2 = 0
ms = {}

for i in range(0, len(mesurements)):
    for y in range(i, i+3):
        if y < len(mesurements):
            ms[cont2] = int(mesurements[y]) + ms.get(cont2, 0)

    cont2 += 1

counter = 0

for i in range(1, len(ms.items())):
    if ms[i] > ms[i - 1]:
        counter += 1

print(counter)