from const import *


def check_number_starts_or_ends_with_decimal(curr_number: str):
    """
    the function receives a string that represent valid float number
    the function prints message if the number is starts or ends with decimal point so the user would know how the
    calculator refers to this type of numbers
    :param curr_number: the string that represent valid float number
    :return: no return value
    """
    if curr_number[0] == '.' or curr_number[-1] == '.':
        print(f"you wrote {curr_number} , the calculator refers it as {float(curr_number)}")


def append_number_to_list(expression_list: list, number: str):
    """
    the function receives a list that represent valid expression and a string that represent number
    the function tries to convert the number to float and append it to the list
    if the number is not in a float format the function raise an exception
    :param expression_list: list that represent valid expression
    :param number: string that represent number
    :return: the list after the change
    :raise: ValueError: in case number from the string is not in a float format, for example, 25.8.7 is not valid number
    """
    try:
        expression_list.append(float(number))
        check_number_starts_or_ends_with_decimal(number)
    except ValueError:
        raise ValueError(f"Invalid Expression -> the number {number} is not in float format")
    return expression_list


def transform_to_list(expression_string: str) -> list:
    """
    the function receives a string that represent valid input from the user
    the function transforms the string to a list of operands and operators while taking care of casting the operands
    to float type and then returns the list
    :param expression_string: valid expression from user input
    :return: list of operators and operands that represent valid expression according to the input
    """
    expression_list = []
    curr_number = ""
    for i in range(len(expression_string)):
        curr = expression_string[i]
        if curr in NUMBERS:
            curr_number += expression_string[i]
        else:
            if curr_number != "":
                expression_list = append_number_to_list(expression_list, curr_number)
                curr_number = ""
            expression_list.append(curr)
    if curr_number != "":
        expression_list = append_number_to_list(expression_list, curr_number)
    return expression_list


def is_minus_of_number(expression_list: list, index: int) -> bool:
    """
    the function receives list that represent valid expression and index of minus operator in the list
    the function returns True if the minus works as sign changer of False if the minus works as regular operator
    :param expression_list: list that represent valid expression
    :param index: index of minus operator in the list
    :return: True or False according to the role of the minus
    """
    if index == 0 and isinstance(expression_list[1], float):
        return True
    before = expression_list[index - 1]
    after = expression_list[index + 1]
    if isinstance(before, str) and before not in ONLY_LEFT_OPERAND_OPERATORS and before != ')' and \
            isinstance(after, float):
        return True
    return False


def reduction_minuses(expression_list: list) -> list:
    """
    the function receives a list that represent valid expression
    the function iterate over the expression and delete every minus that works as sign changer while changing the
    sign of the number after it and than returns the list after the reduction
    :param expression_list: list that represent valid expression
    :return: list after reduction of minuses
    """
    if len(expression_list) == 1:
        return expression_list
    for i in range(len(expression_list) - 1, -1, -1):
        if expression_list[i] == '-':
            if is_minus_of_number(expression_list, i):
                expression_list.pop(i)
                expression_list[i] *= -1
    return expression_list


def check_parentheses_validation(expression_list: list) -> bool:
    """
    the function receives a list that represent expression
    the function returns True if the parentheses in the expression are all valid or False if not
    :param expression_list: list that represent expression
    :return: True or False according to the state of the parentheses
    """
    stack_parenthesis = []
    for i in range(len(expression_list)):
        if expression_list[i] == '(':
            stack_parenthesis.append('(')
        if expression_list[i] == ')':
            if len(stack_parenthesis) == 0:
                return False
            stack_parenthesis.pop()
    if len(stack_parenthesis) != 0:
        return False
    return True


def is_valid_after_only_right_operand_operator(expression_list: list, index: int) -> bool:
    """
    the function receives list that represent expression and index of an only right operand operator in the list
    the function returns True if the items after the operator in the list are valid or False if not
    :param expression_list: list that represent expression
    :param index: index of an only right operand operator in the list
    :return: True or False according to the validation after the operator
    """
    if index == len(expression_list) - 1:
        return False
    if isinstance(expression_list[index + 1], float):
        return True
    before = expression_list[index]
    while expression_list[index + 1] == '-':
        index += 1
    after_minuses = expression_list[index + 1]
    if after_minuses == '(' or (before == '(' and after_minuses in ONLY_RIGHT_OPERAND_OPERATORS):
        return True
    return False


