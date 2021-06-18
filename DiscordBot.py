from discordwebhook import Discord
from discord_webhook import DiscordWebhook
import time
import os
import colorama
from colorama import *

colorama.init()


def bot():
    ilosc = int(input("The number of messages: "))
    czas = int(input("Time the message was sent: "))
    Nazwabota = str(input("Name Bot: "))
    textbota = str(input("Text Bot: "))
    link = str(input("Webchock link: "))
    link_avatar = str(input("link Avatar : "))
    for x in range(ilosc):
        time.sleep(czas)
        discord = Discord(url=link)
        discord.post(
            content = textbota,
            username = Nazwabota,
            avatar_url= link_avatar,
        )

wyjscie = False
while wyjscie ==False:
    print('\033[35m' +'#### Menu ####')
    print('\033[31m' + "1. BOT Zwykły:")
    print('\033[39m' + "##############")

    choice = input("Wybierz Opcjie (1):")

    if choice == '1':
     bot()
     os.system('cls')
     
 
if choice <1:
    print("Zła opcjia")
    
if choice >1:
    print("Zła opcjia")



