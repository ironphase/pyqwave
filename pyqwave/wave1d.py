######################################################################################################
# Sirius Toolkit
# Author: Miguel A Sepulveda
#         2018, Sunnyvale CA (USA)
######################################################################################################
import logging 
import numpy as np



######################################################################################################
class cartesian1d(object):
    """
    Define a finite cartesian coordinate grid in 1 dimension. 
    """

    def __init__(self, xmin, xmax, nsteps):
        """
        Allocate a 1-dimensional cartesian basis set |x_i> starting at position xmin to xmax
        for a total of nsteps grid points: |xmin>, |xmin+d>, |xmin+2d>,....|xmax>.
        """

        if nsteps < 2:
            raise Exception("nsteps should be greater that 1")

        if (xmax <= xmin):
            raise Exception("xmin should be smaller than xmax: {} {}".format(xmin,xmax) )

        self.data = np.zeros(nsteps, dtype=np.float64)
        delta = float(xmax - xmin)/(nsteps-1.0)
        for i in range(nsteps):
            self.data[i] = xmin + i * delta


    def dimension(self):

        return self.data.shape[0]


######################################################################################################
class wave1d(object):

    def __init__(self, N):
        """
        wave1d(N) creates a simple 1-dimensional wave function as a numpy array of complex elements.
        N is the dimension of the wave function in 1D. Since the function is complex each element has
        a (real,img) components.

        ....more to come....

        """

        self.data = np.zeros(N, dtype=np.complex128)


    def dimension(self):

        return self.data.shape[0]


    def norm(self):

        """
        Return the norm of the wave function
        TODO
        """
        return 0.0


# TODO:
#   [1] Compute conjugate of a wave function
#   [2] Product-integral of two wavefunctions Int( psi1 * conj(psi2) )