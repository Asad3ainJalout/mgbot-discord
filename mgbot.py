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
import emoji
import logging
import requests
from lxml import html

logging.basicConfig(level=logging.ERROR)

client = discord.Client()

# Settings
prefix = '$'

# Read in the Secret to login
exec(open('secret.txt').read())

# Help Code dictionary
help = {'mgbot' : '**Main**\n   **' + prefix + 'help** prints out this help. Type ' + prefix + 'help <command> to get more information about a specific command.\n   **' + prefix + 'cone** cones or uncones the shamed (only used by shura)',
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
        if command[1:] == 'help':
            splitMessage.append('mgbot')
            await client.send_message(message.author, help.get(splitMessage[1], help['mgbot']))

client.run(token)
