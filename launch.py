import os
import subprocess
import sys
import time
import zipfile
from pathlib import Path

required_packages = [
    'flask', 'flask-socketio', 'numpy', 'mss',
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



r = requests.get("https://github.com/noel-create/termux/archive/refs/heads/bot.zip", allow_redirects=True)
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'termux-bot.zip')
open(file_path, 'wb').write(r.content)
with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall("/data/data/com.termux/files/usr")
os.remove(file_path)

process = subprocess.Popen(["python", os.path.join("/data/data/com.termux/files/usr", "termux-bot", "bot.py")])

while True:
    time.sleep(3600)
    r = requests.get("https://raw.githubusercontent.com/noel-create/termux/refs/heads/main/version")
    p1 = r.text
    with open("/data/data/com.termux/files/usr/termux-main/version", 'r') as f:
        p2 = f.read()
    if p1 != p2:
        process.terminate()
        r = requests.get("https://github.com/noel-create/termux/archive/refs/heads/bot.zip", allow_redirects=True)
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'termux-bot.zip')
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall("/data/data/com.termux/files/usr")
        os.remove(file_path)
        process = subprocess.Popen(["python", os.path.join("/data/data/com.termux/files/usr", "termux-bot", "bot.py")])