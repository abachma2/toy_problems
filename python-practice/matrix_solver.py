import numpy as np
import matplotlib.pyplot as plt
import math
import time


class Arrays():
    '''
    Contains contants and methods related to the arrays used with array
    '''

    def __init__(self, N, num_nodes):
        '''
        Constants and zero arrays to initialize once the class is called.

        Parameters:
        ===========
        N: int
          order of T_N function used, arrays are initialized to (N+1)/2
          size
        num_nodes: int
          number of spatial nodes in the geometry
        '''
        self.a = 20
        self.sigma_t = 0.1
        self.sigma_s = 0.05
        self.q = 1

        self.phi = np.zeros((num_nodes, 1, mat.ceil(N / 2)))
        self.A = np.zeros((num_nodes, num_nodes, mat.ceil(N / 2)))
        self.S = np.zeros((num_nodes, 1, mat.ceil(N / 2)))

    def matrix_solver(A, S):
        '''
        Performs matrix inversion and multiplication to solve the equaition
        Ax = B, arrays must have the same number of rows

        Parameters:
        ===========
        A: array
          Array of constants, this array is inverted before being multiplied
        S: array
          Array of values not multiplied by the independent variable
        '''
        return np.matmul(np.linalg.inv(A), S)
