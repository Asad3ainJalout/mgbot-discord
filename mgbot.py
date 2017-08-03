#!/usr/bin/python
#
# The Muslim Gamer Bot
# This bot is designd to cater to the muslim gamer communities needs.
#
# Designed and Programmed by Asad3ainJalout
#
# Covered by the GNU General Public License

import asyncio
import discord
import logging
import requests
import sqlite3 as lite
from lxml import html

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
cur.execute("CREATE TABLE IF NOT EXISTS Cone(id INT PRIMARY KEY, userID INT UNIQUE, coneStatus INT, coneStart INT, coneExpire INT, coneReason TEXT, conedTimes INT)")

# Cone code block
async def cone(author,topRole,command,target,reason,time):
    print('testing')

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
        #Cone function, we determine what variables are given before calling the cone function
        elif command[1:] == 'cone':

            await cone(message.author.id, message.author.top_role.id, something, message.mentions, reason, time)
    # Heart emoji reaction to mew at the request of bloodmoney
    elif message.author.id == '229345661454123008':
        await client.add_reaction(message,'♥')

client.run(token)
