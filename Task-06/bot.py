from discord.ext import commands
import discord
import random
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MAIN = 1412005642562179072
ORIENTATION = 1412137892746362931
ANOUNCEMENTS = 1412146933459583006

bot = commands.Bot(command_prefix="!" , intents = discord.Intents.all())

@bot.event

async def on_ready():

    print("hello brodie!!")
    channel = bot.get_channel(MAIN)
    await channel.send("Hello! Friendly Neighbourhood Bot is activated.")

WISDOM = {"rules":"Midtown Tech Rules: Be respectful, no spam, stay on topic!",
          "resources":"please refer documentation of discord.py and discord.ext",
          "contact":"maryjane@outmail.com"
}

@bot.command()

async def wisdom(cfx,type):
    if type in WISDOM:
        await cfx.send(WISDOM.get(type.lower()))
    else:
        await cfx.send("Invalid topic, try rules or resources or contact")
@bot.event

async def on_member_join(member):
    channel = bot.get_channel(ORIENTATION)
    role_1 = discord.utils.get(member.guild.roles, name="Aspiring Hero")
    role_2 = discord.utils.get(member.guild.roles, name="New Student")
    await channel.send(f"Welcome {member.mention} brodie to Midtown Tech!!")
    await member.add_roles(random.choice([role_1, role_2]))


FORBIDDEN = ["villainous spam", "unauthorized link", "off-topic disruption", "menacing threats"]

@bot.event

async def on_message(message):
    if message.author.bot:
        return
    
    for word in FORBIDDEN:
        if word in message.content.lower():
            await message.delete()
            await message.author.send("please follow the rules")
            return
    await bot.process_commands(message) 

@bot.command()
@commands.has_role("faculty")
async def bugle(cfx,*,message):
    channel = bot.get_channel(ANOUNCEMENTS)
    announcement = await channel.send(message)
    async def shred():
            await asyncio.sleep(24*60*60)  
            if not announcement.pinned:
                await announcement.delete()
    bot.loop.create_task(shred())

bot.run(BOT_TOKEN)
