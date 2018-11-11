import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random
import youtube_dl

startup_extensions = [
  'cogs.message','cogs.owner'
]

bot = commands.Bot(command_prefix='f!')
ownerID = "405266248314781696"

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
            
# To remove the help command and make your own help command
#bot.remove_command('help')

@bot.event
async def on_ready():
  print ("------")
  print ("My name is " + bot.user.name)
  print ("With the ID: " + bot.user.id)
  print ("Using discord.py v" + discord.__version__)
  print ("------")
  
@bot.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await bot.send_message(server, fmt.format(member, server))
    
@bot.event
async def on_member_leave(member):
    server = member.server
    fmt = '{0.mention} left {1.name}...'
    await bot.send_message(server, fmt.format(member, server))

@bot.command(pass_context=True)
async def say(ctx, *args):
  """Makeme say your message"""
  if ctx.message.author.id in ownerID:
      channel = ctx.message.channel
      mesg = ' '.join(args)
      await bot.delete_message(ctx.message)
      await bot.send_typing(channel)
      await asyncio.sleep(1)
      await bot.say(mesg)
      print (ctx.message.author.id + " or " +ctx.message.author.name + " made me say'{}'".format(mesg))
  else:
      channel = ctx.message.channel
      mesg = ' '.join(args)
      await bot.delete_message(ctx.message)
      await bot.send_typing(channel)
      await asyncio.sleep(1)
      await bot.say(mesg)
      print (ctx.message.author.id + " or " + ctx.message.author.name + " made me say'{}'".format(mesg))
      
@bot.command(pass_context=True)
async def playing(ctx, *args):
  if ctx.message.author.id in OwnerID:
    mesg = ''.join(args)
    await bot.change_presence(game=discord.Game(name= (mesg)))
    await bot.say("I am now playing" + mesg)
    
@bot.event
async def on ready():
  print ("Ready when you are xd")
  print ("I am running on " + bot.user.name)
  print ("With the ID: " + bot.user.id)
  
@bot.command(pass_context=True)
async def ping(ctx):
  await bot.say("ping_pong: ping!! xSSS"
  print ("user has pinged")
                
@bot.command(pass(context=True)
async def info(ctx, user: discord.Member):
     await bot.say("The users name is: {}".format(user.name))       
     await bot.say("The users ID is: {}".format(user.id))
     await bot.say("The users status is: {}".format(user.status))  
     await bot.say("The users highest role is: {}".format(user.top_role))   
     await bot.say("The user joined at: {}".format(user.joined_at)) 

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name)) 
    await bot.kick(user) 

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):  
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.ban(user)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
bot.run(os.environ.get('Token'))
