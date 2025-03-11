from cats.math import add,sub,mul,div
import pytest

def test_add():
    assert add(1,2) == 3
    assert add(0,0) == 0
    assert add(-1,1) == 0

def test_sub():
    assert sub(1,2) == -1
    assert sub(0,0) == 0
    assert sub(-1,1) == -2
    
def test_mul():
    assert mul(1,2) == 2
    assert mul(0,0) == 0
    assert mul(-1,1) == -1
    
def test_div():
    assert div(1,2) == 0.5
    assert div(-1,1) == -1
    with pytest.raises(TypeError):
        div(1,0) 
