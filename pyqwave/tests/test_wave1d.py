######################################################################################################
# PyQWave Toolkit
# Authors: Daniel Sepulveda    Toronto ON (Canada)
#          Miguel A Sepulveda  Sunnyvale CA (USA)
#
######################################################################################################
import logging
import math
from unittest import TestCase
import pyqwave.wave1d as wave1d

######################################################################################################
class TestWave1d(TestCase):

   def test_wave1d_init(self):
        
      w1 = wave1d.wave1d(32)
      self.assertTrue( w1.dimension() == 32 )

   def test_cartesian1d_init(self):
        
      x1 = wave1d.cartesian1d(0.0, 10.0, 11)
      self.assertTrue( x1.dimension() == 11 )

      for i in range(11):
         self.assertTrue( math.fabs(x1.data[i] - 1.0 * i) < 1.e-6 )

