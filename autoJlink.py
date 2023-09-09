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
    #print("\n")

print("\n")
file = 'out.bin'

answer = input("Read Memory? (y/n): ")
if answer == 'y' or 'yes':
    with open(r'src/memSizes.json', 'r') as f:
        sizes = json.loads(f)
        if modelNum in sizes:
            addr = 0
            length = sizes[modelNum]
        else:
            addr = input("Enter the starting address for memory acquisition: ")
            length = input("Enter the length of acquisition in bits: ")
        
    ans = input("Does CPU need to be halted for memory acquisition? If unknown, please hit enter (y/n): ")

    print("Memory acquisition starting ...", flush=True)
    filename = lEndian(modelNum, speed, addr, length, ans)
    if(filename == 'Error'):
        print("Could not save memory acquisition to file, please check connections and debugger")
    else:
        print("Memory acquired, saved in ", filename)
else:
    exit()



