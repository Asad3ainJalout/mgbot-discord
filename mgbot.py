#!/usr/bin/python
#
# The Muslim Gamer Bot
# This bot is designd to cater to the muslim gamer communities needs.
#
# Designed and Programmed by Asad3ainJalout
#
# Covered by the GNU General Public License

import asyncio
import argparse
import discord
import logging
import requests
import sqlite3 as lite
import time
from lxml import html
from pytimeparse import parse

logging.basicConfig(level=logging.ERROR)

client = discord.Client()

# Settings 
prefix = '$' 

# Read in the Secret to login
exec(open('secret.txt').read())

# sqlite database initilization
con = None
con = lite.connect('mgbot.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Cone(userID INT PRIMARYKEY)")

# Help Code dictionary
help = {
    'mgbot' : '**Main**\n   **' + prefix + 'help** prints out this help. Type ' + prefix + 'help <command> to get more information about a specific command.\n   **' + prefix + 'cone** cones or uncones the shamed (only used by shura)',
    'help' : '**' + prefix + 'help**\nType ' + prefix + 'help <command> for information about a specific command.\nFor example:\n ' + prefix + 'help cone',
       }

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith(prefix):
        splitMessage = message.content.split(" ")
        command = splitMessage[0]
        #Basic help call, make sure to edit the help dictionary for any new entries.
        if command[1:] == 'help':
            splitMessage.append('mgbot')
            await client.send_message(message.author, help.get(splitMessage[1], help['mgbot']))
        #Cone function, we determine what variables are given before calling the cone_argsparse function
        elif command[1:] == 'cone':
            for victim in message.mentions:
                cur.execute("INSERT INTO Cone(userID) VALUES(?)", (victim.id,))
        elif command[1:] == 'uncone':
            for victim in message.mentions:
                cur.execute("DELETE FROM Cone WHERE userID = ?", (victim.id,))
    for victim in cur.execute("SELECT userID FROM Cone WHERE userID = ?", (message.author.id,)):
        await client.add_reaction(message,'💩') # poop
        await client.add_reaction(message,'🇸') # S
        await client.add_reaction(message,'🇭') # H
        await client.add_reaction(message,'🇦') # A
        await client.add_reaction(message,'🇲') # M
        await client.add_reaction(message,'🇪') # E
    else:
        pass

client.run(token)
