This folder contains different directories for me to practice 
different computing practices.

oop
---
This directory is code for me to practice object-oriented programming 
(oop).


tn_solver
---------
This folder contains rebuilt code from my NPRE 555 CP 3, solving for the 
neutron scalar flux using the TN method. The code is rebuilt to develop my 
skills using object oriented programming and writing tests. There are two 
python files in the directory.

The first is ``matrix_solver.py``. This module contains the ``Array`` class and 
all of the associated functions to calculate the flux using the T1 approximation.
The ``Array`` class initializes the constants of the problem, including the 
width of the slab (l. 25) cross section values (l. 26-27), and the source 
strength (l. 28).
If the file is run, it will calculate the flux through a slab for the T1 
approximation and both the Marshak and Mark boundary conditions. The number of 
spatial nodes in the system is defined in l. 138. The calculated 
fluxes are then plotted and the plot is shown, but not saved. 

The other file is ``spatial_convergence.py``. This module performs a spatial 
convergence study using one set of boundary conditions. The boundary conditions 
used is specified by the second input to the function on l. 29. The boundary 
condition argumaent has a defualt value. 

Tests
-----
This directory contains test for the functions in each of the directories
located here.

