import numpy as np
import matplotlib.pyplot as plt

from matrix_solver import Arrays

# Test matrix_solver




# Test fill_A_T1




# Test boundary_conditions
def test_boundary_conditions1():
    array = Arrays(1, 5)
    exp = (-0.2273, 0.2273)
    obs = array.boundary_conditions('Marshak')
    assert exp == obs

def test_boundary_conditions2():
    array = Arrays(1, 5)
    exp = (-0.2414, 0.2414)
    obs = array.boundary_conditions('Mark')
    assert exp == obs

def test_boundary_conditions3():
    array = Arrays(1, 5)
    exp = (0, 0)
    obs = array.boundary_conditions()
    assert exp == obs

# Test fill_S_T1


