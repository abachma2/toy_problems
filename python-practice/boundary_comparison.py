import numpy as np
import matplotlib.pyplot as plt
import time

from arrays import Arrays

if __name__ == '__main__':
    plt.figure()
    for bc in ['Marshak', 'Mark']:
        num_nodes = 100
        tic = time.perf_counter()
        array = Arrays(1, num_nodes)
        array.A = array.fill_A_T1(num_nodes, bc)
        array.S = array.fill_S_T1(num_nodes)
        array.phi[:, :, 0] = array.matrix_solver(
            array.A[:, :, 0], array.S[:, :, 0])
        plt.plot(array.x, array.phi[:, :, 0], label=f'{bc} BC')
        toc = time.perf_counter()
        print(f'{toc-tic} s')
    plt.xlabel('Position (cm)')
    plt.ylabel(r'$\phi$(x) $\frac{n}{cm^3}$')
    plt.legend()
    plt.show()