import discord
import random
import re
import asyncio
import pyowm
import datetime
import time
import requests
import json

from discord.ext import commands
from info import options

description = "JonnyBot - Irritation and game night"
bot_prefix = "~"

client = commands.Bot(description=description, command_prefix=bot_prefix)

a = False
aly = ["Go scotts!", "I LOVE CATS THEYRE SO CUTE@@@@@@@@", "YOURE KILLING POLAR BEARS", "JUPITER DOESN'T HAVE FEELINGS","Tr#@!%","KILL YOURSELFFFFFFFFFFF","Water your plant!","RUDEEEE!","😂😂😂 lol!","GO DIE IN A HOLE!!!!","FIGHT ME","Yus!","GDP","FKENWO-","FNEKDKS","TBEICNE","YOU WRETCHED BAFFONS!!!!","Rhanks!","ASDLKFJASLDFA","ASFJAALSKDFJ","ASDFLKJASDF","ASDFAGSZSEF","KILL YOUR ELF",
"ASJDKFASDFKLJASDFAWERFAESFSRFSFCXSCVZSCRVCSCVCZ", "VERLYSSA ISN'T REAL@@@@@@@@", "I HATE YOU@@@@@@", "YOU GITA SUCK@@@@@", "NOOOOOK", "HEYYYYYY","GALEXXXXXXXXXXXXX","ALEX ONLY HAS FEELINGS FOR GABBYYYYYYYY@@@@@@@@@@@@","FKANFBWOX","NOOOOOOOOOOO!!!!!!!!","*rolls eyes*"]

jo = ["Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lo\n*l","Lpl\n*Lol","Lpl\n*Lpl\n**Lol",  "WE MUST SEIZE THE MEANS OF SOCIAL GRATIFICATION"]

kw = ["Annoying and unoriginal","Good question","#discordmasterrace"]

al = ["K","Wau","K then"]

ow = ["Ok","Y","Galex is real"]

jny = ["aysat","AND HIS NAME IS JOHN CENA!!!","Are you sure about that?","Bruh","I like trains"]

cous = open("C:\\Users\\Jonny\\Documents\\GitHub\\JonnyBot\\aysatbot\\countries.txt","r",encoding='utf8')
coulist = cous.readlines()
cous.close()

cc = {"abbreviation":"country name"}
for line in coulist:
    x = line.index(":")
    cc[line[0:x]] = line[x+1:]

mem = []

@client.event
async def on_ready():
    global mem
    print("------")
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print(discord.__version__)
    print("------")
    #print(client.servers)
    """for serv in client.servers:
        for em in serv.emojis:
            print(em.id)"""

@client.command(pass_context=True,description="Simulates Alyssa's speech patterns with 100% accuracy",categories="test")
async def alyssa(ctx):
    for i in range(0,3):
        rand = random.choice(aly)
        await client.say(rand)

@client.command(pass_context=True,description="Simulates Joe's speech patterns with 100% accuracy")
async def joe(ctx):
    rand = random.choice(jo)
    await client.say(rand)

@client.command(pass_context=True,description="Simulates Kevin W's speech patterns with 100% accuracy")
async def kevw(ctx):
    rand = random.choice(kw)
    await client.say(rand)

@client.command(pass_context=True,description="Simulates Alex's speech patterns with 100% accuracy")
async def alex(ctx):
    rand = random.choice(al)
    await client.say(rand)

@client.command(pass_context=True,description="Simulates Owen's speech patterns with 100% accuracy")
async def owen(ctx):
    rand = random.choice(ow)
    await client.say(rand)

@client.command(pass_context=True,description="Simulates Jonny's speech patterns with 100% accuracy")
async def jon(ctx):
    rand = random.choice(jny)
    await client.say(rand)

@client.command(pass_context=True,description="Toggles 'Are you sure about that' spam; only works in '#nsfw-spam'")
async def aysat(ctx):
    if ctx.message.channel.name == "nsfw-spam":
        global a
        a = not a
        if a == True:
            await client.say("[aysat: ON]")
        else:
            await client.say("[aysat: OFF]")

