import discord 
from discord.ext import commands
import random
from dotenv import load_dotenv, find_dotenv
import os

from config import LOX_IDS, EMOJI, BOSS_OF_THE_GYM

load_dotenv(find_dotenv())

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents) 


@bot.event
async def on_ready():
    print("Bot is up and running...")


@bot.event
async def on_message(message):
    if message.author == bot.user: return

    if message.author.id in LOX_IDS:
        await message.add_reaction(EMOJI)
        if (random.random() * 10) < 0.5: # 5%
            await message.reply("Хохла забыть спросили", mention_author=False)

    await bot.process_commands(message)


@bot.command(name='clear', help='this command will clear last 10 (by default) messages')
@commands.has_role(BOSS_OF_THE_GYM)
async def clear(ctx, amount = 10):
    await ctx.channel.purge(limit=amount)


bot.run(os.getenv("TOKEN"))