######################################################################################################
# PyQWave Toolkit
# Authors: Daniel Sepulveda    Toronto ON (Canada)
#          Miguel A Sepulveda  Sunnyvale CA (USA)
#
######################################################################################################
from unittest import TestCase
import pyqwave.helpers

######################################################################################################
class TestHelpers(TestCase):

    def test_is_integer(self):
        
        result = pyqwave.helpers.is_integer(10)
        self.assertTrue(result)

        result = pyqwave.helpers.is_integer(10.4)
        self.assertTrue(not result)

    def test_is_float(self):
        
        result = pyqwave.helpers.is_float(10.25215)
        self.assertTrue(result)

        result = pyqwave.helpers.is_float(10)
        self.assertTrue(not result)

    def test_is_string_integer(self):
        
        result = pyqwave.helpers.is_string_integer("10")
        self.assertTrue(result)

        result = pyqwave.helpers.is_string_integer("10.4")
        self.assertTrue(not result)

    def test_is_string_float(self):
        
        result = pyqwave.helpers.is_string_float("10.235345")
        self.assertTrue(result)

        result = pyqwave.helpers.is_string_float("10A")
        self.assertTrue(not result)
