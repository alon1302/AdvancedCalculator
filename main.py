from calculator import *
from validation import *
from solver import *

FINISH_FLAG = "done"


def main():
    """
    the main function of this project
    the function get expression input from the user as long as the input does not contain the word "done"
    the function sends the expression to the function that evaluate it and than prints the result
    in case of the user type the word done or the keys ctrl+d has pressed the program will stop
    :return: no return value
    """
    while True:
        try:
            expression = input("insert expression to evaluate (write done to quit): ")
            expression = expression.replace(" ", "")
            expression = expression.replace("\t", "")
            if FINISH_FLAG == expression.lower():
                print("you typed the word \"done\", want to continue evaluate expressions? please rerun the project")
                return
            result = evaluate_expression(expression)
            if result is not None:
                if result == -0:
                    result = 0
                if result.is_integer():
                    result = int(result)
                print(f"the result is: {result} \n")
        except EOFError as e:
            print("ERROR -> special key is not recognize by the system, please rerun the project")
            return


if __name__ == '__main__':
    main()
