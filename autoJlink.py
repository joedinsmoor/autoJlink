import re
import csv
from src.link import *

modelNum = input("Input CPU Model Number: ")

speed = input("Please enter JTAG connection speed, if unknown, please hit enter: ")
if speed == '':
    speed = 4000

cpuInfo = info(modelNum, speed)
print(cpuInfo)


file = 'out.bin'

answer = input("Read Memory? (y/n)")
if answer == 'yes':
    lEndian(modelNum, speed)
    #output(modelNum, file)
else:
    exit()


