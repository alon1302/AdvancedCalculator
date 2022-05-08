from validation import *
from calculator import *


def evaluate_expression(expression_string) -> float:
    """
    the function receives a string that represent input from the user
    the function call the functions to check the validation and to calculate the expression
    in case of an error that has raised the function prints the message to the user
    :param expression_string: The expression we would like to solve as a string.
    :return: The result of said evaluation.
    """
    is_valid = False
    expression_list = []
    try:
        is_valid, expression_list = check_expression_validation(expression_string)
    except ValueError as e:
        print(f"Invalid Expression -> {e}, please enter valid expression\n")
    if is_valid:
        try:
            result = calculate_full_list(expression_list)
            return result
        except InvalidOperation as e:
            print(f"Invalid Arithmetic Operation -> {str(e)} \n")
        except LargeNumberError as e:
            print(e, "\n")
    return None
