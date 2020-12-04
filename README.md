# An assortment of Python scripts for Pentesting

 ```
 /^-----^\
 V  x o  V
  |  Y  |
   \ Q /
   / - \
   |    \
   |     \  OED-JL
   || (___\====
   
   ```
# Modules
pip install pycryptodome
pip install Padding

#  Example scripts

# TCP Clients/Server
tcpClient.py
tcpServer.py

# Encrypted Clients/Server

An experiment, needs a tidy, encrypted the traffic over a tcp socket using AES ECB

# Create an exe from a python script
YOU MUST INSTALL USING THE CMDLINE OF WINDOWS
pip3 install pyinstaller

If you get file cant be on windows check the PATH
ie add c:\python3

pyinstaller
-F - Create with dependancies
-w - no console

You can do in in the Terminal to create a linux executable or cmd line for windows

pyinstaller -F -w client.py

# Alternative make of exe using cx_Freeze (THIS VERSION AVOIDS AV DETECTION BETTER)

pip install cx_Freeze


python setup.py build

Check the build directory

# Deploying the application

python setup.py bdist_msi


# Start a simple HTTP Server
python3 -m http.server 8888
