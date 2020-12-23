


class Source:

    def __init__(self, list_of_commands):
        self.commands = list_of_commands
        self.acc_value = 0
        self.current_line = 0

    def evaluate_line(self):
        command, arg = self.commands[self.current_line]

        if command == 'jmp':
            self.current_line += arg

        elif command == 'acc':
            self.acc_value += arg
            self.current_line += 1

        elif command == 'nop':
            self.current_line += 1

        return self.current_line, self.acc_value

    def clean_and_rebuild(self):
        self.acc_value = 0
        self.current_line = 0

    def evaluate_script(self):

        num_lines = len(self.commands)
        visited_lines = [False] * num_lines

        while 0 <= self.current_line < num_lines and not visited_lines[self.current_line]:
            visited_lines[self.current_line] = True
            self.evaluate_line()

        evaluated_to_completion = self.current_line == num_lines
        return self.acc_value, evaluated_to_completion


def compile_lol(filename):
    with open(filename, 'r') as source_file:
        source_code = source_file.read()
        source_lines = source_code.split('\n')

    def parse_command(line):
        command = line.split(' ')
        return command[0], int(command[1])

    commands = [
        parse_command(line_of_code)
        for line_of_code
        in source_lines
    ]

    return Source(commands)


def swap_jmps_and_nops(original_source: Source):

    original_lines = original_source.commands
    altered_versions = {}

    for line_num in range(len(original_lines)):
        command, arg = original_lines[line_num]

        # Change jmp to nop
        if command == 'jmp':
            new_version = original_lines.copy()
            new_version[line_num] = ('nop', arg)
            altered_versions[line_num] = Source(new_version)

        # Change nop to jmp
        elif command == 'nop':
            new_version = original_lines.copy()
            new_version[line_num] = ('jmp', arg)
            altered_versions[line_num] = (Source(new_version))

    return altered_versions


def problem_1(source_code):
    final_value, ran_to_completion = source_code.evaluate_script()
    print("Just before the infinite loop, acc={}".format(final_value))


def problem_2(source_code):
    all_possible_swaps = swap_jmps_and_nops(source_code)

    for changed_line, new_code in all_possible_swaps.items():

        final_value, ran_to_completion = new_code.evaluate_script()

        if ran_to_completion:
            print("Successfully booted with acc={}, by swapping line {}".format(final_value, changed_line))


if __name__ == '__main__':
    boot_code = compile_lol('boot_code.txt')

    problem_1(boot_code)
    problem_2(boot_code)
