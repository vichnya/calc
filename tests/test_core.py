import pytest
from src.calculator.core import calculate

def test_calculate_simple_sum():
    result = calculate(op1=1, op2=2, op3=3)
    assert result == 6

def test_calculate_zero():
    result = calculate(op1=0, op2=0)
    assert result == 0
