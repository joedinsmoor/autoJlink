import re
import pylink
import csv


link = pylink.jlink()

def lEndian(mNum, speed):
    try: 
        link.connect(mNum, speed)
   # except JLinkException:
    #    print("Connection Failed")
    except TypeError:
        print("Speed invalid")
    finally:
        pass

def info(mNum, speed):
   information = ''
   information.append(link.core_cpu())
   information.append(link.core_id())
   information.append(link.core_name())
   return information

    

def bEndian(mNum, speed):
    pass

def output(stream, mNum):
    pass

link.close()