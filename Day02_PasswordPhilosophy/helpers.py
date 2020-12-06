import re
from abc import ABC


class PasswordPolicy(ABC):

    def validate(self, password):
        pass

    def __str__(self):
        pass

# end class PasswordPolicy


class LetterCountPolicy(PasswordPolicy):

    def __init__(self, min, max, letter):
        self.min = int(min)
        self.max = int(max)
        self.letter = letter

    def validate(self, password):
        letter_count = password.count(self.letter)
        return letter_count >= self.min and letter_count <= self.max

    def __str__(self):
        return "{}-{} {}".format(self.min, self.max, self.letter)

# end class LetterCountPolicy


class PositionPolicy(PasswordPolicy):

    def __init__(self, pos1, pos2, letter):
        self.pos1 = int(pos1) - 1
        self.pos2 = int(pos2) - 1
        self.letter = letter

    def validate(self, password):
        return bool(password[self.pos1] == self.letter) != bool(password[self.pos2] == self.letter)

    def __str__(self):
        return "{}-{} {}".format(self.pos1, self.pos2, self.letter)

# end class PositionPolicy

def parse_file(filename, policy):
    passwords_and_policies = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            match = re.match("^(\d+)-(\d+) (\w): (.*)$", line)
            min = match.group(1)
            max = match.group(2)
            letter = match.group(3)
            password = match.group(4)

            passwords_and_policies.append((password, policy(min, max, letter)))

    return passwords_and_policies
