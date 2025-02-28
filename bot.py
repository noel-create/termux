import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import os
import pyautogui
from nextcord import File
import time
from PIL import Image
import keyboard
import subprocess
import string
import random
import asyncio
import shutil
import datetime
import socket
from datetime import datetime
import win32gui
import win32con
import win32api
import time
import os
import pyautogui
import uuid
import cv2
import webbrowser
import requests
import sys
import win32gui, win32con
from PIL import Image
from typing import Optional
import win32com.client
from pathlib import Path
import psutil


user_profile = os.environ['USERPROFILE']
target_path = os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows')
os.makedirs(target_path, exist_ok=True)

sys.stdout = open(os.path.join(target_path, "skibidi-mainmain", "log.txt"), "a", buffering=1)  # "a" = append mode, "buffering=1" = line buffering
sys.stderr = sys.stdout

user_profile = os.environ['USERPROFILE']
target_path = os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows')
os.makedirs(target_path, exist_ok=True)

pyautogui.FAILSAFE = False

client = commands.Bot(command_prefix = '!', intents=nextcord.Intents.default())

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')
    channel = client.get_channel(1344779173000122470)
    embed = nextcord.Embed(description="Bot online!", title="Bot online!", timestamp=datetime.now(), colour=0x00f51d)
    embed.set_author(name="Termux Bot")
    embed.set_footer(text=f"Termux Bot v.idk")
    channel.send(embed=embed)

testServerId = [1139988299386195981]

@client.slash_command(guild_ids=testServerId, description="Gets the status of the bot.")
async def status(interaction : Interaction):
    await interaction.response.send_message("Requesting status...")
    battery_status = psutil.sensors_battery()
    txt = f"""Battery percentage: {battery_status.percent}%
    Battery plugged: {battery_status.power_plugged}
    Battery left: {battery_status.secsleft}"""

    embed = nextcord.Embed(description=txt, title="Status:", timestamp=datetime.now(), colour=0x00f51d)
    embed.set_author(name="Termux Bot")
    embed.set_footer(text=f"Termux Bot v.idk")
    interaction.channel.send(embed=embed)


@client.slash_command(guild_ids=testServerId, description="Outputs the log file, useful for debugging.")
async def output_log(interaction : Interaction):
    category = interaction.channel.category
    if str(category) == str(ip):
        await interaction.response.send_message("Sending log file...")
        log_path = "log.txt"
        file1 = nextcord.File(log_path, filename='log.txt')
        await interaction.send(file=file1)

token = input("Token: ")
with open("token.txt", "w") as f:
    f.write(token)
client.run(token)