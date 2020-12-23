import re




def read_rules_file(filepath):

    with open(filepath, 'r') as rules_file:
        rules_file_contents = rules_file.read()
        rules_descriptions = rules_file_contents.split('\n')

    rule_regex = '(.*) bags contain (.*)' # 1 dim beige bag, 4 muted cyan bags, 1 clear lavender bag.
    rule_pattern = re.compile(rule_regex)

    inner_bags_regex = '(\\d*) (\\w* \\w*) bags?'
    inner_bag_pattern = re.compile(inner_bags_regex)

    rules = {}
    rules_reversed = {}

    for rule_description in rules_descriptions:
        match = rule_pattern.match(rule_description)

        if (match):

            outer_bag_color = match.group(1)
            inner_bags = match.group(2)

            inner_rule = []

            for inner_bag_match in inner_bag_pattern.finditer(inner_bags):
                inner_bag_count = inner_bag_match.group(1)
                inner_bag_color = inner_bag_match.group(2)

                inner_rule.append( (int(inner_bag_count), inner_bag_color) )

                if inner_bag_color not in rules_reversed:
                    rules_reversed[inner_bag_color] = []
                rules_reversed[inner_bag_color].append(outer_bag_color)

            rules[outer_bag_color] = inner_rule

    return rules, rules_reversed


def print_rules(rules_dict):
    for key, value in rules_dict.items():
        print("{} -> {}".format(key, value))


def find_outer_bag_color(inner_colors_list, inner_to_outer_rules, found_so_far):

    for inner_color in inner_colors_list:
        if inner_color in inner_to_outer_rules:
            possible_outer_colors = inner_to_outer_rules[inner_color]
            found_so_far.update(set(possible_outer_colors))

            find_outer_bag_color(possible_outer_colors, inner_to_outer_rules, found_so_far)


def find_bag_count(outer_bag, outer_to_inner_rules):

    inner_bag_count = 1  # I'm a bag

    if outer_bag in outer_to_inner_rules:
        bags_i_can_hold = outer_to_inner_rules[outer_bag]

        for count, color in bags_i_can_hold:
            inner_bag_count += count * find_bag_count(color, outer_to_inner_rules)

    return inner_bag_count



if __name__ == '__main__':
    outer_to_inner, inner_to_outer = read_rules_file('tsa_rules.txt')
    # print_rules(outer_to_inner)
    # print_rules(inner_to_outer)

    holders = set()
    find_outer_bag_color(['shiny gold'], inner_to_outer, holders)

    bags_in_gold = find_bag_count('shiny gold', outer_to_inner) - 1
    print(bags_in_gold)