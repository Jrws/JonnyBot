import discord
import random
import re
import asyncio
import pyowm
import datetime
import time
import requests
import json
import os
import itertools

from discord.ext import commands
from info import options

description = "JonnyBot - Irritation and game night"
bot_prefix = "~"

client = commands.Bot(description=description, command_prefix=bot_prefix)

aly = ["Go scotts!", "I LOVE CATS THEYRE SO CUTE@@@@@@@@", "YOURE KILLING POLAR BEARS", "JUPITER DOESN'T HAVE FEELINGS","Tr#@!%","KILL YOURSELFFFFFFFFFFF","Water your plant!","RUDEEEE!","😂😂😂 lol!","GO DIE IN A HOLE!!!!","FIGHT ME","Yus!","GDP","FKENWO-","FNEKDKS","TBEICNE","YOU WRETCHED BAFFONS!!!!","Rhanks!","ASDLKFJASLDFA","ASFJAALSKDFJ","ASDFLKJASDF","ASDFAGSZSEF","KILL YOUR ELF",
"ASJDKFASDFKLJASDFAWERFAESFSRFSFCXSCVZSCRVCSCVCZ", "VERLYSSA ISN'T REAL@@@@@@@@", "I HATE YOU@@@@@@", "YOU GITA SUCK@@@@@", "NOOOOOK", "HEYYYYYY","GALEXXXXXXXXXXXXX","ALEX ONLY HAS FEELINGS FOR GABBYYYYYYYY@@@@@@@@@@@@","FKANFBWOX","NOOOOOOOOOOO!!!!!!!!","*rolls eyes*","*nods*","DJFALSK DFJAS","VICTORYYYY"]

jo = ["Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lo\n*l","Lpl\n*Lol","Lpl\n*Lpl\n**Lol",  "WE MUST SEIZE THE MEANS OF SOCIAL GRATIFICATION"]

kw = ["Annoying and unoriginal","Good question","#discordmasterrace","salty af"]

al = ["K","Wau","K then","Bro rip","Um"]

ow = ["Ok","Y","Galex is real","Idk","Y tho","i cri evri tiem"]

jny = ["aysat","AND HIS NAME IS JOHN CENA!!!","Are you sure about that?","Bruh","I like trains","seems legit"]

ga = ["Wau","Harsh","Wau harsh","Lol","Yup","STAHP","HAHA","*shrugs*","Oh","IM DONE","Uhh...","Yey","YAASSSSSS","DAMN"]

cous = open(os.path.join(os.path.dirname(__file__),"lists\\countries.txt"),encoding="utf8")
coulist = cous.readlines()
cous.close()

bcList = open(os.path.join(os.path.dirname(__file__),"lists\\blackcards.txt"),encoding="utf8")
blackCards = bcList.readlines()
bcList.close()
for i in range(len(blackCards)):
    blackCards[i] = blackCards[i][:-1]
wcList = open(os.path.join(os.path.dirname(__file__),"lists\\whitecards.txt"),encoding="utf8")
whiteCards = wcList.readlines()
wcList.close()
for i in range(len(whiteCards)):
    whiteCards[i] = whiteCards[i][:-1]

gmods = {'serv id':['players']}

cc = {"abbreviation":"country name"}
for line in coulist:
    x = line.index(":")
    cc[line[0:x]] = line[x+1:]

@client.event
async def on_ready():
    print("------")
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print(discord.__version__)
    print("------")

@client.command(pass_context=True,description="Simulates Alyssa's speech patterns with 100% accuracy",categories="test")
async def alyssa(ctx):
    for i in range(0,3):
        rand = random.choice(aly)
        await client.say(rand)
    await client.delete_message(ctx.message)

@client.command(pass_context=True,description="Simulates Joe's speech patterns with 100% accuracy")
async def joe(ctx):
    rand = random.choice(jo)
    await client.say(rand)
    await client.delete_message(ctx.message)

@client.command(pass_context=True,description="Simulates Kevin W's speech patterns with 100% accuracy")
async def kevw(ctx):
    rand = random.choice(kw)
    await client.say(rand)
    await client.delete_message(ctx.message)

@client.command(pass_context=True,description="Simulates Alex's speech patterns with 100% accuracy")
async def alex(ctx):
    rand = random.choice(al)
    await client.say(rand)
    await client.delete_message(ctx.message)

@client.command(pass_context=True,description="Simulates Owen's speech patterns with 100% accuracy")
async def owen(ctx):
    rand = random.choice(ow)
    await client.say(rand)
    await client.delete_message(ctx.message)

@client.command(pass_context=True,description="Simulates Jonny's speech patterns with 100% accuracy")
async def jon(ctx):
    rand = random.choice(jny)
    await client.say(rand)
    await client.delete_message(ctx.message)

@client.command(pass_context=True,description="Simulates Gabby's speech patterns with 100% accuracy")
async def gab(ctx):
    rand = random.choice(ga)
    await client.say(rand)
    await client.delete_message(ctx.message)

areya = False
@client.command(pass_context=True,description="Toggles 'Are you sure about that' spam; only works in '#nsfw-spam'")
async def aysat(ctx):
    if ctx.message.channel.name == "nsfw-spam":
        global areya
        areya = not areya
        if areya == True:
            await client.say("[aysat: ON]")
        else:
            await client.say("[aysat: OFF]")
turns = {'id': ["players"]}
last = {'id':"player"}

impstory = {'id': ["list"]}
impgame = {'id': "True/False"}
impord = {"id":"True/False"}

