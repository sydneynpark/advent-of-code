'''
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.

'''

from validation_strategies import ValidationStrategy, IntegerRangeFieldValidationStrategy, MeasurementRangeValidationStrategy, MultipleValidationStrategies, FixedAnswerValidationStrategy, RegexValidationStrategy, OptionalFieldValidationStrategy
from passport import Passport, PassportValidator

VALIDATION_RULES = {
    "byr": IntegerRangeFieldValidationStrategy(1920, 2002),
    "iyr": IntegerRangeFieldValidationStrategy(2010, 2020),
    "eyr": IntegerRangeFieldValidationStrategy(2020, 2030),
    "hgt": MultipleValidationStrategies([
        MeasurementRangeValidationStrategy(150, 193, 'cm'),
        MeasurementRangeValidationStrategy(59, 76, 'in')
        ]),
    "hcl": RegexValidationStrategy("\\#[0-9a-f]{6}$"),
    "ecl": FixedAnswerValidationStrategy(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
    "pid": RegexValidationStrategy("\\d{9}$"),
    "cid": OptionalFieldValidationStrategy()
}


if __name__ == '__main__':
    validator = PassportValidator(VALIDATION_RULES)
    passports = validator.parse_passport_file('./resources/scanned_passports.txt')


    count_valid = 0
    count_invalid = 0
    for passport in passports:
        if validator.validate(passport):  # ,True):
            count_valid += 1
        else:
            count_invalid += 1

    print("Of {} passports, {} checked out.".format(count_valid+count_invalid, count_valid))
    print("Of {} passports, {} were INVALID.".format(count_valid+count_invalid, count_invalid))
