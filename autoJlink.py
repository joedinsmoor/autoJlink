import re
import csv
from src.link import *

modelNum = input("Input CPU Model Number: ")
print(modelNum)

speed = input("Please enter JTAG connection speed, if unknown, please hit enter: ")
if speed == '':
    speed = 4000

print(info(modelNum, speed))

answer = input("Read Memory? (y/n)")
if answer == 'yes':
    lEndian(modelNum, speed)
else:
    exit()


