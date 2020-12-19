import numpy as np
import matplotlib.pyplot as plt
import math
import time


class Arrays(object):
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
        self.x, self.delta_x = np.linspace(-self.a, self.a, num_nodes,
                                           retstep=True)

        self.phi = np.zeros((num_nodes, 1, math.ceil(N / 2)))
        self.A = np.zeros((num_nodes, num_nodes, math.ceil(N / 2)))
        self.S = np.zeros((num_nodes, 1, math.ceil(N / 2)))

    def matrix_solver(self, A, S):
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

    def fill_A_T1(self, num_nodes, bc='None'):
        '''
        Fills A constant matrix to create a tridiagonal matrix for the T1
        approximation

        Parameters:
        ===========
        A: array
          Constant array to be filled
        num_nodes: int
          number of spatial nodes in the system, this number is looped over
          to fill the matrix as needed to account for boundary conditions
        bc: string
          Name of boundary condition to be applied. Default is no boundary
          conditions are applied.
        '''
        for xx in range(num_nodes):
            self.A[xx, xx, 0] = -1 / (self.sigma_t * self.delta_x) + \
                    (self.sigma_t - self.sigma_s) * self.delta_x
            if xx > 0:
                self.A[xx, xx - 1, 0] = 1 / (2 * self.sigma_t * self.delta_x)
                if xx == num_nodes - 1:
                    self.A[xx, xx - 1, 0] = -1 / self.delta_x
                    if bc == 'Marshak':
                        self.A[xx, xx, 0] = 1 / self.delta_x + \
                            4 * self.sigma_t / np.pi
                    elif bc == 'Mark':
                        self.A[xx, xx, 0] = 1 / self.delta_x + \
                            np.sqrt(2) * self.sigma_t
            elif xx < num_nodes - 1:
                self.A[xx, xx + 1, 0] = 1 / (2 * self.sigma_t * self.delta_x)
                if xx == 0:
                    self.A[xx, xx + 1, 0] = 1 / self.delta_x
                    if bc == 'Marshak':
                        self.A[xx, xx, 0] = -1 / self.delta_x - \
                            4 * self.sigma_t / np.pi
                    elif bc == 'Mark':
                        self.A[xx, xx, 0] = -1 / self.delta_x - \
                            np.sqrt(2) * self.sigma_t
            
        return self.A

    def fill_S_T1(self, num_nodes):
        '''
        Fills S constant matrix to create a column matrix for the T1
        approximation

        Parameters:
        ===========
        S: array
          Constants array to be filled
        num_nodes: int
          number of spatial nodes in the system
        '''
        for xx in range(num_nodes):
            if xx == 0:
                self.S[xx, 0, 0] = 0
            elif xx == num_nodes - 1:
                self.S[xx, 0, 0] = 0
            else:
                self.S[xx, 0, 0] = self.q * self.delta_x
        return self.S


if __name__ == '__main__':
    plt.figure()
    for bc in ['Marshak', 'Mark']:
        tic = time.perf_counter()
        array = Arrays(1, 10)
        array.A = array.fill_A_T1(10, bc)
        array.S = array.fill_S_T1(10)
        print(array.A[1,:,0])
        array.phi[:, :, 0] = array.matrix_solver(
            array.A[:, :, 0], array.S[:, :, 0])
        plt.plot(array.x, array.phi[:, :, 0], label=f'{bc} BC')
        toc = time.perf_counter()
        print(f'{toc-tic} s')
    plt.xlabel('Position (cm)')
    plt.ylabel(r'$\phi$(x) $\frac{n}{cm^3}$')
    plt.legend()
    plt.show()
