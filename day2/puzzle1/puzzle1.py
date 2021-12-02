def add_horizontal(value):
    position['horizontal'] = position.get('horizontal', 0) + value

def add_vertical(value):
    position['vertical'] = position.get('vertical', 0) + value

def rmv_vertical(value):
    position['vertical'] = position.get('vertical', 0) - value

possibleMoves = {
                'forward': add_horizontal,
                'down':add_vertical,
                'up':rmv_vertical,
                 }

def switch_moves(move, value):
    resp = possibleMoves.get(move, f'invalid argument: {move}')
    if type(resp) == str:
        print(resp)
        exit(1)
    else:
        resp(value)

position = {'horizontal': 0, 'vertical': 0}

with open("input.txt", "r") as fh:
    contents = fh.read()

moves = contents.split('\n')

for move in moves:
    value = int(move.split(' ')[1])
    move = move.split(' ')[0]
    switch_moves(move,value)

response = position['horizontal'] * position['vertical']
print(response)
