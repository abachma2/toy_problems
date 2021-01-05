from spatial_convergence import calculate_delta

import sys

# Test calculate_delta

def test_calculate_delta():
    exp = 1
    obs = calculate_delta(4, 2)
    assert exp == obs
