with open("input.txt", "r") as fh:
    contents = fh.readlines()

clean_contents = []
for content in contents:
    if content != '\n':
        clean_contents.append(content.strip().replace('  ',' '))


nums = clean_contents.pop(0)
nums = nums.split(',')
boards = [[clean_contents[i].split(' '), clean_contents[i+1].split(' '), clean_contents[i+2].split(' '),
           clean_contents[i+3].split(' '), clean_contents[i+4].split(' ')] for i in range(0, len(clean_contents), 5)]
playing_board = [[[False for y in range(0,5)] for x in range(0,5)] for i in range(0, len(clean_contents), 5)]


def check_boards_horizontal():
    check = {'column': []}
    for i in range(0, len(playing_board)):
        for j in range(0, len(playing_board[i])):
            if False not in playing_board[i][j]:
                check['column'] = [int(val) for val in boards[i][j]]
                return check
    return -1


def check_boards_vertical():
    won = True
    check = {'column': []}
    for i in range(0, len(playing_board)):
        for v in range(0, 5):
            for j in range(0, 5):
                check['column'].append(int(boards[i][j][v]))
                if not playing_board[i][j][v]:
                    won = False
            if won:
                return check
            check = {'column': []}
            won = True
    return -1


def get_sum_unmarked(board_index):
    result = []
    for i in range(0, len(boards[board_index])):
        for j in range(0, len(boards[board_index][i])):
            if not playing_board[board_index][i][j]:
                result.append(int(boards[board_index][i][j]))
    return sum(result)


def play_game():
    for num in nums:
        for i in range(0, len(boards)):
            for j in range(0, len(boards[i])):
                if num in boards[i][j]:
                    index = boards[i][j].index(num)
                    playing_board[i][j][index] = True
                    horizontal = check_boards_horizontal()
                    vertical = check_boards_vertical()
                    if type(horizontal) == dict:
                        horizontal['number'] = int(num)
                        horizontal['board'] = int(i)
                        return horizontal
                    elif type(vertical) == dict :
                        vertical['number'] = int(num)
                        vertical['board'] = int(i)
                        return vertical


winner = play_game()
print(winner)
print(get_sum_unmarked(winner['board'])*winner['number'])