story = {'id': ["list"]}
game = {'id': "True/False"}
turns = {'id': ["players"]}
last = {'id':"player"}
impord = {"id":"True/False"}

@client.command(pass_context=True,description="For Improv games:\n\nstart: starts Improv game\nstop: ends Improv game\nresume: resumes the Improv game\ndelete: deletes last entry\nstory: prints the Improv story")
async def improv(ctx, option: str):
    global story, game, impord, turns
    s = ctx.message.server.id
    if s not in impord:
        impord[s] = False
    if s not in turns:
        turns[s] = ["None"]
    if s not in story:
        story[s] = []
        game[s] = False
    if option == "start":
        if not game[s]:
            game[s] = True
            story[s] = []
            await client.say("Improv beginning now!")
        else:
            await client.say("Improv game already in progress!")
    elif option == "stop":
        if game[s]:
            game[s] = False
            para = ""
            await client.say("Finishing...")
            for i in story[s]:
                if i[0:3] == "++.":
                    j = i[3:]
                else:
                    j = i[1:]
                if j[0] == " ":
                    j = j[1:]
                if j[0] in [".",",","!","?",'"',"'","/"]:
                    para += j
                elif j[0] == " ":
                    para += j[1:]
                else:
                    para += " " + j
            await client.say(para)
        else:
            await client.say("Improv game not detected.")
    elif option == "story":
        para = ""
        for i in story[s]:
            if i[0:3] == "++.":
                j = i[3:]
            else:
                j = i[1:]
            if j[0] == " ":
                j = j[1:]
            if j[0] in [".",",","!","?",'"',"'","/"]:
                para += j
            elif j[0] == " ":
                para += j[1:]
            else:
                para += " " + j
        await client.say(para)
    elif option == "delete":
        if game[s]:
            await client.say('Deleting "%s"...' % story[s][-1][1:])
            story[s] = story[s][:-1]
        else:
            await client.say("Improv game not in progress.")
    elif option == "resume":
        if not game[s]:
            game[s] = True
            await client.say("Improv resuming now!")
        else:
            await client.say("Improv game already in progress!")
    elif option == "order":
        if game[s]:
            if s in turns:
                impord[s] = not impord[s]
                if impord[s]:
                    await client.say("Enabled turn order.")
                else:
                    await client.say("Disabled turn order.")
            else:
                await client.say("Order not set yet. (type ~order player1 player2 ... to set order)")
        else:
            await client.say("Improv game not in progress.")
    elif option == "turn":
        try:
            if game[s] and impord[s]:
                o = []
                ppl = ""
                for i in turns[s]:
                    o.append(ctx.message.server.get_member(i))
                for x in o:
                    if turns[s].index(x.id)-1 >= 0:
                        if last[s] == turns[s][turns[s].index(x.id)-1]:
                            ppl = ppl + ', {0.mention}'.format(x)
                        else:
                                ppl = ppl + ', {0.display_name}'.format(x)
                    else:
                        if last[s] == turns[s][-1]:
                            ppl = ppl + ', {0.mention}'.format(x)
                        else:
                                ppl = ppl + ', {0.display_name}'.format(x)
                ppl = ppl[2:]
                await client.say(ppl)
            elif not impord[s]:
                await client.say("Turn order not enabled (type ~improv order to enable)")
            else:
                await client.say("Improv game not in progress")
        except AttributeError:
            await client.say("Order not set yet. (type ~order player1 player2 ... to set order)")
    else:
        await client.say("Unknown Improv command.")

@client.command(pass_context=True,description="Set turn order for games")
async def order(ctx, *players):
    try:
        global turns, last
        s = ctx.message.server.id
        turns[s] = []
        for i in players:
            if ctx.message.server.get_member(i.replace("!","")[2:-1]) != None:
                turns[s].append(i.replace("!","")[2:-1])
            elif ctx.message.server.get_member_named(i) != None:
                turns[s].append(ctx.message.server.get_member_named(i).id)
            else:
                turns[s] = []
                await client.say('Could not find member named "{}"'.format(i))
                return
        last[s] = turns[s][-1]
        await client.say("Order set!")
    except IndexError:
        await client.say("Player list not given.")

