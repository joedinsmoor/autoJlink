import re
import csv
from src.link import *

modelNum = input("Input CPU Model Number: ")

speed = input("Please enter JTAG connection speed, if unknown, please hit enter: ")
if speed == '':
    speed = 4000

cpuInfo = info(modelNum, speed)
for inform in cpuInfo:
    print(inform)
    print("\n")


file = 'out.bin'

answer = input("Read Memory? (y/n)")
if answer == 'y' or 'yes':
    print("Memory acquisition starting ...", flush=True)
    filename = lEndian(modelNum, speed)
    print("Memory acquired, saved in ", filename)
else:
    exit()



