import os
import sys
from discord_webhook import DiscordWebhook, DiscordEmbed
from colorama import init
init()
from colorama import Fore
from tqdm import tqdm
import time
from time import sleep
 

os.system("title injector webhook spammer")
y = Fore.YELLOW
w = Fore.WHITE

def clear():
    os.system("cls")

title = f"""
            ██╗███╗   ██╗     ██╗███████╗ ██████╗████████╗ ██████╗ ██████╗ 
            ██║████╗  ██║     ██║██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
            ██║██╔██╗ ██║     ██║█████╗  ██║        ██║   ██║   ██║██████╔╝
            ██║██║╚██╗██║██   ██║██╔══╝  ██║        ██║   ██║   ██║██╔══██╗
            ██║██║ ╚████║╚█████╔╝███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║
            ╚═╝╚═╝  ╚═══╝ ╚════╝ ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                               """


clear()
print(title)
print("""
                        Discord Webhook Spammer - v1.0
                                              
""")

webh = input(w + "[" + y + "+" + w + "] Webhook: ")
amt = input(w + "[" + y + "+" + w + "] Amount: ")
msg = input(w + "[" + y + "+" + w + "] Message: ")
input(f"{w}Press {y}ENTER{w} to start spamming: ")
clear()
print(title)
for i in tqdm(range(int(amt)), desc ="Spamming"):
    webhook = DiscordWebhook(url=webh, content=msg)
    response = webhook.execute()
time.sleep(2)
print("finished")
input()
