## autoJlink
Scripts for automatic memory acquisiton using JLink

Used for automatic memory acquisition of ARM CPUs using JTAG and the Segger JLink libraries. 

Usage:

``` pip -r requirements.txt ```
``` python3 autoJlink.py ```

Support:

Any CPUs supported by the Segger JLink, Jtrace, or JTrace Pro are supported here. A full compatibility list can be found [here](https://www.segger.com/supported-devices/jlink/)

NOTE:

If you have the python library PyLink installed, and you do not have PyLink-Square installed, uninstall and remove any trace of Pylink before installing and running this program. The naming conventions of these libraries causes unfixable issues, which I cannot change. 

Troubleshooting:

If you get an error like: ```TypeError: Expected to be given a valid DLL.``` on windows, you must add your JLink dll to path, or copy it to the autoJLink directory. A command to add it to path is: ```set PATH=%PATH%;path\to\jlink\dll\```

