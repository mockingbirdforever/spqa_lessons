from calculator import Calculator
import pytest

calculator = Calculator()


@pytest.mark.positive_test
def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9
