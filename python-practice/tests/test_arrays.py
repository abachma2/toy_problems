import numpy as np

from arrays import Arrays

# Test matrix_solver


def test_matrix_solver1():
    array = Arrays(1, 5)
    exp = np.array([[1.4286], [-0.7143], [1.4286]])
    A = np.array([[1, 2, 0], [2, 1, 2], [0, 2, 1]])
    S = np.array([[0], [5], [0]])
    obs = array.matrix_solver(A, S)
    assert np.all(exp == obs)


def test_matrix_solver2():
    array = Arrays(1, 5)
    exp = 'Error in solving matrix equation'
    obs = array.matrix_solver(np.zeros((3, 3)), np.ones((3, 1)))
    assert np.all(exp == obs)


def test_matrix_solver3():
    array = Arrays(1, 5)
    exp = 'Error in solving matrix equation'
    obs = array.matrix_solver(np.ones((3, 3)), np.ones((2, 1)))
    assert np.all(exp == obs)


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


# Test fill_A_T1
def test_fill_A_T1_1():
    array = Arrays(1, 5)
    exp = np.array([[-0.2273, 0.1, 0, 0, 0],
                    [0.5, -0.5, 0.5, 0, 0],
                    [0, 0.5, -0.5, 0.5, 0],
                    [0, 0, 0.5, -0.5, 0.5],
                    [0, 0, 0, -0.1, 0.2273]])
    exp = np.reshape(exp, (5, 5, 1))
    obs = array.fill_A_T1(5, 'Marshak')
    assert np.all(exp == obs)


def test_fill_A_T1_2():
    array = Arrays(1, 5)
    exp = np.array([[-0.2414, 0.1, 0, 0, 0],
                    [0.5, -0.5, 0.5, 0, 0],
                    [0, 0.5, -0.5, 0.5, 0],
                    [0, 0, 0.5, -0.5, 0.5],
                    [0, 0, 0, -0.1, 0.2414]])
    exp = np.reshape(exp, (5, 5, 1))
    obs = array.fill_A_T1(5, 'Mark')
    assert np.all(exp == obs)


def test_fill_A_T1_1():
    array = Arrays(1, 5)
    exp = np.array([[0, 0.1, 0, 0, 0],
                    [0.5, -0.5, 0.5, 0, 0],
                    [0, 0.5, -0.5, 0.5, 0],
                    [0, 0, 0.5, -0.5, 0.5],
                    [0, 0, 0, -0.1, 0]])
    exp = np.reshape(exp, (5, 5, 1))
    obs = array.fill_A_T1(5)
    assert np.all(exp == obs)


# Test fill_S_T1
def test_fill_S_T1():
    array = Arrays(1, 5)
    exp = np.array([0, 10, 10, 10, 0])
    exp = np.reshape(exp, (5, 1, 1))
    obs = array.fill_S_T1(5)
    assert np.all(exp == obs)
