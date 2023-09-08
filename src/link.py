import pylink
import json
import os


ip_addr = '192.168.10.123:80'
serial_no = 'None'

memSizes = "memSizes.json"

#memDict = json.load(memSizes)

def lEndian(mNum, speed, saddr, length, ans):
    """Retrieve little endian formatted memory.

        Args:
          mNum : str
            CPU Model number for memory acquisition
          speed : int
            JTAG Link speed in Khz
          saddr : int
            Starting address for memory acquisition
          length : int 
            length of total acquisition in bits
          ans : bool
            flag for determining whether halt is necessary

        Returns:
          filname : str
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
        if ans == 'y' or '':
            res = link.halt()
        try:
            out = link.memory_read(addr=saddr,num_units=length) # - Read specified amount of memory, future support for changing this memory address to dynamically handle different memory sizes based on CPU model number
        except pylink.JLinkException:
            print("Memory could not be read, please verify connections and try again")
        finally:
            try: 
                name = output(mNum, out)
            except MemoryError:
                pass
            finally:
                return 'Error'
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
    information.append("Debugger Information:")
    information.append(nlink.connected_emulators(host=1))
    information.append("CPU Serial Number:")
    information.append(nlink.core_cpu())
    information.append("Core ID:")
    information.append(nlink.core_id())
    information.append("Core Name:")
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
    size = 100

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
            while size != 10000000:
                out = link.memory_read(0,size) # - Reading memory up to 1.92 GB, future support for changing this memory address to dynamically handle different memory sizes based on CPU model number
                size = size * 10
        except pylink.JLinkException:
            print("Memory could not be read, please verify connections and try again")
        finally:
            name = output(mNum, out)
    else:
        print("Connection Failed, please restart program, and ensure connections are correct.")
    link.close()
    return name

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
    filename = filename + '.bin'
    f = open(filename, "w")
    for out in stream:
        f.write(out+"\n")
    if(os.path.getsize(filename) == 0):
        raise MemoryError
    link.close()
    return filename

# Method for saving memory to .bin file without any manipulation, ensuring a hygenic forensic acquisition. 


