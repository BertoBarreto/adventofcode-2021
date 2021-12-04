def max_count(line):
    return '1' if max(line.count('1'), line.count('0')) == line.count('1') else '0'


def min_count(line):
    return '1' if min(line.count('1'), line.count('0')) == line.count('1') else '0'


with open("input.txt", "r") as fh:
    contents = fh.read()

bits = contents.split('\n')
bits_matrix = [[bits[j][i] for j in range(0, len(bits))] for i in range(0, len(bits[0]))]

gamma_rate = ''
epsilon_rate = ''
for v_line in bits_matrix:
    gamma_rate += max_count(v_line)
    epsilon_rate += min_count(v_line)

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
power_consumption = gamma_rate * epsilon_rate
print(power_consumption)
