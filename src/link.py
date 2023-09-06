import pylink
import csv




def lEndian(mNum, speed):
    link = pylink.JLink()
    try: 
        link.connect(mNum, speed)
    except TypeError:
        print("Speed invalid")
    except all:
        print("Connection Failed")
    finally:
        pass
    if link.target_connected:
        link.memory_read(0,0xF0000000) # - Reading memory up to 1.92 GB, future support for changing this memory address to dynamically handle different memory sizes based on CPU model number
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

# Returns CPU information to ensure that user is debugging the correct architecture
    

def bEndian(mNum, speed):
    link = pylink.JLink()
    try: 
        link.connect(mNum, speed)
    except TypeError:
        print("Speed invalid")
    except all:
        print("Connection Failed")
    finally:
        pass
    if link.target_connected:
        link.memory_read(0,0xF0000000) # - Reading memory up to 1.92 GB, future support for changing this memory address to dynamically handle different memory sizes based on CPU model number
    else:
        print("Connection Failed, please restart program, and ensure connections are correct.")
    link.close()

def output(mNum, stream):
    link = pylink.JLink()
    filename = mNum
    filename.append('.bin')
    f = open(filename)
    f.write(stream)
    link.close()
    return True

# Method for saving memory to .bin file without any manipulation, ensuring a hygenic forensic acquisition. 


