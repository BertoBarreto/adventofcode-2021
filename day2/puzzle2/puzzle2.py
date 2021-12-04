position = {'horizontal': 0,
            'vertical': 0,
            'aim': 0}

def forward_horizontal(value):
    position['horizontal'] = position.get('horizontal', 0) + value
    position['vertical'] = position.get('vertical', 0) + (position.get('aim', 0) * value)


def up_vertical(value):
    position['aim'] = position.get('aim', 0) - value


def down_vertical(value):
    position['aim'] = position.get('aim', 0) + value


possibleMoves = {'forward': forward_horizontal,
                 'down': down_vertical,
                 'up': up_vertical}


def switch_moves(move, value):
    resp = possibleMoves.get(move, f'invalid movement: {move}')
    if type(resp) == str:
        print(resp)
        exit(1)
    else:
        resp(value)


with open("input.txt", "r") as fh:
    contents = fh.read()

moves = contents.split('\n')

for movement in moves:
    amount = int(movement.split(' ')[1])
    movement = movement.split(' ')[0]
    switch_moves(movement, amount)

response = position['horizontal'] * position['vertical']
print(response)
