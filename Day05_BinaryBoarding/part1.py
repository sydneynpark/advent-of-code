NUM_ROWS = 128
NUM_COLS = 8


ROWS_UPPER = 'B'
ROWS_LOWER = 'F'

COLS_UPPER = 'R'
COLS_LOWER = 'L'


def seat_id(row, col):
    return (row * NUM_COLS) + col


def use_top_half(bottom, top):
    diff = top - bottom
    new_bottom = bottom + (diff // 2)
    return new_bottom, top


def use_bottom_half(bottom, top):
    diff = top - bottom
    new_top = top - (diff // 2)
    return bottom, new_top


def find_seat(boarding_pass):
    row_bottom = 0
    row_top = NUM_ROWS
    col_bottom = 0
    col_top = NUM_COLS

    for partition in boarding_pass:
        if partition == ROWS_UPPER:
            row_bottom, row_top = use_top_half(row_bottom, row_top)
        elif partition == ROWS_LOWER:
            row_bottom, row_top = use_bottom_half(row_bottom, row_top)
        elif partition == COLS_UPPER:
            col_bottom, col_top = use_top_half(col_bottom, col_top)
        elif partition == COLS_LOWER:
            col_bottom, col_top = use_bottom_half(col_bottom, col_top)
        else:
            print("What the hey?")

    return seat_id(row_bottom, col_bottom)


if __name__ == '__main__':
    with open('./resources/boarding_passes.txt', 'r') as f:
        boarding_passes = f.read().splitlines()
        seats = [find_seat(boarding_pass) for boarding_pass in boarding_passes]
        highest_seat = max(seats)
        print("The highest seat is {}".format(highest_seat))

    seats.sort()
    for i in range(len(seats)):
        if i+1 < len(seats) and seats[i+1] != seats[i]+1:
            print("".format(seats[i], seats[i+1]))
            print("{} -> ({}) -> {}".format(seats[i], seats[i] + 1, seats[i+1]))