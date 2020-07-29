import re


def validate_cpf_mask_input(raw_input: str) -> re.Match:
    """
    Validate raw input. If the input match with cpf mask, return re.Match object.
    If not, return None
    """
    pattern = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    return re.match(pattern, raw_input)


def validate_if_all_numbers_are_same_number(cpf_list_numbers: list) -> bool:
    """
    A validator function to validate if cpf numbers are same number
    """

    if len(set(cpf_list_numbers)) == 1:
        return False
    return True


def validate_first_cpf_check_digit(cpf_list_numbers: list) -> bool:
    """
    A validator function to validate if cpf first check digit is valid
    """
    cpf_9_first_digits = cpf_list_numbers[:-2]
    cpf_second_to_last_digit = int(cpf_list_numbers[-2])
    list_of_multipliers_for_first_validation = [x for x in range(2, 11)]
    list_of_multipliers_for_first_validation.reverse()

    sum_of_products_for_first_validation = 0
    for index in range(len(cpf_9_first_digits)):
        cpf_number = int(cpf_9_first_digits[index])
        multiplier = list_of_multipliers_for_first_validation[index]
        sum_of_products_for_first_validation += cpf_number * multiplier

    module_sum_first_validation_plus_10_divided_by_11 = (
        sum_of_products_for_first_validation * 10
    ) % 11

    if module_sum_first_validation_plus_10_divided_by_11 == 10:
        module_sum_first_validation_plus_10_divided_by_11 = 0

    if (
        module_sum_first_validation_plus_10_divided_by_11
        != cpf_second_to_last_digit
    ):
        return False
    return True


def validate_second_cpf_check_digit(cpf_list_numbers: list) -> bool:
    """
    A validator function to validate if cpf second check digit is valid
    """
    cpf_10_first_digits = cpf_list_numbers[:-1]
    cpf_last_digit = int(cpf_list_numbers[-1])
    list_of_multipliers_for_second_validation = [x for x in range(2, 12)]
    list_of_multipliers_for_second_validation.reverse()

    sum_of_products_for_second_validation = 0
    for index in range(len(cpf_10_first_digits)):
        cpf_number = int(cpf_10_first_digits[index])
        multiplier = list_of_multipliers_for_second_validation[index]
        sum_of_products_for_second_validation += cpf_number * multiplier

    module_sum_second_validation_plus_10_divided_by_11 = (
        sum_of_products_for_second_validation * 10
    ) % 11

    if module_sum_second_validation_plus_10_divided_by_11 == 10:
        module_sum_second_validation_plus_10_divided_by_11 = 0

    if module_sum_second_validation_plus_10_divided_by_11 != cpf_last_digit:
        return False
    return True


def validate_cpf(cpf: str) -> bool:
    """
    A validator function to validate cpf of each client
    """

    cpf_mask_validated = validate_cpf_mask_input(cpf)

    if cpf_mask_validated:
        cleaned_cpf = cpf.replace('.','').replace('-','')
        cpf_list_numbers = list(cleaned_cpf)

        # Validates first digit
        all_digits_equal_or_not_validation = validate_if_all_numbers_are_same_number(
            cpf_list_numbers
        )

        first_check_digit_validation = validate_first_cpf_check_digit(
            cpf_list_numbers
        )

        second_check_digit_validation = validate_second_cpf_check_digit(
            cpf_list_numbers
        )

        if (
            all_digits_equal_or_not_validation
            and first_check_digit_validation
            and second_check_digit_validation
        ):
            return True
        else:
            raise ValueError("O CPF inserido não é válido. Tente novamente.")

    else:
        return f"O valor inserido - {cpf} - não é um formato válido de CPF. Tente novamente com um valor válido."