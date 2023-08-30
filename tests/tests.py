import pytest
import pylink

@pytest.fixture(scope="module")
def autoJlinkTest():
    #Testing here will only test to ensure that a given binary can be saved in a given output directory
    #Due to the nature of how this library functions, and the function of JLink as a whole
    #a full test suite is not possible. However, offline testing is being performed using a Segger JTrace Pro
    f.open("testBinary.bin")