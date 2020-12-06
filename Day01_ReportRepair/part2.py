import helpers



def find_items_that_add_to_target(target_sum, how_many_items, num_list_asc, bottom_index = 0):

    # Base case: target sum is negative or zero
    if target_sum <= 0:
        return None

    # Base case: we need one value so it needs to be an exact match
    if how_many_items == 1:
        if target_sum in num_list_asc[bottom_index:]:
            return [target_sum]
        else:
            return None

    bottom_value = num_list_asc[bottom_index]
    other_values = find_items_that_add_to_target(target_sum - bottom_value, how_many_items - 1, num_list_asc, bottom_index + 1)

    # Recursive case: we need multiple values to add up to target_sum
    # Grab the bottommost value we are allowed to search,
    # and find the other values that match
    while other_values is None and bottom_index + how_many_items < len(num_list_asc):
        bottom_index += 1
        bottom_value = num_list_asc[bottom_index]
        other_values = find_items_that_add_to_target(target_sum - bottom_value, how_many_items - 1, num_list_asc, bottom_index + 1)

    if other_values is None:
        return None
    else:
        return [bottom_value] + other_values



def run_search(target_sum, number_of_items, unsorted_list):
    unsorted_list.sort()
    answer = find_items_that_add_to_target(target_sum, number_of_items, unsorted_list)
    print(helpers.string_as_sum(answer))
    print(helpers.string_as_product(answer))


if __name__ == '__main__':
    expenses_from_file = helpers.read_expenses('./resources/expense_report.txt')
    run_search(2020, 3, expenses_from_file)