def check_supported_characters(expression_string: str) -> (bool, str):
    """
    the function receives a string that represent input from the user
    the function return True if all the characters in the string are familiar to the calculator , if not returns
    False and the unfamiliar character
    :param expression_string: user input
    :return: True or False according to all of the characters in the string
    """
    for char in expression_string:
        if not (char in NUMBERS or char in VALID_OPERATORS):
            return False, char
    return True, ' '


def has_any_numbers(expression_string: str) -> bool:
    """
    the function receives a string that represent input from the user
    the function return True if there is at least one digit in the string or False if not
    :param expression_string: user input
    :return: True or False according to all of the characters in the string
    """
    for char in expression_string:
        if char in NUMBERS and char != '.':
            return True
    return False


def is_valid_string_input(expression_string: str):
    """
    the function receives a string that represent input from the user and raise an exception if the input is invalid
    :param expression_string: string that represent input from the user
    :raise ValueError: if one of the characters in the string is invalid or if the string does not contains any digits
    :return: no return value
    """
    is_valid, char = check_supported_characters(expression_string)
    if len(expression_string) == 0:
        raise ValueError("your expression is empty")
    if not is_valid:
        raise ValueError(f"the character {char} cannot be part of the expression")
    if not has_any_numbers(expression_string):
        raise ValueError("your expression does not contain numbers at all")


def check_expression_validation(expression_string: str) -> (bool, list):
    """
    the function receives a string that represent input from the user
    the function call function to checks the validation of the input in the expression,
    if valid calls to function that transform the string to list then
    the function checks the validation of every item in the list and raise exception if one of them is invalid
    the function returns True and the valid list if all the items are valid
    :param expression_string: string that represent input from the user
    :return: True and the valid list if the user's expression is valid
    """
    is_valid_string_input(expression_string)
    expression_list = transform_to_list(expression_string)
    expression_list = reduction_minuses(expression_list)
    first = expression_list[0]
    if isinstance(first, str) and first not in ONLY_RIGHT_OPERAND_OPERATORS and first not in ['-', '(']:
        raise ValueError(f"your expression can't start with the operator {first}")
    if not check_parentheses_validation(expression_list):
        raise ValueError("parenthesis inconsistency in your expression")
    if first in ONLY_RIGHT_OPERAND_OPERATORS and not is_valid_after_only_right_operand_operator(expression_list, 0):
        raise ValueError(f"after the operator {first} it has to be number or parenthesis or sequence of" +
                         " minuses that lead to number or parenthesis")
    for i in range(1, len(expression_list)):
        before = expression_list[i - 1]
        current = expression_list[i]
        if isinstance(current, float):
            if before in ONLY_LEFT_OPERAND_OPERATORS:
                raise ValueError(f"the number {current} can't be after {before}")
        elif current in ONLY_RIGHT_OPERAND_OPERATORS:
            if isinstance(before, float) or before in ONLY_LEFT_OPERAND_OPERATORS or before == ')':
                raise ValueError(f"the operator {current} can't be after {before}")
            if not is_valid_after_only_right_operand_operator(expression_list, i):
                raise ValueError(f"after the operator {current} it has to be number or parenthesis or sequence of" +
                                 "minuses that lead to number or parenthesis")
        elif current == '(':
            if isinstance(before, float) or before in ONLY_LEFT_OPERAND_OPERATORS or before == ')':
                print(f"you type {before} and ( without an operator between them, the calculator" +
                      " puts multiply operator as default")
                expression_list.insert(i, '*')
        elif current in ONLY_LEFT_OPERAND_OPERATORS or current == ')':
            if isinstance(before, str) and before != ')' and before not in ONLY_LEFT_OPERAND_OPERATORS:
                raise ValueError(f"the operator {current} can't be after {before}")
        else:  # current == other operator
            if current != '-':
                if isinstance(before, str) and before not in ONLY_LEFT_OPERAND_OPERATORS and before != ')':
                    raise ValueError(f"the operator {current} can't be after the operator {before}")
    end = expression_list[-1]
    if isinstance(end, str) and end not in ONLY_LEFT_OPERAND_OPERATORS and end != ')':
        raise ValueError(f"your expression can't end with the operator {end}")
    return True, expression_list
