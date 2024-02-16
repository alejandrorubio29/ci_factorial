
import pytest


from src.functions import factorial

# Test 1
def test_factorial_1():
    assert factorial(1) == 1

# Test 2: nno entero
    
def test_factorial_typeError():
    with pytest.raises(TypeError):
        factorial(1.5) 

# Test 3: entero negativo
        
def test_factorial_ValueError():
    with pytest.raises(ValueError):
        factorial(-1) 

# Test 4: factorial caso general
        
def test_factorial_General():
    assert factorial(5) == 120
