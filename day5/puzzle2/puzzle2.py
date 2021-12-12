with open("input.txt", "r") as fh:
    contents = fh.read()

contents = contents.split('\n')
coordinates = []
biggest = 0

for coord in contents:
    splitted = coord.split(' -> ')
    val1 = [int(x) for x in splitted[0].split(',')]
    val2 = [int(x) for x in splitted[1].split(',')]
    points = []
    if val1[0] == val2[0]:
        if val1[1] > val2[1]:
            for c in range(val2[1], val1[1] + 1):
                coordinates.append([val1[0], c])
        else:
            for c in range(val1[1], val2[1] + 1):
                coordinates.append([val1[0], c])
    elif val2[1] == val1[1]:
        if val1[0] > val2[0]:
            for c in range(val2[0], val1[0] + 1):
                coordinates.append([c, val1[1]])
        else:
            for c in range(val1[0], val2[0] + 1):
                coordinates.append([c, val1[1]])
    elif val2[0] != val1[0] and val2[1] != val1[1]:
        numsx = []
        numsy = []
        if val1[0] > val2[0]:
            for c in range(val2[0], val1[0]+1):
                numsx.append(c)
        elif val1[0] < val2[0]:
            for c in range(val1[0], val2[0]+1):
                numsx.append(c)
            numsx.reverse()
        if val1[1] > val2[1]:
            for c in range(val2[1], val1[1]+1):
                numsy.append(c)
        elif val1[1] < val2[1]:
            for c in range(val1[1], val2[1]+1):
                numsy.append(c)
            numsy.reverse()

        for i in range(0, len(numsx)):
            coordinates.append([numsx[i], numsy[i]])
    print(f'{val1} | {val2} => {points}')

    if int(val1[0]) > biggest:
        biggest = int(val1[0])
    elif int(val2[0]) > biggest:
        biggest = int(val2[0])
    elif int(val1[1]) > biggest:
        biggest = int(val1[1])
    elif int(val2[1]) > biggest:
        biggest = int(val2[1])

diagram = [['.' for x in range(0, biggest + 1)] for i in range(0, biggest + 1)]


def print_diagram():
    for line in diagram:
        for dot in line:
            print(dot, end='')
        print()


def place_point(x, y):
    pos = diagram[y][x]
    if pos == '.':
        diagram[y][x] = 1
    else:
        diagram[y][x] += 1


for coord in coordinates:
    place_point(coord[0], coord[1])


def total_points():
    points = 0
    for line in diagram:
        for num in line:
            if num != '.' and num >= 2:
                points += 1
    print(points)



total_points()