#!/usr/bin/python
#
# The Muslim Gamer Bot
# This bot is designd to cater to the muslim gamer communities needs.
#
# Designed and Programmed by Asad3ainJalout
#
# Covered by the GNU General Public License

import discord
import asyncio
import json
import urllib.request
import logging

logging.basicConfig(level=logging.ERROR)

client = discord.Client()

# Read in the Secret to login
exec(open('secret.txt').read())

# Code block for the Quran command
async def quran(command,request):
    data = []
    if command == 'info':
        obj = json.loads(urllib.request.urlopen("http://staging.quran.com:3000/api/v3/chapters/%s" % (request)).read())['chapter']
        data.append(obj['name_arabic'])
        data.append(obj['name_simple'])
        data.append(json.loads(urllib.request.urlopen("http://staging.quran.com:3000/api/v3/chapters/%s/info" % (request)).read())['chapter_info']['short_text'])
        data.append(obj['revelation_order'])
        data.append(obj['revelation_place'])
        data.append(obj['verses_count'])
        data.append(obj['translated_name']['name'])
        return data
    elif command == 'verse':
        request = request.split(":")
        sura = request[0]
        verse = int(request[1])
        obj = json.loads(urllib.request.urlopen("http://staging.quran.com:3000/api/v3/chapters/%s/verses?recitation=1&translations=21&language=en&text_type=words" % (sura)).read())['verses'][verse-1]
        data.append(obj['text_madani'])
        data.append(obj['translations'][verse-1]['text'])
        return data

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('C-C-C-C-C-C-CONVO KILLER #WindowsMasterRace'):
        await client.send_message(message.channel,' s/Windows/Linux/')
    elif message.content.startswith('$quran'):
        content = message.content.split(" ")
        data = await quran(content[1],content[2])
        if content[1] == 'info':
            await client.send_message(message.channel,"```%s\t\t\t%s\t\t\tVerses: %s\n%s\t\t\t%s\t\t\tRevelation Order: %s\n\n%s```" % (data[1],data[0],data[3],data[4],data[6],data[5],data[2]))
        elif content[1] == 'verse':
            await client.send_message(message.channel,"```%s\n%s```" % (data[0],data[1]))
        else:
            await client.send_message(message.author,"\n_**Main Commands**_\n\t$quran\n_**$quran Commands**_\n\tinfo (surah number)")
    elif message.content.startswith('$help'):
        await client.send_message(message.author,"```Main Commands\n--------------------\n\t$help\n\t$quran\n\t\tinfo 1\n\t\tverse 1:1```")
    
client.run(token)
