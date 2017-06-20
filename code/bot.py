import discord
import random

from discord.ext import commands

description = "JonnyBot - Irritation and game night"
bot_prefix = "~"

client = commands.Bot(description=description, command_prefix=bot_prefix)

a = False
aly = ["Go scotts!", "I LOVE CATS THEYRE SO CUTE@@@@@@@@", "YOURE KILLING POLAR BEARS", "JUPITER DOESN'T HAVE FEELINGS","Tr****","KILL YOURSELFFFFFFFFFFF","Water your plant!","RUDEEEE!","😂😂😂 lol!","GO DIE IN A HOLE!!!!","FIGHT ME","Yus!","GDP","FKENWO-","FNEKDKS","TBEICNE","YOU WRETCHED BAFFONS!!!!","Rhanks!","ASDLKFJASLDFA","ASFJAALSKDFJ","ASDFLKJASDF","ASDFAGSZSEF","KILL YOUR ELF","ASJDKFASDFKLJASDFAWERFAESFSRFSFCXSCVZSCRVCSCVCZ", "VERLYSSA ISN'T REAL@@@@@@@@", "I HATE YOU@@@@@@", "YOU GITA SUCK@@@@@", "NOOOOOK", "HEYYYYYY","GALEXXXXXXXXXXXXX","ALEX ONLY HAS FEELINGS FOR GABBYYYYYYYY@@@@@@@@@@@@"]

jo = ["Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lol","Lo\n*l","Lpl\n*Lol","Lpl\n*Lpl\n**Lol","WE MUST SEIZE THE MEANS OF SOCIAL GRATIFICATION"]

kw = ["Annoying and unoriginal","Good question","#discordmasterrace"]

wyrq = open("C:\\Users\\Jonny\\Desktop\\aysatbot\\wyr.txt","r",encoding='utf8')
wyrlist = wyrq.readlines()

truthq = open("C:\\Users\\Jonny\\Desktop\\aysatbot\\truths.txt","r",encoding='utf8')
truthlist = truthq.readlines()

story = {'id': ["list"]}
game = {'id': "True/False"}

@client.event
async def on_ready():
    print("------")
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print(discord.__version__)
    print("------")

@client.command(pass_context=True,description="Simulates Alyssa's speech patterns with 100% accuracy")
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

@client.command(pass_context=True,description="Toggles 'Are you sure about that' spam; only works in '#nsfw-spam'")
async def aysat(ctx):
    if ctx.message.channel.name == "nsfw-spam":
        global a
        a = not a
        if a == True:
            await client.say("[aysat: ON]")
        else:
            await client.say("[aysat: OFF]")

@client.command(pass_context=True,description="Randomly selects a 'would you rather' question from a list")
async def wyr(ctx):
    global wyrlist
    rand = random.choice(wyrlist)
    await client.say(rand)

@client.command(pass_context=True,description="Randomly selects a 'truth' question from a list")
async def truth(ctx):
    global truthlist
    rand = random.choice(truthlist)
    await client.say(rand)

@client.command(pass_context=True,description="For Improv games:\n\nstart: starts Improv game\nstop: ends Improv game\nresume: resumes the Improv game\ndelete: deletes last entry\nstory: prints the Improv story")
async def improv(ctx, option: str):
    global story, game
    s = ctx.message.server.id
    if s not in story:
        story[s] = []
        game[s] = False
    if option == "start":
        if game[s] == False:
            game[s] = True
            story[s] = []
            await client.say("Improv beginning now!")
        else:
            await client.say("Improv game already in progress!")
    elif option == "stop":
        if game[s] == True:
            game[s] = False
            para = ""
            await client.say("Finishing...")
            for i in story[s]:
                j = i[1:]
                para += " " + j
            await client.say(para)
        else:
            await client.say("Improv game not detected.")
    elif option == "story":
        para = ""
        for i in story[s]:
            j = i[1:]
            para += " " + j
        await client.say(para)
    elif option == "delete":
        if game[s] == True:
            await client.say('Deleting "%s"...' % story[s][-1][1:])
            story[s] = story[s][:-1]
        else:
            await client.say("Improv game not in progress.")
    elif option == "resume":
        if game[s] == False:
            game[s] = True
            await client.say("Improv resuming now!")
        else:
            await client.say("Improv game already in progress!")
    else:
        await client.say("Unknown Improv command.")


@client.event
async def on_message(message):
    global story, game
    if message.author.id != message.server.me.id and message.content[0] != bot_prefix and a == 1 and message.content[-1] != "?" and message.channel.name=="nsfw-spam":
        await client.send_message(message.channel, '{0.author.mention}, are you sure about that?'.format(message))
    if "game night" in message.content.lower() and message.channel.name == "game-night":
        gn = message.server.roles
        for i in gn:
            if i.name == "game-night":
                await client.send_message(message.channel, "{0.mention}".format(i))
    if message.content.lower()[0:4] == "i'm ":
        await client.send_message(message.channel, "Hi, " + message.content[4:])
    elif message.content.lower()[0:3] == "im ":
        await client.send_message(message.channel, "Hi, " + message.content[3:])
    elif message.content.lower()[0:5] == "i am ":
        await client.send_message(message.channel, "Hi, " + message.content[5:])
    if message.server.id not in story:
        story[message.server.id] = []
        game[message.server.id] = False
    if game[message.server.id] == True:
        if message.content[0] == "." and message.content[1] != ".":
            story[message.server.id].append(message.content)
    await client.process_commands(message)

client.run("Nevergonnagiveyouupnevergonnaletyoudownnevergonnarunaroundanddesertyou")
