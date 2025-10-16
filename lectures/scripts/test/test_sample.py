import pytest

# general functions

def add(x ,y):

    return x + y

def subtract(x, y):

    return x - y

# tests for the above defined functions

def test_add():

    assert add(2, 3) == 5

def test_subtract():

    assert subtract(5, 3) == 2

def test_add_mirror():

    assert add(5, 2) == add(2, 5)

def test_subtract_mirror():

    """
    rationale:
    
    a-b = -(b-a) 

    """

    assert subtract(5, 2) == -subtract(2, 5)

def test_add_type_error():             # this test will expect a TypeError to be raised
    with pytest.raises(TypeError):
        add('2', 3)