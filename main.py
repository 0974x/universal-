import discord
import os
import random
import requests
from discord.ext import commands, tasks
import asyncio

intents = discord.Intents.all()


bot = commands.Bot(command_prefix="-", intents=intents)

statuses = [
    discord.Game("0974x | osama"),
    discord.Streaming(name="Streaming on Twitch", url="https://twitch.tv/yourchannel"),
    discord.Activity(type=discord.ActivityType.listening, name="osama")
]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'Made By 0974x')
    
    change_status.start()
    
    cogs_to_load = ['info', 'voice', 'clone', 'interface']
    for cog in cogs_to_load:
        try:
            await bot.load_extension(f'cogs.{cog}')
            print(f'Loaded cog: {cog}')
        except Exception as e:
            print(f'Failed to load cog {cog}: {e}')
    

    try:
        await bot.tree.sync()
        print("Slash commands synced successfully.")
    except Exception as e:
        print(f"Error syncing slash commands: {e}")

@tasks.loop(seconds=10)
async def change_status():
    for status in statuses:
        await bot.change_presence(activity=status)
        await asyncio.sleep(10)

bot.run('MTI4NDgyOTkxMzU5Mjg5MzQ5Mg.GO3NIG.SMXhcwHJclqOTrvf9gt6BdgiV3cGAVWSldiqic')
