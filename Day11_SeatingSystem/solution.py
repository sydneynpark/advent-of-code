import copy


OCCUPIED_SEAT = '#'
EMPTY_SEAT = 'L'
FLOOR = '.'

TOO_MANY_NEIGHBORS = 4

DEBUG = False

def print_map(seating_chart):
    if DEBUG:
        for row in seating_chart:
            print(''.join(row))
        print()


def count_neighbors(seating_chart, coords):
    row_coord, col_coord = coords
    neighbors = 0

    total_rows = len(seating_chart)
    total_cols = len(seating_chart[0])

    row_vicinity_min, row_vicinity_max = (max(0, row_coord - 1), min(row_coord + 2, total_rows))
    col_vicinity_min, col_vicinity_max = (max(0, col_coord - 1), min(col_coord + 2, total_cols))



    # Clip ranges to not extend beyond the bounds of the map
    for neighboring_row in range(row_vicinity_min, row_vicinity_max):
        for neighboring_col in range(col_vicinity_min, col_vicinity_max):

            # Don't count your own seat
            if not (neighboring_row == row_coord and neighboring_col == col_coord):

                if seating_chart[neighboring_row][neighboring_col] == OCCUPIED_SEAT:
                    neighbors += 1

    return neighbors


def count_occupied(map):
    count = 0
    for row in map:
        for seat in row:
            if seat == OCCUPIED_SEAT:
                count += 1
    return count


def step(seating_chart):
    num_rows = len(seating_chart)
    num_cols = len(seating_chart[0])

    new_map = [ [' ' for _ in range(num_cols)] for _ in range(num_rows)]

    changed = False


    for row in range(0, num_rows):
        for col in range(0, num_cols):

            # If you're sitting and there's too many people around, get up
            if seating_chart[row][col] == OCCUPIED_SEAT and count_neighbors(seating_chart, (row, col)) >= TOO_MANY_NEIGHBORS:
                new_map[row][col] = EMPTY_SEAT
                changed = True

            # If you're standing but it's spacey, sit down
            elif seating_chart[row][col] == EMPTY_SEAT and count_neighbors(seating_chart, (row, col)) == 0:
                new_map[row][col] = OCCUPIED_SEAT
                changed = True

            # Otherwise, don't change (sitting and comfortable; standing and crowded; floor)
            else:
                new_map[row][col] = seating_chart[row][col]

    return new_map, changed


def run_simulation(starting_map):

    current_map = starting_map
    how_many_rounds = 0

    num_rows = len(starting_map)
    num_cols = len(starting_map[0])
    print("DIMENSIONS: {}x{}".format(num_rows, num_cols))

    changed = True
    while changed:
        print_map(current_map)

        current_map, changed = step(current_map)
        how_many_rounds += 1

    occupied_seats = count_occupied(current_map)
    return occupied_seats


def read_map(filepath):
    with open(filepath, 'r') as f:
        contents = f.read().splitlines()
        return [
            list(line)
            for line
            in contents
        ]



if __name__ == '__main__':
    initial_seating_chart = read_map('seating_system.txt')
    final_seat_count = run_simulation(initial_seating_chart)
    print(final_seat_count)
