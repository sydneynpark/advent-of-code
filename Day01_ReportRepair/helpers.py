def read_expenses(filename):
    with open(filename, 'r') as expense_file:
        expenses = expense_file.read().splitlines()
        expenses_numbers = [int(expense) for expense in expenses]
    return expenses_numbers


def find_last_index_smaller(val_to_stop_before, num_list_asc):
    last_index_smaller = -1

    while num_list_asc[last_index_smaller + 1] > val_to_stop_before:
        last_index_smaller += 1

    return last_index_smaller



def string_as_sum(val_list):

    total = sum(val_list)
    eqn = ' + '.join(map(str, val_list))
    eqn = eqn + ' = ' + str(total)
    return eqn

def string_as_product(args):
    eqn = ' * '.join(str(val) for val in args)
    product = 1
    for val in args:
        product *= val
    eqn += ' = ' + str(product)
    return eqn