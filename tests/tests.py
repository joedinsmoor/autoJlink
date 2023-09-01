import pytest
import pylink
from os.path import exists
import os
from pathlib import Path
import sys
sys.path.append('../src')
from src.link import *

@pytest.fixture(scope="module")
def autoJlinkTest(filename):
    #Testing here will only test to ensure that a given binary can be saved in a given output directory
    #Due to the nature of how this library functions, and the function of JLink as a whole
    #a full test suite is not possible. However, offline testing is being performed using a Segger JTrace Pro
    model = 'testCPU'
    binary = 'AB-L18ER.bin'
    return(output(model, binary))


def autoJlinkAnswer():
    assert autoJlinkTest('AB-L18ER.bin') == 'testCPU.bin'