
def organize_my_adapters(filepath):
    with open(filepath, 'r') as f:
        contents = f.read().splitlines()
        joltages = [ int(joltage) for joltage in contents]
        joltages.sort()
        return joltages




MAX_JOLTAGE_DIFF = 3

def part_1(joltage_adapters):

    print('--- PART 1 ---')


    current_joltage = 0
    diffs = [0] * (MAX_JOLTAGE_DIFF + 1)

    for i in range(len(joltage_adapters)):
        joltage_diff = joltage_adapters[i] - current_joltage
        if joltage_diff > 3:
            print("Too big of a joltage diff")
        diffs[joltage_diff] += 1
        current_joltage = joltage_adapters[i]

    diffs[3] += 1
    for i in range(len(diffs)):
        print("There were {} {}-jolt jumps.".format(diffs[i], i))

    one_three_jolt_product = diffs[1] * diffs[3]
    print("Answer: {}".format(one_three_jolt_product))


def find_all_possible_arrangements(joltage_adapters_desc, arrangement_count_by_joltage, target_joltage_index = None):
    if target_joltage_index is None:
        target_joltage_index = 0


    target_joltage = joltage_adapters_desc[target_joltage_index]

    # if already solved, use the solution we found
    if target_joltage in arrangement_count_by_joltage:
        return arrangement_count_by_joltage[target_joltage]
    # Base case: We've reached the outlet.
    if target_joltage == 0:
        return 1

    possible_arrangements = 0  # I'm an arrangement
    next_adapter_index = target_joltage_index + 1

    # Find arrangements for any adapters that could possibly connect to this one
    while next_adapter_index < len(joltage_adapters_desc) and joltage_adapters_desc[next_adapter_index] >= (target_joltage - MAX_JOLTAGE_DIFF):
        possible_arrangements += find_all_possible_arrangements(joltage_adapters_desc, arrangement_count_by_joltage, next_adapter_index)
        next_adapter_index += 1

    print("{} jolts - {} combinations".format(target_joltage, possible_arrangements), flush=True)

    # Cache answer and return
    arrangement_count_by_joltage[target_joltage] = possible_arrangements
    return possible_arrangements










def part_2(joltage_adapters_asc):
    print('--- PART 2 ---')
    joltage_adapters_desc = joltage_adapters_asc
    joltage_adapters_desc.reverse()
    joltage_adapters_desc.append(0)
    known_arrangements = {}
    print(joltage_adapters_desc)

    answer = find_all_possible_arrangements(joltage_adapters_desc, known_arrangements)
    print(answer)





if __name__ == '__main__':
    adapters_ascending = organize_my_adapters('joltage_adapters.txt')
    # part_1(adapters_ascending)
    part_2(adapters_ascending)