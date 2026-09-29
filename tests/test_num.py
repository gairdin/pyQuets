import pytest

def test_num1(numbers):
    for i in numbers:
        assert i % 2 == 0

def test_num2(numbers):
    for i in numbers:
        assert i % 2 == 0