@client.command(pass_context=True,description="For Improv games:\n\nstart: starts Improv game\nstop: ends Improv game\nresume: resumes the Improv game\ndelete: deletes last entry\nstory: prints the Improv story")
async def improv(ctx, option: str=None):
    s = ctx.message.server.id
    if s not in impord:
        impord[s] = False
    if s not in turns:
        turns[s] = ["None"]
    if s not in impstory:
        impstory[s] = []
        impgame[s] = False
    if s not in gmods:
        gmods[s] = ['219642803943112705']
    if option not in ['restart','pause','resume','useorder'] or ctx.message.author.id in gmods[s]:
        if option == None:
            await client.say("```Commands:\n\n~improv [option]\n\n  restart - starts/restarts the game, clears story\n\n  pause - pauses game and gives current progress of story\n\n  resume - resumes game without clearing story\n\n  story - gives current story progressn\n\n  delete - deletes last entry in story\n\n  useorder - toggles the use of turn order\n\n  turn - if order is enabled: gives the order and mentions whose turn it currently is\n\n  order - same as turn```")
        elif option.lower() == "restart":
            if not impgame[s]:
                impgame[s] = True
                impstory[s] = []
                await client.say("Improv beginning now!")
            else:
                await client.say("Cannot restart when game is already in progress!")
        elif option.lower() == "pause":
            if impgame[s]:
                impgame[s] = False
                para = ""
                await client.say("Finishing...")
                for i in impstory[s]:
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
        elif option.lower() == "story":
            para = ""
            for i in impstory[s]:
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
        elif option.lower() == "delete":
            if impgame[s]:
                await client.say('Deleting "%s"...' % impstory[s][-1][1:])
                impstory[s] = impstory[s][:-1]
            else:
                await client.say("Improv game not in progress.")
        elif option.lower() == "resume":
            if not impgame[s]:
                impgame[s] = True
                await client.say("Improv resuming now!")
            else:
                await client.say("Improv game already in progress!")
        elif option.lower() == "useorder":
            if impgame[s]:
                if s in turns:
                    impord[s] = not impord[s]
                    if impord[s]:
                        await client.say("Enabled turn order.")
                    else:
                        await client.say("Disabled turn order.")
                else:
                    await client.say("Order not set yet. (type `~order player1 player2 ...` to set order)")
            else:
                await client.say("Improv impgame not in progress.")
        elif option.lower() in ["turn","order"]:
            try:
                if impgame[s] and impord[s]:
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
                    await client.say("Turn order not enabled (type `~improv order` to enable)")
                else:
                    await client.say("Improv game not in progress")
            except AttributeError:
                await client.say("Order not set yet. (type `~order` player1 player2 ... to set order)")
        else:
            await client.say("Unknown Improv command.")
    else:
        await client.say("You don't have permission to use that command!")

@client.command(pass_context=True,description="Set turn order for games")
async def order(ctx, *players):
    s = ctx.message.server.id
    if s not in gmods:
        gmods[s] = ['219642803943112705']
    if ctx.message.author.id in gmods[s]:
        if len(players) != 0:
            turns[s] = []
            for i in players:
                if ctx.message.server.get_member(i.replace("!","")[2:-1]) != None:
                    if str(ctx.message.server.get_member(i.replace("!","")[2:-1]).status) == "online":
                        turns[s].append(i.replace("!","")[2:-1])
                    else:
                        turns[s] = []
                        await client.say("{} is unavailable!".format(i))
                        return
                elif ctx.message.server.get_member_named(i) != None:
                    if str(ctx.message.server.get_member_named(i).status) == "online":
                        turns[s].append(ctx.message.server.get_member_named(i).id)
                    else:
                        turns[s] = []
                        await client.say("{0.mention} is unavailable!".format(ctx.message.server.get_member_named(i)))
                        return
                else:
                    turns[s] = []
                    await client.say('Could not find member named "{}"'.format(i))
                    return
            last[s] = turns[s][-1]
            await client.say("Order set!")
        else:
            if s not in turns:
                await client.say("Order not set yet.")
            elif turns[s] == []:
                await client.say("Order is blank.")
            else:
                ppl = ""
                o = []
                for i in turns[s]:
                    o.append(ctx.message.server.get_member(i))
                for x in o:
                    ppl += ", {0.mention}".format(x)
                ppl = ppl[2:]
                await client.say(ppl)
    else:
        await client.say("You don't have permission to use that command!")

@client.command(pass_context=True,description="Kicks someone from a game")
async def gamekick(ctx, player: str=None):
    s = ctx.message.server.id
    if ctx.message.author.id in gmods[s]:
        if s not in turns:
            turns[s] = []
        try:
            if ctx.message.server.get_member_named(player).id in turns[s] or player.replace("!","")[2:-1] in turns[s]:
                if ctx.message.server.get_member(player.replace("!","")[2:-1]) != None:
                    i = turns[s].index(ctx.message.server.get_member(player.replace("!","")[2:-1]))
                elif ctx.message.server.get_member_named(player) != None:
                    i = turns[s].index(ctx.message.server.get_member_named(player).id)
                await client.say("Successfully kicked {0.mention} from the game!".format(ctx.message.server.get_member(turns[s][i])))
                del turns[s][i], cahpoints[s][i], cahhands[s][i], cahresp[s][i], cahpicked[s][i]
                if cahgame[s]:
                    if cahczar[s].id not in cahplayers[s]:
                        await client.say("The round was skipped due to the Charizard leaving.")
                        cahresp[s] = [True for q in range(len(cahresp[s]))]
                        await client.say("Starting next round...")
                        if cahjoining[s] != []:
                            for person in cahjoining[s]:
                                cahplayers[s].append(person)
                                cahpoints[s].append(0)
                                cahhands[s].append([])
                                cahresp[s].append(True)
                                cahpicked[s].append([])
                                cahtimeout[s].append(True)
                            cahjoining[s] = []
                        if i < len(cahplayers[s]):
                            cahczar[s] = client.get_server(s).get_member(cahplayers[s][i])
                        else:
                            cahczar[s] = client.get_server(s).get_member(cahplayers[s][0])
                        await client.say("Charizard: {0.mention}".format(cahczar[s]))
                        cahpicked[s] = [[] for x in range(len(turns[s]))]
                        cahresults[s] = {}
                        cahchoices[s] = []
                        cahblack[s] = cahcb[s].pop()
                        await client.say("```css\n{}\n```".format(cahblack[s]))
                        cahpick[s] = cahblack[s].count("_")
                        if cahpick[s] == 0:
                            cahpick[s] = 1
                        for index in range(len(cahplayers[s])):
                            pm = client.get_server(s).get_member(cahplayers[s][index])
                            try:
                                if cahplayers[s][index] != cahczar[s].id:
                                    bcmessage = "-CAH-```css\n{}\n```\nYour cards:\n\n".format(cahblack[s])
                                    for j in range(10-len(cahhands[s][index])):
                                        cahhands[s][index].append(cahcw[s].pop())
                                    mess = ""
                                    cnt = 1
                                    for k in cahhands[s][index]:
                                        if mess == "":
                                            mess += '```{}) {}```'.format(cnt,k)
                                        else:
                                            mess += "\n" + '```{}) {}```'.format(cnt,k)
                                        cnt += 1
                                    if cahpick[s] == 1:
                                        mess = bcmessage + mess + "\nPick `" + str(cahpick[s]) + "` card!"
                                    else:
                                        mess = bcmessage + mess + "\nPick `" + str(cahpick[s]) + "` cards!"
                                    await client.send_message(pm,mess)
                                    cahresp[s][index] = False
                                else:
                                    await client.send_message(pm,"-CAH-```css\n{}\n```\nYou are the Charizard!".format(cahblack[s]))
                            except:
                                await client.say("An error occured sending a message to {0.mention}.".format(pm))
                            print(cahresp[s])
                    elif all(cahresp[s]):
                        cahresults[s] = {}
                        for x,y in zip(cahpicked[s],cahplayers[s]):
                            if x != []:
                                mess = "```"
                                for cards in x:
                                    mess += cards + "``````"
                                mess = mess[:-3]
                                cahresults[s][mess] = y
                        cahchoices[s] = list(cahresults[s].keys())
                        random.shuffle(cahchoices[s])
                        sendmain = "-Results-\n```css\n{}\n```-----\n{}".format(cahblack[s],"\n".join(cahchoices[s]))
                        for c,n in zip(cahchoices[s],range(len(cahchoices[s]))):
                            cahchoices[s][n] = "{}) {}".format(n+1,c)
                        send = "-Results-\n```css\n{}\n```-----\n{}\nPick your favorite!".format(cahblack[s],"\n".join(cahchoices[s]))
                        await client.send_message(client.get_server(s).get_channel(cahchannel[s]),sendmain)
                        try:
                            await client.send_message(cahczar[s],send)
                        except:
                            await client.say("An error occured sending a message to {0.mention}.".format(cahczar[s]))
                        cahresp[s][cahplayers[s].index(cahczar[s].id)] = False
        except:
            await client.say('Could not find member named "{}"'.format(player))
    else:
        await client.say("You don't have permission to use that command!")

