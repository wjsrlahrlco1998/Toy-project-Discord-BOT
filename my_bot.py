import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot

client = discord.Client()

@client.event
async def on_message(message):
    content = message.content
    guild = message.guild
    author = message.author
    channel = message.channel
    if content.startswith("!test"):
        await message.channel.send("test" + message.content)
    if content == "!ping":
        await message.channel.send("Pong!")


client.run('MTAyMzE3MjIzNDEyNDIwNjEzMA.GRggsV.JFlCBkdkOohsdpADD8j1bJuZA-QTCdjzpGemRk')