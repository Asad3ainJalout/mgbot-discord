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
from pytimeparse import parse
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
cur.execute("CREATE TABLE IF NOT EXISTS Cone(userID INT PRIMARYKEY, coneStatus INT, coneStart INT, coneExpire INT, coneReason TEXT, conedTimes INT, coner TEXT)")

# Cone code block
async def cone_argsparse(string):
    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    parser.add_argument('victims', nargs='+')
    parser.add_argument('-r', nargs='+')
    parser.add_argument('-t')
    return parser.parse_args(string)

async def cone(userID,command,coneStart,coneDuration,coneReason,coner, channel):
    if command == 'set' and (message.author.top_role.id == '287369489987928075' or message.author.top_role.id == '193105896010809344' or message.author.top_role.id == '192322577207787523'):
        pass
    if command == 'unset' and (message.author.top_role.id == '287369489987928075' or message.author.top_role.id == '193105896010809344' or message.author.top_role.id == '192322577207787523'):
        pass
    if command == 'info':
        if cur.fetchone():
            await client.send_message(channel, cur.execute("SELECT coneStart, coneExpire, coneReason, conedTimes, coner FROM Cone WHERE userID = '%s'" % userID))
        else:
            await client.send_message(channel,'This user has never been coned')
    return

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
            args = await cone_argsparse(splitMessage[1:])
            
            #checking if the variables defined or not
            try:
                args.t
            except:
                args.t = '2000y'
            try:
                args.r
            except:
                args.r = 'You have been coned for reasons unknown.'
            
            for victim in args.victims:
                await cone(victim[1:],args.command,message.timestamp,parse(args.t),args.r,message.author.name.id,message.channel)

client.run(token)