@client.command(pass_context=True,description="Adds or removes moderators for games, who get to use game control commands")
async def gamemod(ctx, option: str=None, player: str=None):
    s = ctx.message.server.id
    if s not in gmods:
        gmods[s] = ['219642803943112705']
    if option not in ["add","+","remove","-",None] or ctx.message.author.id == '219642803943112705':
        if option == None:
            await client.say("```Commands:\n\n~gamemod [option] [player]\n\n  list - lists game moderators for the server\n\n  add [player] - adds someone as game moderator\n  remove [player] - removes someone as game moderator\n  + [player] - same as add\n  - [player] - same as remove```")
        elif option.lower() == "list":
            mess = "```Game moderators:\n\n"
            for i in gmods[s]:
                mess += ctx.message.server.get_member(i).display_name + "\n"
            mess = mess[:-1] + "```"
            await client.say(mess)
        elif option.lower() in ["add","+"]:
            if ctx.message.server.get_member(player.replace("!","")[2:-1]) != None:
                if ctx.message.server.get_member_named(player).id not in gmods[s]:
                    gmods[s].append(player.replace("!","")[2:-1])
                    await client.say("{} is now a game mod!".format(player))
                else:
                    client.say("{} is already a game mod!".format(player))
            elif ctx.message.server.get_member_named(player) != None:
                if ctx.message.server.get_member_named(player).id not in gmods[s]:
                    gmods[s].append(ctx.message.server.get_member_named(player).id)
                    await client.say("{0.mention} is now a game mod!".format(ctx.message.server.get_member_named(player)))
                else:
                    await client.say("{0.mention} is already a game mod!".format(ctx.message.server.get_member_named(player)))
            else:
                await client.say('Could not find member named "{}"'.format(player))
        elif option.lower() in ["remove","-"]:
            if ctx.message.server.get_member(player.replace("!","")[2:-1]) != None:
                if player.replace("!","")[2:-1] in gmods[s]:
                    gmods[s].remove(player.replace("!","")[2:-1])
                    await client.say("Removed {} as game mod!".format(player))
                else:
                    await client.say("{} is not a game mod!".format(player))
            elif ctx.message.server.get_member_named(player) != None:
                if ctx.message.server.get_member_named(player).id in gmods[s]:
                    gmods[s].remove(ctx.message.server.get_member_named(player).id)
                    await client.say("Removed {0.mention} as game mod!".format(ctx.message.server.get_member_named(player)))
                else:
                    await client.say("{0.mention} is not a game mod!".format(ctx.message.server.get_member_named(player)))
            else:
                await client.say('Could not find member named "{}"'.format(i))
        else:
            await client.say("Incorrect usage. Type `~gamemod` for subcommands.")
    else:
        await client.say("You don't have permission to use that command!")

@client.command(pass_context=True,description="Who do you really like?")
async def who(ctx):
    await client.say("Who do you really like? Not a sarcastic answer, but actually. By the way, last time, it was a sarcastic answer. Celebrity crushes don't count.")
    await client.delete_message(ctx.message)

tem = {'id':'f/c/k'}

@client.command(pass_context=True,description="Temperature mode settings")
async def temp(ctx, mode=""):
    s = ctx.message.server.id
    if mode != "":
        if mode.lower() == "f":
            tem[s] = "f"
            await client.say("Temperature mode set to `F`.")
        elif mode.lower() == "c":
            tem[s] = "c"
            await client.say("Temperature mode set to `C`.")
        elif mode.lower() == "k":
            tem[s] == "k"
            await client.say("Temperature mode set to `K`.")
        else:
            await client.say("Unknown temperature mode.")
    else:
        if s not in tem:
            tem[s] = "f"
        await client.say("Temperature mode is `{}`.".format(tem[s].upper()))

