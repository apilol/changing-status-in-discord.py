import discord
import asyncio
from discord.ext import commands

token = "bot token" # Bot Token
intents = discord.Intents().all() # Discord Intents (Can be Activated at Discord Developer)
bot = commands.Bot(command_prefix='>', intents=intents)

# / Status Part # \
async def ch_pr(): # Defining
 await bot.wait_until_ready() # Activate when Bot Is Ready  
 wstatuses = ["For Rule Breakers", "Github Tut"] # Actual Status Part
 while not bot.is_closed(): # If Bot Not Closed, Start Statuses
   watchingstatus = random.choice(wstatuses) # Randomly Choose From Your Status List
   await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=watchingstatus)) # Sets the Bots Status (You Can change status=discord.Status.dnd)
   await asyncio.sleep(7) # Changes status Every 7 Seconds (to Change time, Change the Number
    
    
# / Running Bot & ETC # \
bot.loop.create_task(ch_pr())
bot.run(token)
