######################################################################################################
# PyQWave Toolkit
# Authors: Daniel Sepulveda    Toronto ON (Canada)
#          Miguel A Sepulveda  Sunnyvale CA (USA)
#
######################################################################################################
import logging


######################################################################################################
# Define physical constants here (using atomic units only)
#  hbar
#  ....
#


######################################################################################################
def is_string_integer( string ):
    try:
        value = int(string)
        return True
    except ValueError:
        pass

    return False

######################################################################################################
def is_string_float( string ):
    try:
        value = float(string)
        return True
    except ValueError:
        pass

    return False

######################################################################################################
def is_integer( number ):
    return isinstance(number,int)

######################################################################################################
def is_float( number ):
    return isinstance(number, float)

    