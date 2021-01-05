import numpy as np
import matplotlib.pyplot as plt
import math 
import time

from matrix_solver import Arrays

def calculate_delta(new_A, old_A):
    '''
    Calculates delta value to determine convergence

    Parameters:
    ===========
    new_A: array
        array with more nodes, need to determine max
    old_A: float
        maximum value of flux using previous number of nodes
    '''
    return abs(new_A.max()-old_A)/old_A

if __name__ =='__main__':
    num_nodes = 4
    delta = 10
    old_A = 1
    ii = 1
    plt.figure()
    while delta > 1e-4:
        array = Arrays(1, num_nodes)
        array.A = array.fill_A_T1(num_nodes, 'Marshak')
        array.S = array.fill_S_T1(num_nodes)
        array.phi[:, :, 0] = array.matrix_solver(array.A[:,:,0], array.S[:,:,0])
        delta = calculate_delta(array.phi[:, :, 0], old_A)
        old_A = array.phi[:,:,0].max()
        ii += 1
        plt.plot(array.x, array.phi[:, :, 0], label=f'{num_nodes} Nodes')
        num_nodes *= 2
    plt.xlabel('Position (cm)')
    plt.ylabel(r'$\phi (\frac{n}{cm^3})$')
    plt.legend()
    plt.show()
