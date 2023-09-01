import re
import pylink
import csv




def lEndian(mNum, speed):
    link = pylink.JLink()
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
   nlink = pylink.JLink()
   information = ''
   nlink.connect(mNum, speed)
   information.append(nlink.core_cpu())
   information.append(nlink.core_id())
   information.append(nlink.core_name())
   nlink.close()
   return information

    

def bEndian(mNum, speed):
    pass

def output(mNum, stream):
    link = pylink.JLink()
    filename = mNum
    filename.append('.bin')
    f = open(filename)
    f.write(stream)
    link.close()
    return True


