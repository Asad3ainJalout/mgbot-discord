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
cur.execute("CREATE TABLE IF NOT EXISTS Cone(userID TEXT PRIMARYKEY)")

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
                cur.execute("INSERT INTO Cone (victim)")
        elif command[1:] == 'uncone':
            for victem in message.mentions:
                cur.execute("DELETE FROME Cone WHERE userID = ?", victim)
    elif cur.execute("SELECT EXISTS(SELECT 1 FROM Cone WHERE userID=? LIMIT 1)", (message.author.id,)):
        await client.send_message(message.channel, "coned")

client.run(token)
