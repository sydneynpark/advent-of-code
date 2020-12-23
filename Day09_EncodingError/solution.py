

def read_xmas_transmission(filepath):
    with open(filepath, 'r') as transmission:
        transmission_values = transmission.read().splitlines()
        transmission_numbers = [
            int(val)
            for val
            in transmission_values
        ]
        return transmission_numbers


def is_valid_value(value, preamble):

    sorted_preamble = preamble.copy()
    sorted_preamble.sort()

    smallest_index = 0
    largest_index = len(sorted_preamble) - 1

    while smallest_index < largest_index:

        sum = sorted_preamble[smallest_index] + sorted_preamble[largest_index]

        # Nice! We found two values that add up to the target value
        if sum == value:
            return True

        # Too small. Need to use a larger small-value
        elif sum < value:
            smallest_index += 1

        # Too large. Need to use a smaller large-value
        elif sum > value:
            largest_index -= 1

        # How did you get here?
        else:
            pass

    return False


def find_first_invalid_index(transmission, preamble_length):
    current_index = preamble_length

    while is_valid_value(transmission[current_index], transmission[current_index-preamble_length:current_index]):
        current_index += 1

    return current_index


def find_all_invalid_indexes(transmission, preamble_length):
    current_index = preamble_length
    invalid_indexes = []

    while current_index < len(transmission):
        print("Checking index {}: value {}".format(current_index, transmission[current_index]))
        if not is_valid_value(transmission[current_index], transmission[current_index-preamble_length:current_index]):
            invalid_indexes.append(current_index)
            print(" -> Invalid")
        else:
            print(" -> Valid")
        current_index += 1

    return invalid_indexes


def find_contiguous_values(values):

    first_contiguous_index = None
    last_contiguous_index = None

    for i in range(len(values) - 1):

        # Haven't found any contiguous yet. Look for one.
        if first_contiguous_index is None:
            if values[i] + 1 == values[i+1]:
                first_contiguous_index = i
                last_contiguous_index = i+1

        # We have already found a contiguous. Stretch the range as long as you keep finding contiguous vals.
        else:
            if values[i] + 1 == values[i+1]:
                last_contiguous_index = i+1

    return values[first_contiguous_index], values[last_contiguous_index]


def find_contiguous_summers(target_sum, summers):
    bottom_index = 0
    top_index = 1

    while top_index < len(summers):

        contiguous_summers = summers[bottom_index:top_index+1]
        contiguous_sum = sum(contiguous_summers)

        # We found contiguous items that sum to the target value
        if contiguous_sum == target_sum:
            return contiguous_summers

        # Too small. We need to pull another value into our sliding window.
        elif contiguous_sum < target_sum:
            top_index += 1

        # Too large. We need to throw out the lowest value from our sliding window.
        elif contiguous_sum > target_sum:
            bottom_index += 1

        # How did you get here?
        else:
            pass

    return None


def part_1(transmission, preamble_length):

    invalid_index = find_first_invalid_index(transmission, preamble_length)
    print("The first invalid value is {} at index={}".format(transmission[invalid_index], invalid_index))
    return transmission[invalid_index]


def part_2(transmission, invalid_value):

    items_that_sum = find_contiguous_summers(invalid_value, transmission)
    items_that_sum_str = [str(item) for item in items_that_sum]
    adding_string = ' + '.join(items_that_sum_str)

    print("{} = {} = {}".format(adding_string, invalid_value, sum(items_that_sum)))

    summers_min = min(items_that_sum)
    summers_max = max(items_that_sum)

    print("{} (min) + {} (max) = {}".format(summers_min, summers_max, summers_min + summers_max))
    print("The soln was {}".format(summers_min + summers_max))


if __name__ == '__main__':

    preamble_size = 25
    xmas_transmission = read_xmas_transmission('xmas_transmission.txt')

    part_2_arg = part_1(xmas_transmission, preamble_size)
    part_2(xmas_transmission, part_2_arg)

