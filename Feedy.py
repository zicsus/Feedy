import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from Parser.Parser import *

Client = discord.Client()
client = commands.Bot(command_prefix = "?")

parser = Parser()

@client.event
async def on_ready():
    print("Feedy is online!")

@client.event
async def on_message(message):
    if(message.content == "cookie"):
        await client.send_message(message.channel, ":cookie:")

    if(message.content.startswith == "!F"):
        parser.getLatestFeed()
        await client.send_message(message.channel, "Getting latest feed")


client.run("YOUR_TOKEN")