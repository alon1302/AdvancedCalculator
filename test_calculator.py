import pytest
import solver
import calculator
import exceptions
import validation

SIMPLE_SOLVABLE_EXPRESSIONS = [("1+3", 4), ("8-4.5", 3.5), ("2*3", 6), ("7.8/1.2", 6.5), ("3^3", 27), ("2@10", 6),
                               ("7$2", 7), ("-8&3", -8), ("256%10", 6), ("~1.8", -1.8), ("~-2", 2), ("4!", 24),
                               ("(((((52.69)))))", 52.69), ("5*--(2!)", 10), ("2-(-(--~(9)))", -7), ("4+(5!+3)", 127)]

COMPLEX_SOLVABLE_EXPRESSIONS = [("-1--~---(2--(~--1+-(1-(-1)+~5)-~-5))", -2),
                                ("8--(7-9)*2^(10-9*(8+(7^-(-2)+5)))------- 6    +34", 36),
                                ("7/ 48+ 7!* (48/ 3! -5 )&7945/  4956", 3.196680790960452),
                                ("(8*(7+(8-9)-5)+7) * (8/(5.2+2.8))", 15),
                                ("(8&5 + ((35.8&21)-13)!/(13@17.3)-~(10*-8))", 2586.3861386138615),
                                ("3+2*(3!-7)-3^6+(8&7)", -721),
                                ("(-~--(  11 *5 +(31&4)/3.2    ) +   -(17.35    @4!)+4!)", 59.575),
                                ("((( -(-(8! /7.8)+4 )-128&15.  3) *2)  )", 10299.861538461539),
                                ("28.5/(4/8)---~-4!+15&7*(1+1-1)", 40),
                                ("((-~--(6-2)!) - 25@ 7*-~5  +(15/2)+11)", -37.5),
                                ("-(8*7.4+45%2 -~-5!+(5+~5)+11^2^0.5)", 48.8),
                                ("-1--~---(2--(~--1+-(1-(-1)+~5)-~-5))", -2),
                                ("~(5+2*6^(3+1))@(3!-7)", -1299),
                                ("5--((1+2)+(3*(2+1)))", 17),
                                ("1^2*(5+2^(3-1))*(2+3)+2^3*2", 61),
                                ("2.80808-(9+0)--9.8*-(9.909@(7$2+8))^2", 1513.93086845),
                                ("-2+(9*-(9@-(3+4!)+~(9+8.5))^2)+2^(9$3)", 6830.25),
                                ("1&(2!-~5^4*(17%5*2)/10)+100-100", -248)]

INVALID_EXPRESSIONS = ["3^*2", "+4", "7*2+", "7~7", "((4+65)*4", "hsdefgef", "", "       ", "+", ".", "~-~5",
                       "5!56", "4!~5", "5+!3", "3+~~4"]

INVALID_OPERATIONS = ["1/0", "-5!", "-~-5!", "5/(2-2)", "-5^0.5", "5%(2/2-1)", "(7.5-9)!"]


@pytest.mark.parametrize("test_input, result", SIMPLE_SOLVABLE_EXPRESSIONS + COMPLEX_SOLVABLE_EXPRESSIONS)
def test_solver_with_solution(test_input: str, result: float):
    """
    the function receives string that represent valid expression and float that represent the result of the expression
    the function checks if the results are matching
    :param test_input: string that represent valid expression
    :param result: float that represent the result of the expression
    """
    assert solver.test_calculate_valid_expression(test_input) == result


@pytest.mark.parametrize("test_input", INVALID_EXPRESSIONS)
def test_invalid_expression_exception_raise(test_input):
    """
    the function receives string that represent invalid expression that supposed to raise ValueError exception while
    checking the validation. the function checks if the expected exception has raised
    :param test_input: string that represent valid expression
    """
    with pytest.raises(ValueError):
        validation.check_expression_validation(test_input)


@pytest.mark.parametrize("test_input", INVALID_OPERATIONS)
def test_invalid_operation_exception_raise(test_input):
    """
    the function receives string that represent valid expression that supposed to raise InvalidOperation exception while
    the solving. the function checks if the expected exception has raised
    :param test_input: string that represent valid expression
    """
    with pytest.raises(exceptions.InvalidOperation or exceptions.LargeNumberError):
        calculator.test_calculate_valid_expression(test_input)


if __name__ == '__main__':
    pytest.main()
