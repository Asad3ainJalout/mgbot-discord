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
from lxml import html

logging.basicConfig(level=logging.ERROR)

client = discord.Client()

# Read in the Secret to login
exec(open('secret.txt').read())

# Code block for the Urban command
async def urban(request):
    page = requests.get("https://www.urbandictionary.com/define.php", params={'term':request})
    tree = html.fromstring(page.content)
    data = tree.xpath('//*[@id="content"]/div[1]/div[3]/child::node()')
    print(data.tostring(et, encoding='utf8', method='xml'))
    return data
    
# Code block for the Quran command
async def quran(command,request):
    data = []
    if command == 'info':
        obj = requests.get("http://staging.quran.com:3000/api/v3/chapters/%s" % (request)).json()['chapter']
        data.append(obj['name_arabic'])
        data.append(obj['name_simple'])
        data.append(requests.get("http://staging.quran.com:3000/api/v3/chapters/%s/info" % (request)).json()['chapter_info']['short_text'])
        data.append(obj['revelation_order'])
        data.append(obj['revelation_place'])
        data.append(obj['verses_count'])
        data.append(obj['translated_name']['name'])
        return data
    elif command == 'verse':
        request = request.split(":")
        sura = int(request[0])
        verse = int(request[1])
        obj = requests.get("http://staging.quran.com:3000/api/v3/chapters/%s/verses?recitation=1&translations=21&language=en&text_type=words" % (sura)).json()['verses'][verse-1]
        data.append(obj['text_madani'])
        data.append(obj['translations'][0]['text'])
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
    if message.content.startswith("You can't tell MuslimGamer-bot what to do, this is America man"):
        await client.send_message(message.channel,'Exactly, I do what I want.')
        await client.send_message(message.channel,'http://shirtminion.com/wp-content/uploads/2015/06/Im-Sorry-I-Thought-This-Was-America-South-Park-1.jpg')
    if message.author.id == ('218150923829116929'):
        await client.add_reaction(message,'💩')
    if message.author.id == ('192360529426120704'):
        await client.add_reaction(message,'💩')
    if message.content.startswith('$urban'):
        content = message.content.split(" ")
        data = await urban(content[1])
        await client.send_message(message.channel,"```%s```" % (data))
    elif message.content.startswith('$quran'):
        content = message.content.split(" ")
        data = await quran(content[1],content[2])
        if content[1] == 'info':
            await client.send_message(message.channel,"```%s\t\t\t%s\t\t\tVerses: %s\n%s\t\t\t%s\t\t\tRevelation Order: %s\n\n%s```" % (data[1],data[0],data[5],data[4],data[6],data[3],data[2]))
        elif content[1] == 'verse':
            await client.send_message(message.channel,"```%s\n%s```" % (data[0],data[1]))
        else:
            await client.send_message(message.author,"\n_**Main Commands**_\n\t$quran\n_**$quran Commands**_\n\tinfo (surah number)")
    elif message.content.startswith('$help'):
        await client.send_message(message.author,"```Main Commands\n--------------------\n\t$help\n\t$quran\n\t\tinfo 1\n\t\tverse 1:1```")
    
client.run(token)
