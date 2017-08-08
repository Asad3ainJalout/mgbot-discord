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
import sqlite3 as lite

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
        #Cone function, we determine what variables are given before calling the cone_argsparse function
        if command[1:] == 'cone' and (message.author.top_role.id == '287369489987928075' or message.author.top_role.id == '193105896010809344' or message.author.top_role.id == '192322577207787523'):
            cur.execute("SELECT EXISTS(SELECT userID FROM Cone WHERE userID=? LIMIT 1)", (message.author.id,))
            allowed = cur.fetchone()[0]
            if allowed == 0:
                for victim in message.mentions:
                    cur.execute("INSERT INTO Cone(userID) VALUES(?)", (victim.id,))
            else:
                await client.send_message(message.channel,"Nice try sucker.")
        elif command[1:] == 'uncone' and (message.author.top_role.id == '287369489987928075' or message.author.top_role.id == '193105896010809344' or message.author.top_role.id == '192322577207787523'):
            cur.execute("SELECT EXISTS(SELECT userID FROM Cone WHERE userID=? LIMIT 1)", (message.author.id,))
            allowed = cur.fetchone()[0]
            if allowed == 0:
                for victim in message.mentions:
                    cur.execute("DELETE FROM Cone WHERE userID = ?", (victim.id,))
            else:
                await client.send_message(message.channel,"Nice try sucker.")
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
