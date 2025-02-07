import discord
import os
from dotenv import load_dotenv
import time



# Import silicoAi file
import sys
sys.path.insert(0, 'SilicoAi')
import SilicoAi

import logging
# Load environment variables and initialize the bot
load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)

# Discord Guild IDs
guildId = os.getenv("GUILD_IDs")

# Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Initialize SilicoAi
silicoAi = SilicoAi.silicoAi()


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=[guildId])
async def hello(ctx):
    async with ctx.typing():
        await ctx.send("Typing...")
    
    await ctx.respond(f"Hello! {ctx.author.name}")

@bot.event
async def on_message(message):
    start_time = time.time()
    if message.author == bot.user:
        return
    
    async with message.channel.typing():
    # simulate something heavy
        print(message.content)
        response = silicoAi.generate(message.content)
        print(response)
        await message.channel.send(response)

    print('Time Taken:', time.strftime("%H:%M:%S",time.gmtime(time.time() - start_time)))


bot.run(os.getenv("CLIENT_TOKEN"))
