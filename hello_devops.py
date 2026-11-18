#!/usr/bin/env python3
"""My first DevOps script: prints basic info about this machine."""

import socket
import platform
from datetime import datetime

hostname = socket.gethostname()
os_name = platform.system()
python_version = platform.python_version()
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"Hostname : {hostname}")
print(f"OS       : {os_name}")
print(f"Python   : {python_version}")
print(f"Time     : {now}")
