from src.math_operation import *

def test_add():
    assert add(5,2)==7
    assert add(-5,2)==3

def test_sub():
    assert sub(5,2)==3
    assert sub(-5,2)==7
