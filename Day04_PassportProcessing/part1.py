from passport import Passport, PassportValidator
from validation_strategies import ValidationStrategy, RequiredFieldValidationStrategy, OptionalFieldValidationStrategy

if __name__ == '__main__':
    required_fields = [
        'byr',  # (Birth Year)
        'iyr',  # (Issue Year)
        'eyr',  # (Expiration Year)
        'hgt',  # (Height)
        'hcl',  # (Hair Color)
        'ecl',  # (Eye Color)
        'pid',  # (Passport ID)
    ]
    optional_fields = [
        'cid',  # (Country ID)
    ]

    validations = {}
    for field in required_fields:
        validations[field] = RequiredFieldValidationStrategy()
    for field in optional_fields:
        validations[field] = OptionalFieldValidationStrategy()

    validator = PassportValidator(validations)
    passports = validator.parse_passport_file('./resources/scanned_passports.txt')

    ValidationStrategy.use_debug_mode(False)   # (True)

    valids = 0
    invalids = 0
    total = 0
    for passport in passports:
        total += 1
        if validator.validate(passport):
            valids += 1
        else:
            invalids += 1

    print("Found {} valid passports".format(valids))
    print("Found {} invalid passports".format(invalids))