@client.command(pass_context=True,description="Weather forecast")
async def weather(ctx, *city: str):
    tem[ctx.message.server.id] = "f"
    try:
        owm = pyowm.OWM(options.owm())
        c = ""
        for i in city:
            c = c + i + " "
        try:
            observation = owm.weather_at_place(c)
        except:
            await client.say("City not found.")
            return
        w = observation.get_weather()
        fore = w.get_status()
        if fore == "Clouds":
            fe = ":cloud:"
        elif fore == "Clear":
            fe = ":sunny:"
        elif fore == "Rain" or fore == "Drizzle":
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
        if ctx.message.server.id in tem:
            if tem[ctx.message.server.id] == "c":
                t = str(w.get_temperature('celsius')['temp']) + "°C"
                hi = str(w.get_temperature('celsius')['temp_max']) + "°C"
                lo = str(w.get_temperature('celsius')['temp_min']) + "°C"
            elif tem[ctx.message.server.id] == "k":
                t = str(w.get_temperature()['temp']) + "°K"
                hi = str(w.get_temperature()['temp_max']) + "°K"
                lo = str(w.get_temperature()['temp_min']) + "°K"
            else:
                t = str(w.get_temperature('fahrenheit')['temp']) + "°F"
                hi = str(w.get_temperature('fahrenheit')['temp_max']) + "°F"
                lo = str(w.get_temperature('fahrenheit')['temp_min']) + "°F"
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
async def loctime(ctx, *city: str):
    c = ""
    for i in city:
        c = c + i + " "
    if c.lower() == "utc " or c.lower() == "gmt ":
        utc = str(datetime.datetime.utcnow())
        await client.say(("UTC / GMT\n\n    {}\n    {}/{}/{}").format(utc[11:19],utc[5:7],utc[8:10],utc[0:4]))
    else:
        owm = pyowm.OWM(options.owm())
        try:
                observation = owm.weather_at_place(c)
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
            if hr == 12:
                m = "AM"
                day += 1
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

returnim = {'user':'True/False'}
@client.command(pass_context=True,description="Opt in and out of JonnyBot's I'm returner")
async def opt(ctx, option: str):
    if option.lower() == "in":
        returnim[ctx.message.author.id] = True
        await client.say("{0.author.mention}, you have jopted in!".format(ctx.message))
    elif option.lower() == "out":
        returnim[ctx.message.author.id] = False
        await client.say("{0.author.mention}. you have jopted out!".format(ctx.message))
    else:
        await client.say('Incorrect usage, do `~opt in` to opt in and `~opt out` to opt out.')

cahgame = {'serv id':'True/False'}
cahcb = {'serv id':['black cards']}
cahcw = {'serv id':['white cards']}
cahplayers = {'serv id':['players']}
cahpoints = {'serv id':['points (same index as players above)']}
cahhands = {'serv id':[ ['white cards (same index as players above)'],['...'] ]}
cahresp = {'serv id':['True/False for having picked or not (same index as players above)']}
cahpicked = {'serv id':[ ['cards picked (same index as players above)'],['...'] ]}
cahczar = {'serv id':'player'}
cahplaying = {'user id':'serv id'}
cahblack = {'serv id':'current black card'}
cahpick = {'serv id':'# of cards to pick (int)'}
cahchannel = {'serv id':'channel'}
cahresults = {'serv id':{'choice content':'user'}}
cahchoices = {'serv id':['options']}
cahtowin = {'serv id':"points needed to win (int)"}
cahtimeout = {'serv id':["True/False for timeout (same index as players above)"]}
cahjoining = {"serv id":["players who want to join"]}

