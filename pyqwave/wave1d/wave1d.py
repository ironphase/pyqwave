######################################################################################################
# Sirius Toolkit
# Author: Miguel A Sepulveda
#         2018, Sunnyvale CA (USA)
######################################################################################################
import logging 
import numpy as np


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