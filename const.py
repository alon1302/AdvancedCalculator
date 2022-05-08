# This Python file is used for lists of fixed values in the code

# string that represent all the characters that can be part of a number
NUMBERS = "0123456789."

# A dictionary that contains pairs of operators and their priority to calculate in the expression
# 1 -> the current lowest priority
# 6 -> the current highest priority
OPERATORS_STRENGTH_DICT = {'': -10, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3,
                           '%': 4, '@': 5, '$': 5, '&': 5, '~': 6, '!': 6}

# A list containing regular operators that receive operands on both sides
REGULAR_OPERATORS = ['+', '-', '*', '/', '^', '%', '@', '$', '&']

# A list that contains specials operators that receive one operand from their left
ONLY_LEFT_OPERAND_OPERATORS = ['!']

# A list that contains specials operators that receive one operand from their right
ONLY_RIGHT_OPERAND_OPERATORS = ['~']

# A list that contains all the valid operators that exists in this calculator
VALID_OPERATORS = list(OPERATORS_STRENGTH_DICT.keys()) + ['(', ')']
