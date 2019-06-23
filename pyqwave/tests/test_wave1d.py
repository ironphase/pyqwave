######################################################################################################
# PyQWave Toolkit
# Authors: Daniel Sepulveda    Toronto ON (Canada)
#          Miguel A Sepulveda  Sunnyvale CA (USA)
#
######################################################################################################
import logging
from unittest import TestCase
import pyqwave

######################################################################################################
class TestWave1d(TestCase):

     def test_wave1d_init(self):
        
        w1 = pyqwave.wave1d.wave1d(32)
        self.assertTrue( w1.dimension() == 32 )

