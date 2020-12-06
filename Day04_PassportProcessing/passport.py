from validation_strategies import ValidationStrategy



class Passport:

    def __init__(self, info: dict[str, str]):
        self.passport_info: dict[str, str] = info

    def passport_fields(self) -> set[str]:
        return set(self.passport_info.keys())


class PassportValidator:

    def __init__(self, fields_and_validations: dict[str, ValidationStrategy]):
        self.validation_by_field: dict[str, ValidationStrategy] = fields_and_validations
        self.passports_checked = 0

    @staticmethod
    def parse_passport(passport_string: str) -> Passport:
        infos = passport_string.split()
        fields_vals_dict: dict[str, str] = {}
        for info in infos:
            split_field_and_value = info.split(':')
            field_name = split_field_and_value[0]
            field_value = split_field_and_value[1]
            fields_vals_dict[field_name] = field_value
        return Passport(fields_vals_dict)

    @staticmethod
    def parse_passport_file(filepath: str) -> list[Passport]:
        with open(filepath, 'r') as f:
            all_passports = f.read()
            passport_string_list = all_passports.split('\n\n')
            passport_list = [PassportValidator.parse_passport(passport_string) for passport_string in passport_string_list]
        return passport_list

    def validate(self, passport: Passport, print_debug_output: bool = False) -> bool:

        def debug(msg):
            if print_debug_output:
                print("[{}] {}".format(self.passports_checked, msg))

        self.passports_checked += 1
        is_valid = True
        debug("Starting passport...")

        for field, validator in self.validation_by_field.items():
            found_value = passport.passport_info.get(field, None)
            is_valid &= validator.validate(found_value)
            if not validator.validate(found_value):
                debug(" -> Failing value {} : {}".format(field, found_value))

        if is_valid:
            debug("*** Accepted")
        else:
            debug("XXX Rejected")
        return is_valid

