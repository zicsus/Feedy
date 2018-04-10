import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from Parser.Parser import Parser

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

url = ""
parser = Parser(url)

@client.event
async def on_ready():
    print("Feedy is online!")

@client.event
async def on_message(message):
    if(message.content.lower() == "!help"):
        response = "I don't do much at the time. but here's what i got \n -> !top5 : Get latest latest 5 gaming news"
        await client.send_message(message.channel, response)

    elif(message.content == "!top5"):
        await client.send_message(message.channel, "Getting top 5 news. Please Wait...")
        parser.update()
        top5 = parser.top5()  
        for x in top5:
            response = x["title"] + "\n\n"
            response += x["description"][0:200] + "... \n"
            response += x["media"]
            await client.send_message(message.channel, response)
    
    elif()
        

client.run("NDIyNDUzNjA2NjU0OTM1MDQz.DYcBsQ.ftZTzQxbKEU1Kif5m5PRyjLYH00")