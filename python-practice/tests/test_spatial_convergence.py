from spatial_convergence import calculate_delta

import sys

# Test calculate_delta

def test_calculate_delta1():
    exp = 0.2
    obs = calculate_delta(6, 5)
    assert exp == obs

def test_calculate_delta2():
    exp = 1
    obs = calculate_delta(0, 3)
    assert exp == obs

def test_calculate_delta3():
    exp = 'Divide by 0'
    obs = calculate_delta(3, 0)
    assert exp == obs