@client.command(pass_context=True,description="Cards Against Humanity!")
async def cah(ctx, option: str=None, other: str=None):
    s = ctx.message.server.id
    cahchannel[s] = ctx.message.channel.id
    if s not in gmods:
        gmods[s] = ['219642803943112705']
    if s not in cahgame:
        cahgame[s] = False
        cahtowin[s] = 10
    if s not in cahplayers:
        cahplayers[s] = []
        cahpoints[s] = []
        cahczar[s] = ""
        cahhands[s] = []
        cahresp[s] = []
        cahpicked[s] = []
        cahtimeout[s] = []
        cahjoining[s] = []
    if s not in cahcb:
        cahcb[s] = []
        cahcw[s] = []
        cahblack[s] = ""
        cahpick[s] = ""
    if s not in turns and option not in [None,"points"]:
        await client.say("Set an order first with `~order`!")
        return
    if option not in ["restart","pause","resume","skip","points"] or ctx.message.author.id in gmods[s]:
        if option == None:
            await client.say("```Commands:\n\n~cah [option]\n\n  restart - restarts game\n  pause - pauses game\n  resume - resumes game\n  score - see the current score\n  join - join a game\n  leave - leave a game (score removed)\n  skip - skips everyone who hasnt played yet, or the czar\n  points [number] - sets the amount of points needed to win```")
        elif option.lower() == "restart":
            if not cahgame[s]:
                if len(turns[s]) > 1:
                    if len(turns[s]) == 2:
                        await client.say("Two people makes for a pretty lame game of CAH, just sayin'.\n-----")
                    cahplayers[s] = turns[s]
                    cahpoints[s] = [0 for x in range(len(turns[s]))]
                    cahhands[s] = [[] for x in range(len(turns[s]))]
                    cahresp[s] = [True for x in range(len(turns[s]))]
                    cahpicked[s] = [[] for x in range(len(turns[s]))]
                    cahgame[s] = True
                    for p in cahplayers[s]:
                        cahplaying[p] = s
                    await client.say("Starting a game of Cards Against Humanity!")
                    cahczar[s] = ctx.message.server.get_member(cahplayers[s][0])
                    await client.say("Charizard: {0.mention}".format(cahczar[s]))
                    cahcb[s] = blackCards
                    random.shuffle(cahcb[s])
                    cahcw[s] = whiteCards
                    random.shuffle(cahcw[s])
                    cahblack[s] = cahcb[s].pop()
                    await client.say("```css\n{}\n```".format(cahblack[s]))
                    cahpick[s] = cahblack[s].count("_")
                    if cahpick[s] == 0:
                        cahpick[s] = 1
                    for index in range(len(cahplayers[s])):
                        pm = ctx.message.server.get_member(cahplayers[s][index])
                        try:
                            if cahplayers[s][index] != cahczar[s].id:
                                bcmessage = "-CAH-```css\n{}\n```\nYour cards:\n\n".format(cahblack[s])
                                for j in range(10):
                                    cahhands[s][index].append(cahcw[s].pop())
                                mess = ""
                                cnt = 1
                                for k in cahhands[s][index]:
                                    if mess == "":
                                        mess += '```{}) {}```'.format(cnt,k)
                                    else:
                                        mess += "\n" + '```{}) {}```'.format(cnt,k)
                                    cnt += 1
                                if cahpick[s] == 1:
                                    mess = bcmessage + mess + "\nPick `" + str(cahpick[s]) + "` card!"
                                else:
                                    mess = bcmessage + mess + "\nPick `" + str(cahpick[s]) + "` cards!"
                                await client.send_message(pm,mess)
                                cahresp[s][index] = False
                            else:
                                await client.send_message(pm,"-CAH-```css\n{}\n```\nYou are the Charizard!".format(cahblack[s]))
                        except:
                            await client.say("An error occured sending a message to {0.mention}.".format(pm))
                else:
                    await client.say("Get some friends. Can't play CAH alone.")
            else:
                await client.say("Cannot restart while game is in progress!")
        elif option.lower() == "pause":
            if cahgame[s]:
                cahgame[s] = False
                for i in cahplayers[s]:
                    if i in cahplaying:
                        cahplaying[i] = None
                await client.say(":pause_button: Cards Against Humanity")
            else:
                await client.say("Cannot pause when game is already paused!")
        elif option.lower() == "resume":
            if not cahgame[s] and cahplayers[s] != []:
                cahgame[s] = True
                for p in cahplayers[s]:
                    cahplaying[p] = s
                await client.say(":arrow_forward: Cards Against Humanity")
            elif cahplayers[s] == []:
                await client.say("No CAH game currently exists!")
            else:
                await client.say("CAH game is already in progress!")
        elif option.lower() == "score":
            if cahplayers[s] != []:
                mess = "```"
                for pl,pnts in zip(cahplayers[s],cahpoints[s]):
                    mess += "\n    {} | {}".format(pnts,ctx.message.server.get_member(pl).display_name)
                mess += "```"
                await client.say(mess)
            else:
                await client.say("No CAH game detected.")
        elif option.lower() == "join":
            if ctx.message.author.id not in cahplayers[s]:
                cahjoining[s].append(ctx.message.author.id)
                await client.say("{0.mention} has joined the game!".format(ctx.message.author))
            else:
                await client.say("You're already in the game, {0.mention}!".format(ctx.message.author))
        elif option.lower() == "leave":
            if ctx.message.author.id in cahplayers[s]:
                i = cahplayers[s].index(ctx.message.author.id)
                await client.say("{0.mention} has left the game!".format(ctx.message.author))
                del turns[s][i], cahpoints[s][i], cahhands[s][i], cahresp[s][i], cahpicked[s][i]
                if cahgame[s]:
                    if cahczar[s].id not in cahplayers[s]:
                        await client.say("The round was skipped due to the Charizard leaving.")
                        cahresp[s] = [True for q in range(len(cahresp[s]))]
                        await client.say("Starting next round...")
                        if cahjoining[s] != []:
                            for person in cahjoining[s]:
                                cahplayers[s].append(person)
                                cahpoints[s].append(0)
                                cahhands[s].append([])
                                cahresp[s].append(True)
                                cahpicked[s].append([])
                                cahtimeout[s].append(True)
                            cahjoining[s] = []
                        if i < len(cahplayers[s]):
                            cahczar[s] = client.get_server(s).get_member(cahplayers[s][i])
                        else:
                            cahczar[s] = client.get_server(s).get_member(cahplayers[s][0])
                        await client.say("Charizard: {0.mention}".format(cahczar[s]))
                        cahpicked[s] = [[] for x in range(len(turns[s]))]
                        cahresults[s] = {}
                        cahchoices[s] = []
                        cahblack[s] = cahcb[s].pop()
                        await client.say("```css\n{}\n```".format(cahblack[s]))
                        cahpick[s] = cahblack[s].count("_")
                        if cahpick[s] == 0:
                            cahpick[s] = 1
                        for index in range(len(cahplayers[s])):
                            pm = client.get_server(s).get_member(cahplayers[s][index])
                            try:
                                if cahplayers[s][index] != cahczar[s].id:
                                    bcmessage = "-CAH-```css\n{}\n```\nYour cards:\n\n".format(cahblack[s])
                                    for j in range(10-len(cahhands[s][index])):
                                        cahhands[s][index].append(cahcw[s].pop())
                                    mess = ""
                                    cnt = 1
                                    for k in cahhands[s][index]:
                                        if mess == "":
                                            mess += '```{}) {}```'.format(cnt,k)
                                        else:
                                            mess += "\n" + '```{}) {}```'.format(cnt,k)
                                        cnt += 1
                                    if cahpick[s] == 1:
                                        mess = bcmessage + mess + "\nPick `" + str(cahpick[s]) + "` card!"
                                    else:
                                        mess = bcmessage + mess + "\nPick `" + str(cahpick[s]) + "` cards!"
                                    await client.send_message(pm,mess)
                                    cahresp[s][index] = False
                                else:
                                    await client.send_message(pm,"-CAH-```css\n{}\n```\nYou are the Charizard!".format(cahblack[s]))
                            except:
                                await client.say("An error occured sending a message to {0.mention}.".format(pm))

                    elif all(cahresp[s]):
                        cahresults[s] = {}
                        for x,y in zip(cahpicked[s],cahplayers[s]):
                            if x != []:
                                mess = "```"
                                for cards in x:
                                    mess += cards + "``````"
                                mess = mess[:-3]
                                cahresults[s][mess] = y
                        cahchoices[s] = list(cahresults[s].keys())
                        random.shuffle(cahchoices[s])
                        sendmain = "-Results-\n```css\n{}\n```-----\n{}".format(cahblack[s],"\n".join(cahchoices[s]))
                        for c,n in zip(cahchoices[s],range(len(cahchoices[s]))):
                            cahchoices[s][n] = "{}) {}".format(n+1,c)
                        send = "-Results-\n```css\n{}\n```-----\n{}\nPick your favorite!".format(cahblack[s],"\n".join(cahchoices[s]))
                        await client.send_message(client.get_server(s).get_channel(cahchannel[s]),sendmain)
                        try:
                            await client.send_message(cahczar[s],send)
                        except:
                            await client.say("An error occured sending a message to {0.mention}.".format(cahczar[s]))
                        cahresp[s][cahplayers[s].index(cahczar[s].id)] = False
            else:
                await client.say("You're not in the game, {0.mention}!".format(ctx.message.author))
        elif option.lower() == "skip":
            if cahgame[s]:
                if cahresp[s][cahplayers[s].index(cahczar[s].id)]:
                    for i,j in zip(cahresp[s],range(len(cahresp[s]))):
                        if not i:
                            await client.send_message(ctx.message.server.get_member(cahplayers[s][j]),"Your turn has been skipped.")
                    dummy = cahresp[s][:]
                    del dummy[cahplayers[s].index(cahczar[s].id)]
                    if dummy.count(True) > 0:
                        cahresp[s] = [True for x in range(len(cahresp[s]))]
                        cahresults[s] = {}
                        for x,y in zip(cahpicked[s],cahplayers[s]):
                            if x != []:
                                mess = "```"
                                for cards in x:
                                    mess += cards + "``````"
                                mess = mess[:-3]
                                cahresults[s][mess] = y
                        cahchoices[s] = list(cahresults[s].keys())
                        random.shuffle(cahchoices[s])
                        sendmain = "-Results-\n```css\n{}\n```-----\n{}".format(cahblack[s],"\n".join(cahchoices[s]))
                        for c,n in zip(cahchoices[s],range(len(cahchoices[s]))):
                            cahchoices[s][n] = "{}) {}".format(n+1,c)
                        send = "-Results-\n```css\n{}\n```-----\n{}\nPick your favorite!".format(cahblack[s],"\n".join(cahchoices[s]))
                        await client.send_message(client.get_server(s).get_channel(cahchannel[s]),sendmain)
                        try:
                            await client.send_message(cahczar[s],send)
                        except:
                            await client.say("An error occured sending a message to {0.mention}.".format(cahczar[s]))
                        cahresp[s][cahplayers[s].index(cahczar[s].id)] = False
                    else:
                        await client.say("The round has been skipped.")
                        await client.send_message(cahczar[s],"Your turn has been skipped.")
                        cahresp[s] = [True for q in range(len(cahresp[s]))]
                        await client.say("Starting next round...")
                        if cahjoining[s] != []:
                            for person in cahjoining[s]:
                                cahplayers[s].append(person)
                                cahpoints[s].append(0)
                                cahhands[s].append([])
                                cahresp[s].append(True)
                                cahpicked[s].append([])
                                cahtimeout[s].append(True)
                            cahjoining[s] = []
                        if cahplayers[s].index(cahczar[s].id) + 1 < len(cahplayers[s]):
                            cahczar[s] = client.get_server(s).get_member(cahplayers[s][cahplayers[s].index(cahczar[s].id)+1])
                        else:
                            cahczar[s] = client.get_server(s).get_member(cahplayers[s][0])
                        await client.say("Charizard: {0.mention}".format(cahczar[s]))
                        cahpicked[s] = [[] for x in range(len(turns[s]))]
                        cahresults[s] = {}
                        cahchoices[s] = []
                        cahblack[s] = cahcb[s].pop()
                        await client.say("```css\n{}\n```".format(cahblack[s]))
                        cahpick[s] = cahblack[s].count("_")
                        if cahpick[s] == 0:
                            cahpick[s] = 1
                        for index in range(len(cahplayers[s])):
                            pm = client.get_server(s).get_member(cahplayers[s][index])
                            try:
                                if cahplayers[s][index] != cahczar[s].id:
                                    bcmessage = "-CAH-```css\n{}\n```\nYour cards:\n\n".format(cahblack[s])
                                    for j in range(10-len(cahhands[s][index])):
                                        cahhands[s][index].append(cahcw[s].pop())
                                    mess = ""
                                    cnt = 1
                                    for k in cahhands[s][index]:
                                        if mess == "":
                                            mess += '```{}) {}```'.format(cnt,k)
                                        else:
                                            mess += "\n" + '```{}) {}```'.format(cnt,k)
                                        cnt += 1
                                    if cahpick[s] == 1:
                                        mess = bcmessage + mess + "\nPick `" + str(cahpick[s]) + "` card!"
                                    else:
                                        mess = bcmessage + mess + "\nPick `" + str(cahpick[s]) + "` cards!"
                                    await client.send_message(pm,mess)
                                    cahresp[s][index] = False
                                else:
                                    await client.send_message(pm,"-CAH-```css\n{}\n```\nYou are the Charizard!".format(cahblack[s]))
                            except:
                                await client.say("An error occured sending a message to {0.mention}.".format(pm))
                else:
                    await client.say("The round was skipped due to the Charizard being skipped.")
                    try:
                        await client.send_message(cahczar[s],"Your turn has been skipped.")
                    except:
                        await client.say("An error occured sending a message to {0.mention}.".format(cahczar[s]))
                    cahresp[s] = [True for q in range(len(cahresp[s]))]
                    await client.say("Starting next round...")
                    if cahjoining[s] != []:
                        for person in cahjoining[s]:
                            cahplayers[s].append(person)
                            cahpoints[s].append(0)
                            cahhands[s].append([])
                            cahresp[s].append(True)
                            cahpicked[s].append([])
                            cahtimeout[s].append(True)
                        cahjoining[s] = []
                    if cahplayers[s].index(cahczar[s].id) + 1 < len(cahplayers[s]):
                        cahczar[s] = client.get_server(s).get_member(cahplayers[s][cahplayers[s].index(cahczar[s].id)+1])
                    else:
                        cahczar[s] = client.get_server(s).get_member(cahplayers[s][0])
                    await client.say("Charizard: {0.mention}".format(cahczar[s]))
                    cahpicked[s] = [[] for x in range(len(turns[s]))]
                    cahresults[s] = {}
                    cahchoices[s] = []
                    cahblack[s] = cahcb[s].pop()
                    await client.say("```css\n{}\n```".format(cahblack[s]))
                    cahpick[s] = cahblack[s].count("_")
                    if cahpick[s] == 0:
                        cahpick[s] = 1
                    for index in range(len(cahplayers[s])):
                        pm = client.get_server(s).get_member(cahplayers[s][index])
                        try:
                            if cahplayers[s][index] != cahczar[s].id:
                                bcmessage = "-CAH-```css\n{}\n```\nYour cards:\n\n".format(cahblack[s])
                                for j in range(10-len(cahhands[s][index])):
                                    cahhands[s][index].append(cahcw[s].pop())
                                mess = ""
                                cnt = 1
                                for k in cahhands[s][index]:
                                    if mess == "":
                                        mess += '```{}) {}```'.format(cnt,k)
                                    else:
                                        mess += "\n" + '```{}) {}```'.format(cnt,k)
                                    cnt += 1
                                if cahpick[s] == 1:
                                    mess = bcmessage + mess + "\nPick `" + str(cahpick[s]) + "` card!"
                                else:
                                    mess = bcmessage + mess + "\nPick `" + str(cahpick[s]) + "` cards!"
                                await client.send_message(pm,mess)
                                cahresp[s][index] = False
                            else:
                                await client.send_message(pm,"-CAH-```css\n{}\n```\nYou are the Charizard!".format(cahblack[s]))
                        except:
                            await client.say("An error occured sending a message to {0.mention}.".format(pm))
        elif option.lower() == "points":
            if not cahgame[s] or max(cahpoints[s]) == 0:
                if other != None:
                    try:
                        cahtowin[s] = int(other)
                        await client.say("Points to win set to `{}`.".format(str(cahtowin[s])))
                    except:
                        await client.say("Give an interger value!")
                else:
                    await client.say("Points to win: `{}`.".format(str(cahtowin[s])))
        else:
            await client.say("Incorrect usage. Type `~cah` for subcommands.")
