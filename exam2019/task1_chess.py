rook_str = 'b5'
bishop_str = 'g3'

all_available_posses = set()
for i in range(1, 9):
    for j in range(1, 9):
        tuple_to_add = (i, j)
        all_available_posses.add(tuple_to_add)

def convert(str_pos):
    str_pos_lst = list(str_pos)
    if str_pos_lst[0] == 'a':
        str_pos_lst[0] = 1
    elif str_pos_lst[0] == 'b':
        str_pos_lst[0] = 2
    elif str_pos_lst[0] == 'c':
        str_pos_lst[0] = 3
    elif str_pos_lst[0] == 'd':
        str_pos_lst[0] = 4
    elif str_pos_lst[0] == 'e':
        str_pos_lst[0] = 5
    elif str_pos_lst[0] == 'f':
        str_pos_lst[0] = 6
    elif str_pos_lst[0] == 'g':
        str_pos_lst[0] = 7
    elif str_pos_lst[0] == 'h':
        str_pos_lst[0] = 8

    str_pos_lst[1] = int(str_pos_lst[1])

    return tuple(str_pos_lst)

def convert_back(numnum):
    numnum = list(numnum)
    if numnum[0] == 1:
        numnum[0] = 'a'
    elif numnum[0] == 2:
        numnum[0] = 'b'
    elif numnum[0] == 3:
        numnum[0] = 'c'
    elif numnum[0] == 4:
        numnum[0] = 'd'
    elif numnum[0] == 5:
        numnum[0] = 'e'
    elif numnum[0] == 6:
        numnum[0] = 'f'
    elif numnum[0] == 7:
        numnum[0] = 'g'
    elif numnum[0] == 8:
        numnum[0] = 'h'

    numnum[1] = str(numnum[1])

    return ''.join(numnum)

# rook_num = convert(rook_str)
# bishop_num = convert(bishop_str)


def vertical_horizontal(position: tuple) -> set:
    """
    Return set with unavailable cells for rook
    """
    occupied = set()
    for pos in range(1, 9):
        figure_pos1 = (pos, position[1])
        figure_pos2 = (position[0], pos)

        occupied.add(figure_pos1)
        occupied.add(figure_pos2)


    return occupied


def for_bishop(position: tuple):
    position1 = position[0]
    position2 = position[1]
    moves = ((-1, -1), (1, -1), (-1, 1), (1, 1))
    unavailb = []
    for i in moves:
        position1_1 = position1
        position2_2 = position2
        while (0 < position1_1 <= 8 and 0 < position2_2 <= 8):
            to_add = (position1_1, position2_2)
            unavailb.append(to_add)
            position1_1 = position1_1 + i[0]
            position2_2 = position2_2 +i[1]

    return set(unavailb)

def available_for_chess(available_posses, unavailable_posses):
    result = available_posses.intersection(unavailable_posses)
    return result


def chess_puzzle(pos_1, pos_2):
    num_pos_1 = convert(pos_1)
    num_pos_2 = convert(pos_2)

    unavailables = []

    unavailables.extend(vertical_horizontal(num_pos_1))
    unavailables.extend(vertical_horizontal(num_pos_2))
    unavailables.extend(for_bishop(num_pos_2))

    unavail = set(unavailables)

    res = list(available_for_chess(all_available_posses, unavail))

    res = set(map(convert_back, res))

    return res


print(chess_puzzle('b5', 'g3'))

print()

