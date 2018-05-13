import discord
import os
from discord.ext import commands


bot = commands.Bot(command_prefix="-", owner_id=277981712989028353)


@bot.event
async def on_ready():
    print("Bot is online, and READY TO ROLL!")
    await bot.change_presence(activity=discord.Game(name="with Mega Elite™"))


@bot.event
async def on_message(message):
    if message.content.lower() == 'hi':
        await message.channel.send("Hiya! I'm a fun bot :D")
    elif message.content.lower() == "what's up":
        await message.channel.send("Meh...not much")
    elif message.content.lower() == "fuck" or message.content.lower() == "bitch" or message.content.lower() == "shit":
        await message.delete()
        await message.channel.send(f"{message.author.mention}, you can't swear! BOI! :rage:", delete_after=3)
    elif message.content.startswith("https://discord.gg/"):
        await message.delete()
        await message.channel.send("Hey! Mega Elite™ is not an invite friendly zone unless given permission by an Administrator!")
    elif message.content.lower() == "lol":
        await message.channel.send("XD")
    elif "gay" in message.content.lower():
        await message.channel.send("no u")
    else:
        await bot.process_commands(message)
        
        
@bot.event
async def on_private_channel_create(chan):
    await chan.send(":boom: Hi! Thanks for texting me! I am __**Mega Elite's**__ custom bot! :boom: Please subscribe to **Joshua Dodson's YouTube Channel** with this link! -  https://www.youtube.com/channel/UCqqZRbhAn-c724MtJ5ELGiA :boom:")
    
    
bot.run(os.environ.get("TOKEN"))
