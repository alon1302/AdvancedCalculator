from const import *
from exceptions import *
from validation import *


def add(*operands) -> float:
    """
    The function receives several operands and calculates their sum
    :param operands: few operands
    :return: the result of the addition
    """
    return sum(operands)


def sub(operand1, operand2) -> float:
    """
    The function receives two operands and calculates their subtraction
    :param operand1: the first operand
    :param operand2: the second operand
    :return: the result of the subtraction
    """
    return operand1 - operand2


def mul(operand1, operand2) -> float:
    """
    The function receives two operands and calculates their multiplication
    :param operand1: the first operand
    :param operand2: the second operand
    :return: the result of the multiplication
    """
    return operand1 * operand2


def div(operand1, operand2) -> float:
    """
    The function receives two operands and calculates the division of the first by the second
    if the second operand is equal to 0: raise exception
    :param operand1: the first operand
    :param operand2: the second operand
    :return: the result of the division
    :raise: InvalidOperation: if the second operand is equal to 0
    """
    if operand2 == 0:
        raise InvalidOperation(f"Division By Zero -> you try to calculate the result of: {operand1} / 0")
    else:
        return operand1 / operand2


def power(operand1, operand2) -> float:
    """
    The function receives two operands and calculates the first to the power of the second
    if the result is complex number or the result is bigger than the float infinity : raise exception
    :param operand1: the first operand
    :param operand2: the second operand
    :return: the result of the power
    :raise: InvalidOperation: if the result of the power is complex number
    :raise: LargeNumberError: if the result is bigger than the float infinity
    """
    if operand1 < 0 and int(operand2) != operand2:
        raise InvalidOperation(
            f"Complex Result of Power -> you tried to calculate the result of: {operand1} ^ {operand2}")
    else:
        try:
            return pow(operand1, operand2)
        except OverflowError:
            raise LargeNumberError("Reached Float Infinity")


def avg(*operands) -> float:
    """
    The function receives several operands and calculates their average
    :param operands: few operands
    :return: the average of the operands
    """
    return sum(operands) / len(operands)


def maximum(*operands) -> float:
    """
    The function receives several operands and returns the maximum between them
    :param operands: few operands
    :return: the maximum between the operands
    """
    return max(operands)


def minimum(*operands) -> float:
    """
    The function receives several operands and returns the minimum between them
    :param operands: few operands
    :return: the minimum between the operands
    """
    return min(operands)


def module(operand1, operand2) -> float:
    """
    The function receives two operands and calculates the module of the first by the second
    if the second operand is equal to 0: raise exception
    :param operand1: the first operand
    :param operand2: the second operand
    :return: the result of the module
    :raise: InvalidOperation: if the second operand is equal to 0
    """
    if operand2 == 0:
        raise InvalidOperation(f"Module By Zero -> you try to calculate the result of: {operand1} % {operand2}")
    else:
        return operand1 % operand2


def negative(operand) -> float:
    """
    The function receives an operand and returns its inverse
    :param operand: the operand
    :return: the inverse of the operand
    """
    return -1 * operand


def factorial(operand: float) -> float:
    """
    The function receives an operand and calculate its factorial
    if the operand is not a natural number or the result is bigger than the float infinity: raise exception
    :param operand: the operand
    :return: the factorial of the operand
    :raise: InvalidOperation: if the operand is not a natural number
    :raise: LargeNumberError: if the result is bigger than the float infinity
    """
    if 0 <= operand and operand.is_integer():
        return_value = 1.0
        for i in range(2, int(operand) + 1):
            if return_value == float('inf'):
                raise LargeNumberError("Reached Float Infinity")
            return_value *= i
        return return_value
    else:
        raise InvalidOperation(f"Factorial of Non Natural Number -> you try to calculate the result of: ({operand})!")


# a dictionary that contains pairs of operators and their calculation function
# for every operator key, the value is his calculation function
OPERATORS_TO_FUNCTIONS_DICT = {'+': add, '-': sub, '*': mul, '/': div, '^': power, '%': module,
                               '@': avg, '$': maximum, '&': minimum, '~': negative, '!': factorial}


def calculate(operator, *operands) -> float:
    """
    the function receives an operator and several operands and calls the specific function for the operator according
    to the dictionary of operations with the operands
    if the result that has returned is bigger than the float infinity: raise exception
    :param operator: the operator
    :param operands: the operands
    :raise LargeNumberError: if result is bigger than the float infinity
    :return: the result that has returned from the specific operator function
    """
    result = OPERATORS_TO_FUNCTIONS_DICT[operator](*operands)
    if result == float('inf'):
        raise LargeNumberError("Reached Float Infinity")
    return result