@client.event
async def on_message(message):
    if message.author.id != client.user.id and message.author.id != "325108081241489408":
        if message.server != None: #if it's a server
            #aysat spam for #nsfw-spam
            if message.author.id != message.server.me.id and message.content[0] not in [bot_prefix,"!"] and areya == True and "?" not in message.content and message.channel.name=="nsfw-spam":
                await client.send_message(message.channel, '{0.author.mention}, are you sure about that?'.format(message))
            #occasionally saying aysat to something
            if message.author.id != message.server.me.id and message.content[0] not in [bot_prefix,"!"] and "?" not in message.content and len(message.content) > 4 and " " in message.content:
                if random.randint(1,100) == 1:
                    await client.send_message(message.channel, '{0.author.mention}, are you sure about that?'.format(message))
            #i'm response
            if "im" in message.content.lower().replace("'","") or "i am" in message.content.lower() and message.author.id in returnim:
                if message.author.id not in returnim: #opt in and out support
                    returnim[message.author.id] = False
                if returnim[message.author.id] == True:
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
            #making improv work
            if message.server.id not in impstory:
                impstory[message.server.id] = []
                impgame[message.server.id] = False
            if impgame[message.server.id] == True:
                if message.content[0] == "." and message.content[1] != ".":
                    if impord[message.server.id] == True:
                        if turns[message.server.id].index(message.author.id)-1 >= 0:
                            if last[message.server.id] == turns[message.server.id][turns[message.server.id].index(message.author.id)-1]:
                                impstory[message.server.id].append(message.content)
                                last[message.server.id] = message.author.id
                                await client.add_reaction(message,"✅")
                            else:
                                await client.send_message(message.channel, "{0.author.mention}, it's not your turn!".format(message))
                        else:
                            if last[message.server.id] == turns[message.server.id][-1]:
                                impstory[message.server.id].append(message.content)
                                last[message.server.id] = message.author.id
                                await client.add_reaction(message,"✅")
                            else:
                                await client.send_message(message.channel, "{0.author.mention}, it's not your turn!".format(message))
                    else:
                        impstory[message.server.id].append(message.content)
                        await client.add_reaction(message,"✅")
                #force add
                if message.content[0:3] == "++.":
                    impstory[message.server.id].append(message.content)
                    await client.add_reaction(message,"✅")

        else: #if's it's a dm
            if message.author.id in cahplaying:
                if cahplaying[message.author.id] != None:
                    s = cahplaying[message.author.id]
                    p = cahplayers[s].index(message.author.id)
                    if not cahresp[s][p]:
                        if message.author != cahczar[s]:
                            if not cahtimeout[s]:
                                cahtimeout[s] = True
                                picked = message.content.split(" ")
                                try:
                                    picked = [int(x) - 1 for x in picked]
                                except ValueError:
                                    await client.send_message(message.author,"Invalid value given.")
                                    cahtimeout[s] = False
                                    return
                                for i in picked:
                                    if i > 9 or i < 0:
                                        await client.send_message(message.author,"Please choose values from 1 to 10.")
                                        cahtimeout[s] = False
                                        return
                                if len(picked) != cahpick[s]:
                                    if cahpick[s] != 1:
                                        await client.send_message(message.author,"Please pick `{}` cards.".format(cahpick[s]))
                                    else:
                                        await client.send_message(message.author,"Please pick `{}` card.".format(cahpick[s]))
                                else:
                                    m = "```"
                                    for i in picked:
                                        m += cahhands[s][p][i] + "``````"
                                    m = m[:-3]
                                    for i in picked:
                                        if picked.count(i) == 1:
                                            cahpicked[s][p].append(cahhands[s][p][i])
                                        else:
                                            await client.send_message(message.author,"Don't pick repeats!")
                                            cahtimeout[s] = False
                                            return
                                    print(cahhands[s][p])
                                    for i in cahpicked[s][p]:
                                        cahhands[s][p].remove(i)
                                    print(cahhands[s][p])
                                    cahresp[s][p] = True
                                    await client.send_message(client.get_server(s).get_channel(cahchannel[s]),"{0.author.mention} is done picking!".format(message))
                                    await client.send_message(message.author,"Success!")
                                    if all(cahresp[s]):
                                        cahresults[s] = {}
                                        for x,y in zip(cahpicked[s],cahplayers[s]):
                                            if x != []:
                                                mess = "```"
                                                for cards in x:
                                                    mess += cards + "``````"
                                                mess = mess[:-3]
                                                cahresults[s][mess] = y
                                        cahchoices[s] = list(cahresults[s].keys())
                                        random.shuffle(cahchoices[s])
                                        sendmain = "-Results-\n```css\n{}\n```-----\n{}".format(cahblack[s],"\n".join(cahchoices[s]))
                                        for c,n in zip(cahchoices[s],range(len(cahchoices[s]))):
                                            cahchoices[s][n] = "{}) {}".format(n+1,c)
                                        send = "-Results-\n```css\n{}\n```-----\n{}\nPick your favorite!".format(cahblack[s],"\n".join(cahchoices[s]))
                                        await client.send_message(client.get_server(s).get_channel(cahchannel[s]),sendmain)
                                        try:
                                            await client.send_message(cahczar[s],send)
                                        except:
                                            await client.send_message(client.get_server(s).get_channel(cahchannel[s]),"An error occured sending a message to {0.mention}.".format(cahczar[s]))
                                        cahresp[s][cahplayers[s].index(cahczar[s].id)] = False
                                    else:
                                        print(cahresp[s])
                                cahtimeout[s] = False
                        else:
                            if not cahtimeout[s]:
                                cahtimeout[s] = True
                                try:
                                    picked = int(message.content) - 1
                                except ValueError:
                                    await client.send_message(message.author,"Invalid value given.")
                                    cahtimeout[s] = False
                                    return
                                try:
                                    if picked < 0:
                                        await client.send_message(message.author,"Please choose a value from 1 to {}.".format(len(cahchoices[s])))
                                        cahtimeout[s] = False
                                        return
                                    answer = cahchoices[s][picked][cahchoices[s][picked].index(")")+2:]
                                    chan = client.get_server(s).get_channel(cahchannel[s])
                                    winner = cahresults[s][answer]
                                    await client.send_message(message.author,"Success!")
                                    cahpoints[s][cahplayers[s].index(winner)] += 1
                                    scoreboard = "```"
                                    for pl,pnts in zip(cahplayers[s],cahpoints[s]):
                                        scoreboard += "\n    {} | {}".format(pnts,client.get_server(s).get_member(pl).display_name)
                                    scoreboard += "```"
                                    await client.send_message(chan,"----------\n{0}\n{1.mention} won the round!\n-----\n{2}\n----------".format(answer,client.get_server(s).get_member(winner),scoreboard))
                                    if cahpoints[s][cahplayers[s].index(winner)] >= cahtowin[s]: #work on this
                                        await client.send_message(chan,"{0.mention} wins the game!".format(client.get_server(s).get_member(cahplayers[s][cahplayers[s].index(winner)])))
                                        cahpoints[s] = [0 for x in range(len(turns[s]))]
                                        cahhands[s] = [[] for x in range(len(turns[s]))]
                                        cahresp[s] = [True for x in range(len(turns[s]))]
                                        cahpicked[s] = [[] for x in range(len(turns[s]))]
                                        cahgame[s] = False
                                        return
                                    await client.send_message(chan,"Starting next round...")
                                    if cahjoining[s] != []:
                                        for person in cahjoining[s]:
                                            cahplayers[s].append(person)
                                            cahpoints[s].append(0)
                                            cahhands[s].append([])
                                            cahresp[s].append(True)
                                            cahpicked[s].append([])
                                            cahtimeout[s].append(True)
                                        cahjoining[s] = []
                                    if cahplayers[s].index(cahczar[s].id) + 1 < len(cahplayers[s]):
                                        cahczar[s] = client.get_server(s).get_member(cahplayers[s][cahplayers[s].index(cahczar[s].id)+1])
                                    else:
                                        cahczar[s] = client.get_server(s).get_member(cahplayers[s][0])
                                    await client.send_message(chan,"Charizard: {0.mention}".format(cahczar[s]))
                                    cahpicked[s] = [[] for x in range(len(turns[s]))]
                                    cahresults[s] = {}
                                    cahchoices[s] = []
                                    cahblack[s] = cahcb[s].pop()
                                    await client.send_message(chan,"```css\n{}\n```".format(cahblack[s]))
                                    cahpick[s] = cahblack[s].count("_")
                                    if cahpick[s] == 0:
                                        cahpick[s] = 1
                                    for index in range(len(cahplayers[s])):
                                        pm = client.get_server(s).get_member(cahplayers[s][index])
                                        try:
                                            if cahplayers[s][index] != cahczar[s].id:
                                                bcmessage = "-CAH-```css\n{}\n```\nYour cards:\n\n".format(cahblack[s])
                                                for j in range(10-len(cahhands[s][index])):
                                                    cahhands[s][index].append(cahcw[s].pop())
                                                mess = ""
                                                cnt = 1
                                                for k in cahhands[s][index]:
                                                    if mess == "":
                                                        mess += '```{}) {}```'.format(cnt,k)
                                                    else:
                                                        mess += "\n" + '```{}) {}```'.format(cnt,k)
                                                    cnt += 1
                                                if cahpick[s] == 1:
                                                    mess = bcmessage + mess + "\nPick `" + str(cahpick[s]) + "` card!"
                                                else:
                                                    mess = bcmessage + mess + "\nPick `" + str(cahpick[s]) + "` cards!"
                                                await client.send_message(pm,mess)
                                                cahresp[s][index] = False
                                            else:
                                                await client.send_message(pm,"-CAH-```css\n{}\n```\nYou are the Charizard!".format(cahblack[s]))
                                        except:
                                            await client.send_message(client.get_server(s).get_channel(cahchannel[s]),"An error occured sending a message to {0.mention}.".format(pm))
                                except IndexError:
                                    await client.send_message(message.author,"Please choose a value from 1 to {}.".format(len(cahchoices[s])))
                            cahtimeout[s] = False
    await client.process_commands(message)

client.run(options.token())
