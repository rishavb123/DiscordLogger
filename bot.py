import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
log_channel = None

@client.event
async def on_ready():
    global log_channel
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    log_channel = discord.utils.get(guild.channels, name="logs")
    # await log_channel.send("I have initialized")

client.run(TOKEN)