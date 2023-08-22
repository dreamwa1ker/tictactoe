field = "         "
grid = [list(field[i:i + 3]) for i in range(0, len(field), 3)]

current_player = "X"

def print_field():
    print('---------')
    for row in grid:
        print('|', ' '.join(row), '|')
    print('---------')

def get_position_indexes(char):
    positions = ''
    for i in range(len(field)):
        if field[i] == char:
            positions = positions + str(i)
    return positions

def is_position_winning(char):
    winning_positions = ["012", "345", "678", "036", "147", "258", "048", "246"]
    current_positions = ''

    for i in range(len(field)):
        if field[i] == char:
            current_positions = current_positions + str(i)

    for i in winning_positions:
        if all(char in current_positions for char in i):
            return True
    return False

def check_empty_cells():
    for i in field:
        if " " in field:
            return True
        return False


print_field()

while True:
    y, x = input().split()

    while not (y.isdigit() and x.isdigit()):
        print("You should enter numbers!")
        y, x = input().split()

    while int(y) > 3 or int(x) > 3:
        print("Coordinates should be from 1 to 3!")
        y, x = input().split()

    while grid[int(y) - 1][int(x) - 1] != " ":
        print("This cell is occupied! Choose another one!")
        y, x = input().split()

    y, x = map(lambda num: int(num) - 1, (y, x))

    grid[y][x] = current_player
    field = ''.join([''.join(row) for row in grid])
    print_field()

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    if is_position_winning("O"):
        print("O wins")
        break
    elif is_position_winning("X"):
        print("X wins")
        break
    elif not check_empty_cells():
        print("Draw")
        break

