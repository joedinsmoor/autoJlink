import re
import pylink
import csv




def lEndian(mNum, speed):
    link = pylink.jlink()
    try: 
        link.connect(mNum, speed)
   # except JLinkException:
    #    print("Connection Failed")
    except TypeError:
        print("Speed invalid")
    finally:
        pass
    if link.target_connected:
        link.memory_read(0,0xF0000000)
    else:
        print("Connection Failed, please restart program, and ensure connections are correct.")
    link.close()

def info(mNum, speed):
   link = pylink.jlink()
   information = ''
   link.connect(mNum, speed)
   information.append(link.core_cpu())
   information.append(link.core_id())
   information.append(link.core_name())
   link.close()
   return information

    

def bEndian(mNum, speed):
    pass

def output(mNum, stream):
    link = pylink.jlink()
    filename = mNum
    filename.append('.bin')
    f = open(filename)
    f.write(stream)
    link.close()
    return True


