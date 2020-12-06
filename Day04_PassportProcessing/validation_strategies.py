from abc import ABC
import re


class ValidationStrategy(ABC):

    def validate(self, value: str) -> bool:
        pass

    @staticmethod
    def reject_value_none(validation_func):
        def validate_if_not_none(validator, validation_arg):
            if validation_arg is not None:
                return validation_func(validator, validation_arg)
            else:
                return False
        return validate_if_not_none


class RequiredFieldValidationStrategy(ValidationStrategy):

    def validate(self, value):
        return value is not None


class OptionalFieldValidationStrategy(ValidationStrategy):

    def validate(self, value):
        return True


class FixedAnswerValidationStrategy(ValidationStrategy):

    def __init__(self, fixed_answer_list: list[str]):
        self.allowed_values = fixed_answer_list

    @ValidationStrategy.reject_value_none
    def validate(self, value):
        return value in self.allowed_values


class RegexValidationStrategy(ValidationStrategy):
    def __init__(self, regex: str):
        self.regex = regex

    @ValidationStrategy.reject_value_none
    def validate(self, value):
        return bool(re.match(self.regex, value, re.ASCII))


class IntegerRangeFieldValidationStrategy(ValidationStrategy):

    def __init__(self, min_acceptable_val: int, max_acceptable_val: int):
        self.min = min_acceptable_val
        self.max = max_acceptable_val

    @ValidationStrategy.reject_value_none
    def validate(self, value) -> bool:
        int_value = int(value)
        return self.min <= int_value <= self.max


class MeasurementRangeValidationStrategy(ValidationStrategy):

    def __init__(self, min_acceptable_val: int, max_acceptable_val: int, unit_of_measure: str):
        self.range_validator = IntegerRangeFieldValidationStrategy(min_acceptable_val, max_acceptable_val)
        self.unit_of_measure = unit_of_measure

    @ValidationStrategy.reject_value_none
    def validate(self, value):
        found_measurement = re.match("(\\d*){}".format(self.unit_of_measure), value, re.ASCII)
        if found_measurement:
            found_num = found_measurement.group(1)
            return self.range_validator.validate(found_num)


class MultipleValidationStrategies(ValidationStrategy):

    def __init__(self, validation_strategies: list[ValidationStrategy], all_are_required=False):
        self.validations = validation_strategies
        self.require_all = all_are_required

    def _any_are_valid(self, value) -> bool:
        for validation in self.validations:
            if validation.validate(value):
                return True
        return False

    def _all_are_valid(self, value) -> bool:
        for validation in self.validations:
            if not validation.validate(value):
                return False
        return True

    def validate(self, value):
        if self.require_all:
            return self._all_are_valid(value)
        else:
            return self._any_are_valid(value)