@client.command(pass_context=True,description="Who do you really like?")
async def who(ctx):
    await client.say("Who do you really like? Not a sarcastic answer, but actually. By the way, last time, it was a sarcastic answer. Celebrity crushes don't count.")

@client.command(pass_context=True,description="Weather forecast")
async def weather(ctx, city: str, ctry="", temp_mode="f"):
    try:
        owm = pyowm.OWM(options.owm())
        try:
            if len(ctry) > 0:
                observation = owm.weather_at_place(city + "," + ctry)
            else:
                observation = owm.weather_at_place(city)
        except:
            await client.say("City not found.")
            return
        w = observation.get_weather()
        fore = w.get_status()
        if fore == "Clouds":
            fe = ":cloud:"
        elif fore == "Clear":
            fe = ":sunny:"
        elif fore == "Rain":
            fe = ":cloud_rain:"
        elif fore == "Snow":
            fe = ":cloud_snow:"
        elif fore == "Thunderstorm":
            fe = ":thunder_cloud_rain:"
        elif fore == "Haze":
            fe = "<:haze:336952276524466179>"
        elif fore == "Mist":
            fe = "<:mist:336948218141343744>"
        else:
            fe = fore
        if temp_mode.lower() == "c":
            t = str(w.get_temperature('celsius')['temp']) + "°C"
            hi = str(w.get_temperature('celsius')['temp_max']) + "°C"
            lo = str(w.get_temperature('celsius')['temp_min']) + "°C"
        elif temp_mode.lower() == "k":
            t = str(w.get_temperature()['temp']) + "°K"
            hi = str(w.get_temperature()['temp_max']) + "°K"
            lo = str(w.get_temperature()['temp_min']) + "°K"
        else:
            t = str(w.get_temperature('fahrenheit')['temp']) + "°F"
            hi = str(w.get_temperature('fahrenheit')['temp_max']) + "°F"
            lo = str(w.get_temperature('fahrenheit')['temp_min']) + "°F"
        l = str(observation.get_location())
        loc = l[l.index('name=')+5:l.index(', lon')]
        c = cc[observation.get_location().get_country()]
        loc = loc + ", " + c
        text = "%s\n    %s %s\n\n    High: %s, Low: %s\n\n    " % (loc,fe,t,hi,lo)
        await client.say(text)
    except:
        await client.say("Unexpected error")

