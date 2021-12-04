with open("input.txt", "r") as fh:
    contents = fh.read()

bits = contents.split('\n')


def max_count(line):
    if max(line.count('1'), line.count('0')) != 0:
        return '1' if max(line.count('1'), line.count('0')) == line.count('1') else '0'
    else:
        return '1'


def min_count(line):

    if min(line.count('1'), line.count('0')) != 0:
        return '0' if min(line.count('1'), line.count('0')) == line.count('0') else '1'
    else:
        return '0'


def invert(val):
    return '0' if val == '1' else '1'


def remove_unwanted(l, y, matrix):
    for i in range(0, l):
        matrix[i].pop(y)


def verify_line(i, num_max, matrix):
    for j in range(0, len(matrix[i])):
        if num_max == matrix[i][j]:
            remove_unwanted(len(matrix), j,matrix)
            return True

    return False


def get_oxygen_generator_rating():
    rating = ''
    oxygen_matrix = [[bits[j][i] for j in range(0, len(bits))] for i in range(0, len(bits[0]))]
    for i in range(0, len(oxygen_matrix)):
        num_max = invert(max_count(oxygen_matrix[i]))
        while verify_line(i, num_max,oxygen_matrix):
            pass
    for num in oxygen_matrix:
        rating += num[0]
    return rating


def get_co2_scrubber_rating():
    rating = ''
    co2_matrix = [[bits[j][i] for j in range(0, len(bits))] for i in range(0, len(bits[0]))]
    for i in range(0, len(co2_matrix)):
        if len(co2_matrix[0]) != 1:
            num_max = invert(min_count(co2_matrix[i]))
            while verify_line(i, num_max, co2_matrix):
                pass

    for num in co2_matrix:
        rating += num[0]
    return rating


oxygen_rating = int(get_oxygen_generator_rating(),2)
co2_rating = int(get_co2_scrubber_rating(),2)
print(oxygen_rating*co2_rating)
