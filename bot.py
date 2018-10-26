import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random
import youtube_dl

bot = commands.Bot(command_prefix='>')
ownerID = "405266248314781696"

# To remove the help command and make your own help command
#bot.remove_command('help')

@bot.event
async def on_ready():
  print ("------")
  print ("My name is " + bot.user.name)
  print ("With the ID: " + bot.user.id)
  print ("Using discord.py v" + discord.__version__)
  print ("------")

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
bot.run(os.environ.get('Token'))

@bot.command(pass_context=true)
async def say(ctx, *args):
  """Make me say your message""
  if ctx.message.author.id in ownerID:
  channel = ctx.message.channel
  mesg = ' '.join(args)
  await bot.delete_message(ctx.message)
  await bot.send_typing(channel)
  await asyncio.sleep(1)
  await bot.say(mesg)
  print (ctx.message.author.id + " or " +
ctx.message.author.name + "mademe say
'{}'".format(mesg))
    else:
    channel = ctx.message.channel
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    await bot.send_typing(channel)
    await asyncio.sleep(1)
    await bot.say(mesg)
    print (ctx.message.author.id + " or " +
ctx.message.author.name + " made me say
'{}'".format(mesg))
