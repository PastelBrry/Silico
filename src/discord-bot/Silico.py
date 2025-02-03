import discord
import os
from dotenv import load_dotenv

import logging
# Load environment variables and initialize the bot
load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)


guildId = os.getenv("GUILD_IDs")

# Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=[guildId])
async def hello(ctx):
    async with ctx.typing():
        await ctx.send("Typing...")
    
    await ctx.respond(f"Hello! {ctx.author.name}")

bot.run(os.getenv("CLIENT_TOKEN"))
