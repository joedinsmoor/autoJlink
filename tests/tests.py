import pytest
import pylink
from os.path import exists
import os
from pathlib import Path
import sys
sys.path.append('./src')
from link import *

@pytest.fixture(scope="module")

def copy_file(src_path, dest_path):
    with open('AB-L18ER.bin', 'rb') as src_file:
        with open('testCPU.bin', 'wb') as dest_file:
            dest_file.write(src_file.read())

def compare_files(file1, file2):
    with open(file1, 'rb') as f1:
        with open(file2, 'rb') as f2:
            return f1.read() == f2.read()


def autoJlinkAnswer(temp_files):
    src_file, dest_file = temp_files

    copy_file(src_file, dest_file)
    assert compare_files(src_file, dest_file), "Copied contents are not the same."