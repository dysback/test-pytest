import pytest
from utils.math import *


@pytest.fixture
def ffibo_data():
    return [[0, 1],  [2, 2], [5, 5], [10, 55]]

@pytest.mark.parametrize("fibo_data", [[0, 0],  [2, 1], [5, 5], [10, 55]])
def test_fibo(fibo_data):
    assert fibo(fibo_data[0]) == fibo_data[1]

@pytest.mark.parametrize("fibo_data", [-1, -2, -3, -13])
def test_fibo_exception(fibo_data):
    with pytest.raises(ValueError):
        fibo(fibo_data)

@pytest.mark.parametrize("fact_data", [[0, 1],  [1, 1], [3, 6], [8, 40320]])
def test_fact(fact_data):
    assert fact(fact_data[0]) == fact_data[1]

@pytest.mark.parametrize("fact_data", [-1, -2, -3, -13])
def test_fact_exception(fact_data):
    with pytest.raises(ValueError):
        fibo(fact_data)