def find_max_operator(expression_list: list) -> (str, int):
    """
    the function receives a list that represent a valid expression without parenthesis
    the function searches for the operator who must receive first treatment
    according to the operator strength dictionary
    than return this operator and its index in the list
    :param expression_list: list that represent a valid expression without parenthesis
    :return: the first operator to treat and its index in the list
    """
    max_operator = ''
    max_operator_index = -1
    for i in range(len(expression_list)):
        if expression_list[i] in OPERATORS_TO_FUNCTIONS_DICT.keys():
            if OPERATORS_STRENGTH_DICT[expression_list[i]] > OPERATORS_STRENGTH_DICT[max_operator]:
                max_operator = expression_list[i]
                max_operator_index = i
    return max_operator, max_operator_index


def remove_part_of_the_list(list_to_change: list, index1: int, index2: int) -> list:
    """
    the function receives a list and two indexes
    the function removes a slice of the list between the indexes and returns the list after the change
    in case of invalid parameters returns None
    :param list_to_change: a list to change
    :param index1: index to the slice remove
    :param index2: index to the slice remove
    :return: the list after the changes
    """
    from_index = min(index1, index2)
    to_index = max(index1, index2)
    if from_index < len(list_to_change):
        first_part = list_to_change[:from_index]
        if to_index < len(list_to_change):
            second_part = list_to_change[to_index + 1:]
            return first_part + second_part
        else:
            return first_part


def send_to_calculate(expression_list: list, operator: str, index: int):
    """
    the function receives a list that represent a valid expression without parenthesis, an operator and its index in the
    list. the function checks what type of operator is it and calls to the generic calculate function with the operator
    and the matching operands than the function inserts the result to the right place in the list and returns the list
    :param operator: the operator
    :param expression_list: list that represent a valid expression without parenthesis
    :param index: the index of the operator in the list
    :return: the list after the calculation
    """
    if operator in ONLY_LEFT_OPERAND_OPERATORS:
        result = calculate(operator, expression_list[index - 1])
        expression_list = remove_part_of_the_list(expression_list, index - 1, index)
        expression_list.insert(index - 1, result)
    elif operator in ONLY_RIGHT_OPERAND_OPERATORS:
        result = calculate(operator, expression_list[index + 1])
        expression_list = remove_part_of_the_list(expression_list, index, index + 1)
        expression_list.insert(index, result)
    else:  # the operator is regular
        result = calculate(operator, expression_list[index - 1], expression_list[index + 1])
        expression_list = remove_part_of_the_list(expression_list, index - 1, index + 1)
        expression_list.insert(index - 1, result)
    return expression_list


def find_parentheses(expression_list: list) -> (int, int):
    """
    the function receives a list that represent a valid expression and searches parentheses
    the function returns the indexes of matching parentheses or -1 if there are no parentheses in the expression
    :param expression_list: list that represent a valid expression
    :return: the index of the open and the close parentheses or -1 if there are no parentheses
    """
    open_index = -1
    close_index = -1
    for i in range(len(expression_list)):
        if expression_list[i] == '(':
            open_index = i
        if expression_list[i] == ')':
            close_index = i
            break
    return open_index, close_index


def calculate_valid_list_without_parentheses(expression_list: list) -> float:
    """
    recursive function that receives a list that represent a valid expression without parenthesis
    the function breaks down the expression into small expressions and calculates them using recursion in logic order
    according to the operator strength dictionary and thus calculates the total expression result
    :param expression_list: list that represent a valid expression without parenthesis
    :return: the result of the expression
    """
    expression_list = reduction_minuses(expression_list)
    if len(expression_list) == 1:
        return expression_list[0]
    max_operator, max_operator_index = find_max_operator(expression_list)
    expression_list = send_to_calculate(expression_list, max_operator, max_operator_index)
    return calculate_valid_list_without_parentheses(expression_list)


def calculate_full_list(expression_list: list) -> float:
    """
    recursive function that receives a list that represent a valid expression
    the function breaks down the expression into small expressions without parentheses using recursion  and call to the
    function that calculate expressions without parentheses
    the function replace the small expression with the returns result and call for the function again
    :param expression_list: list that represent a valid expression without parenthesis
    :return: the result of the expression
    """
    expression_list = reduction_minuses(expression_list)
    open_index, close_index = find_parentheses(expression_list)
    if open_index == -1:
        return calculate_valid_list_without_parentheses(expression_list)
    curr_expression = expression_list[open_index + 1:close_index]
    curr_result = calculate_valid_list_without_parentheses(curr_expression)
    expression_list = remove_part_of_the_list(expression_list, open_index, close_index)
    expression_list.insert(open_index, curr_result)
    return calculate_full_list(expression_list)


def test_calculate_valid_expression(expression_string) -> float:
    """
    test function
    the function receives string that represent valid expression and calls the functions that evaluates it
    :param expression_string: The expression we would like to solve as a string.
    :return: The result of the evaluation.
    """
    expression_string = expression_string.replace(" ", "")
    expression_string = expression_string.replace("\t", "")
    expression_list = transform_to_list(expression_string)
    result = calculate_full_list(expression_list)
    return result
