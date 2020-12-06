import helpers




def find_pair_to_make_desired_sum(index_to_search, desired_sum, num_list_asc):
    val1 = num_list_asc[index_to_search]

    while val1 + num_list_asc[index_to_search] < desired_sum:
        index_to_search += 1

    if val1 + num_list_asc[index_to_search] == desired_sum:
        return index_to_search
    else:
        return None


def find_sum_vals(desired_sum, expenses):
    expenses.sort()
    half_desired_sum = desired_sum / 2

    index_of_val1 = find_last_index_smaller(half_desired_sum, expenses)
    index_of_val2 = find_pair_to_make_desired_sum(index_of_val1, desired_sum, expenses)
    # todo figure out how to not repeat this line

    while index_of_val2 is None:
        index_of_val1 -= 1
        index_of_val2 = find_pair_to_make_desired_sum(index_of_val1, desired_sum, expenses)

    return expenses[index_of_val1], expenses[index_of_val2]


if __name__ == '__main__':
    expenses_from_file = helpers.read_expenses('./resources/expense_report.txt')
    val1, val2 = find_sum_vals(2020, expenses_from_file)
    print("{} * {} = {}".format(val1, val2, val1 * val2))
