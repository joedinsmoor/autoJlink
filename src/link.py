import pylink
import csv


ip_addr = '192.168.10.123:80'
serial_no = 'None'

def lEndian(mNum, speed):
    """Retrieve little endian formatted memory.

        Args:
          mNum (str): CPU Model number for memory acquisition
          speed (int): JTAG Link speed in Khz

        Returns:
          ``Filename of memory acquired``
        """

    link = pylink.JLink()
    link.open(ip_addr='192.168.10.123:0')
    try: 
        link.connect(mNum)
    except TypeError:
        print("Speed invalid")
    except pylink.JLinkException:
        print("Connection Failed, please check connection and any relevant data")
    finally:
        pass
    if link.target_connected:
        try:
            out = link.memory_read(0,0xF0000000) # - Reading memory up to 1.92 GB, future support for changing this memory address to dynamically handle different memory sizes based on CPU model number
        except pylink.JLinkException:
            print("Memory could not be read, please verify connections and try again")
        finally:
            name = output(mNum, out)
    else:
        print("Connection Failed, please restart program, and ensure connections are correct.")
    link.close()
    return name

def info(mNum, speed):
   """Retrieve CPU information for quality assurance and general information purposes.

        Args:
          mNum (str): CPU Model number for memory acquisition
          speed (int): JTAG Link speed in Khz

        Returns:
          ``Tuple of CPU Model, CPU ID, and CPU Name``
        """
   nlink = pylink.JLink()
   nlink.open(ip_addr='192.168.10.123:0')
   information = []
   nlink.connect(mNum)
   information.append(nlink.core_cpu())
   information.append(nlink.core_id())
   information.append(nlink.core_name())
   nlink.close()
   return information

# Returns CPU information to ensure that user is debugging the correct architecture
    

def bEndian(mNum, speed):
    """Retrieve big endian formatted memory.

        Args:
          mNum (str): CPU Model number for memory acquisition
          speed (int): JTAG Link speed in Khz

        Returns:
          ``None``
        """
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
    """Save retrieved memory to binary file with no bit manipulation.

        Args:
          mNum (str): CPU Model number for memory acquisition
          stream (bitstream): Stream of data in hex directly from internal memory

        Returns:
          ``File containing acquired memory``
        """
    link = pylink.JLink()
    filename = mNum
    filename.append('.bin')
    f = open(filename)
    f.write(stream)
    link.close()
    return filename

# Method for saving memory to .bin file without any manipulation, ensuring a hygenic forensic acquisition. 