@client.command(pass_context=True,description="Local time finder")
async def loctime(ctx, city: str, ctry=""):
    if city.lower() == "utc" or city.lower() == "gmt":
        utc = str(datetime.datetime.utcnow())
        await client.say(("UTC / GMT\n\n    {}\n    {}/{}/{}").format(utc[11:19],utc[5:7],utc[8:10],utc[0:4]))
    else:
        owm = pyowm.OWM(options.owm())
        try:
            if len(ctry) > 0:
                observation = owm.weather_at_place(city + "," + ctry)
            else:
                observation = owm.weather_at_place(city)
        except:
            await client.say("City not found.")
            return
        la = observation.get_location().get_lat()
        lo = observation.get_location().get_lon()
        latlon = str(la) + ', ' + str(lo)
        timestamp = time.time()
        apikey = options.tz()
        apicall = 'https://maps.googleapis.com/maps/api/timezone/json?location=' + latlon + '&timestamp=' + str(timestamp) + '&key=' + apikey
        r = requests.get(apicall)
        resp = json.loads(r.text)
        lt = timestamp + resp["dstOffset"] + resp["rawOffset"]
        t = time.localtime(lt)
        hr = t.tm_hour + 7
        minu = t.tm_min
        sec = t.tm_sec
        day = t.tm_mday
        mon = t.tm_mon
        year = t.tm_year
        m = "AM"
        if hr > 11:
            m = "PM"
        if hr > 12 and hr <= 24:
            hr -= 12
        elif hr >= 24:
            day += 1
            m = "AM"
            hr -= 24
            if hr > 11:
                m = "PM"
            if hr > 12:
                hr -= 12
            if day == 32:
                day = 1
                mon += 1
                if mon == 13:
                    mon = 1
                    year += 1
            elif day == 31 and mon in [4,6,9,11]:
                day = 1
                mon += 1
            elif mon == 2 and day == 30 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
                day = 1
                mon += 1
            elif mon == 2 and day == 29 and not (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
                day = 1
                mom = mon + 1
        if hr < 10:
            hr = "0" + str(hr)
        if minu < 10:
            minu = "0" + str(minu)
        if sec < 10:
            sec = "0" + str(sec)

        l = str(observation.get_location())
        loc = l[l.index('name=')+5:l.index(', lon')]
        c = cc[observation.get_location().get_country()]
        loc = loc + ", " + c

        await client.say(("{}\n    {}:{}:{} {}\n    {}/{}/{}\n    {}").format(loc,hr,minu,sec,m,mon,day,year,resp["timeZoneName"]))

@client.event
async def on_message(message):
    global story, game, last
    if message.author.id != client.user.id and message.author.id != "325108081241489408":
        if message.author.id != message.server.me.id and message.content[0] not in [bot_prefix,"!"] and a == 1 and "?" not in message.content and message.channel.name=="nsfw-spam":
            await client.send_message(message.channel, '{0.author.mention}, are you sure about that?'.format(message))
        """if "game night" in message.content.lower() and message.channel.name == "game-night":
            gn = message.server.roles
            for i in gn:
                if i.name == "game-night":
                    await client.send_message(message.channel, "{0.mention}".format(i))"""
        if message.author.id != message.server.me.id and message.content[0] not in [bot_prefix,"!"] and "?" not in message.content and len(message.content) > 4 and " " in message.content:
            if random.randint(1,100) == 1:
                await client.send_message(message.channel, '{0.author.mention}, are you sure about that?'.format(message))
        if "im" in message.content.lower().replace("'","") or "i am" in message.content.lower():
            if message.content.lower()[0:4] == "i'm ":
                await client.send_message(message.channel, "Hi, " + message.content[4:])
            elif message.content.lower()[0:3] == "im ":
                await client.send_message(message.channel, "Hi, " + message.content[3:])
            elif message.content.lower()[0:5] == "i am ":
                await client.send_message(message.channel, "Hi, " + message.content[5:])
            else:
                x = re.sub(r'[^a-zA-Z0-9\s]', '', message.content.lower())
                if " im " in x:
                    await client.send_message(message.channel,"Hi, " + x[x.index(" im ")+4:])
                elif " i am " in  x:
                    await client.send_message(message.channel,"Hi, " + x[x.index(" i am ")+6:])
        if message.server.id not in story:
            story[message.server.id] = []
            game[message.server.id] = False
        if game[message.server.id] == True:
            if message.content[0] == "." and message.content[1] != ".":
                if impord[message.server.id] == True:
                    if turns[message.server.id].index(message.author.id)-1 >= 0:
                        if last[message.server.id] == turns[message.server.id][turns[message.server.id].index(message.author.id)-1]:
                            story[message.server.id].append(message.content)
                            last[message.server.id] = message.author.id
                            await client.add_reaction(message,"✅")
                        else:
                            await client.send_message(message.channel, "{0.author.mention}, it's not your turn!".format(message))
                    else:
                        if last[message.server.id] == turns[message.server.id][-1]:
                            story[message.server.id].append(message.content)
                            last[message.server.id] = message.author.id
                            await client.add_reaction(message,"✅")
                        else:
                            await client.send_message(message.channel, "{0.author.mention}, it's not your turn!".format(message))
                else:
                    story[message.server.id].append(message.content)
                    await client.add_reaction(message,"✅")
            if message.content[0:3] == "++.":
                story[message.server.id].append(message.content)
                await client.add_reaction(message,"✅")
        if "somebody" in message.content.lower() or "someone" in message.content.lower():
            await client.send_message(message.channel,"AND HIS NAME IS JOHN CENA!!!!!!!!!!!!!")
    await client.process_commands(message)

client.run(options.token())
