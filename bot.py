import discord
import os
from discord.ext import commands


bot = commands.Bot(prefix="-", owner_id=277981712989028353)


@bot.event
async def on_message(message):
