#DownLoader
import os
import time
import sys

DownLoader = input ('Hey Boss DownLoad Starter Pip? [y/n] : ')

if DownLoader == 'y':
  print('DownLoad Started By OS Engine.')
  time.sleep(1)
  os.system('pip install colorama')
  os.system('pip install shutil')
  os.system('pip install flask')
  os.system('pip install webbrowser')
  #Not Completed

elif DownLoader == 'n':
  print('System : WARNING Pip Not Install = Not Work Python Script Or Bash')

else:
  print('Not Sported This Value!!! ')
  sys.exit()
  
#importer
import sys
import time
import flask
import shutil
import random
import hashlib
import colorama
import webbrowser

#Froms
from colorama import *

#Sp, Si def
def sp(text, delay=0.02):
    for char in str(text):
        print(char, end="", flush=True)
        time.sleep(delay)
    print()
  
def si(text, delay=0.02) :
    for char in str(text) :
        print(char, end="", flush=True)
        time.sleep(delay)
    return input()

#Cleaner
os.system('clear')

#Names Inputer 
UserInput = si(Fore.GREEN + "Hello Boss What Your Names? : ")
PassWordInput = si(Fore.GREEN + "Enter Your PassWord! : ")

#Random
Port = random.randint(1024, 2048)
UserLine = random.randint(1, 1000000000)

#Welcome Sender
sp(Fore.BLUE + f"Welcome {UserInput} To Hack Family")
time.sleep(3)

#Starter Engine
os.system('clear')
sp(Fore.GREEN + f"[System] User:{UserInput} Password:{PassWordInput}")
sp(Fore.GREEN + "")
sp(Fore.GREEN + "[System] User Logined To http://BanBan445M.dev <== Is Secret ")
sp(Fore.GREEN + "")
sp(Fore.GREEN + f"[System] User Port {Port} User Line {UserLine}")
sp(Fore.GREEN + "")
time.sleep(3)
os.system('clear')
sp('Loading...')
time.sleep(1)
os.system('clear')
sp('Loading..')
time.sleep(1)
os.system('clear')
sp('Loading.')
time.sleep(1)
os.system('clear')
sp('Loading...')
time.sleep(1)
os.system('clear')
sp('Loading..')
time.sleep(1)
os.system('clear')
sp('Loading.')
time.sleep(1)
os.system('cls')
os.system('clear')

#MainMenu
sp(Fore.RED + r"""
╔══════════════════════════════════════╗
║                                      ║
║   ██   ██  ██  ██       ██           ║
║   ██  ██   ██  ██       ██           ║
║   █████    ██  ██       ██           ║
║   ██  ██   ██  ██       ██           ║
║   ██   ██  ██  ███████  ███████      ║
║                                      ║
║              ⚡ KILL ⚡              ║
║                                      ║
╚══════════════════════════════════════╝
""")
sp('╔══════════════════════════════════════╗')
sp('╚══════════════════════════════════════╝')
sp(Fore.GREEN + "1.Virus Crafter")
sp(Fore.GREEN + "2.SMS Bomber")
sp(Fore.GREEN + "3.App Attacker")
sp(Fore.GREEN + "4.IP Tracker")
sp(Fore.GREEN + "5.Birds")
sp(Fore.GREEN + "6.Enity-KoJ AI")
sp(Fore.GREEN + "7.Enity App Killer")
sp(Fore.GREEN + "8.Fake Hack")
sp(Fore.GREEN + "9.Subscribe GitHub")
sp(Fore.RED + "10.Exit")
sp('╔══════════════════════════════════════╗')
sp('╚══════════════════════════════════════╝')
User = si(Fore.YELLOW + "ẞelect Ñumbers : ")
os.system('cls')
os.system('clear')

#Runners
if User == "1":
    os.system('bash TigerVirus.sh')
  
elif User == "2":
    os.system('python Tools/SmsBomber/SmsBomber.py')
  
elif User == "3":
    os.system('bash Tools/zphisher/zphisher.sh')
  
elif User == "4":
    os.system('python Tools/GhostTrack/GhostTR.py')
  
elif User == "5":
    os.system('python Tools/Birds/main.py')
  
elif User == "6":
    os.system('python Tools/Enity-KoJ/app.py')
  
elif User == "7":
    os.system('bash Tools/Enity/Enity.sh')
  
elif User == "8":
    os.system('python Fake/Fake.py')
  
elif User == "9":
    os.system('python Sub/Sub.py')
  
elif User == "10":
    os.system('python Exit/Exit.py')

else:
  sp('Hey What???')
  sys.exit()
