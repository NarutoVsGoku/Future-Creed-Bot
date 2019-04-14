import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random
import youtube_dl
import time

startup_extensions = [
  'cogs.message','cogs.owner'
]

bot = commands.Bot(command_prefix='f!')
bot.remove_command('help')
ownerID = "405266248314781696"
ownerID2 = "502562008420450305"

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
async def say(ctx, *, args):
  """Make me say your message"""
  if ctx.message.author.id in ownerID or ownerID2:
      channel = ctx.message.channel
      await bot.delete_message(ctx.message)
      await bot.send_typing(channel)
      await asyncio.sleep(1)
      await bot.say(args)
   
      
@bot.command(pass_context=True)
async def playing(ctx, *args):
  if ctx.message.author.id in ownerID or ownerID2:
    mesg = ' '.join(args)
    await bot.change_presence(game=discord.Game(name= (mesg)))
    await bot.say("I am now playing " + mesg)
  else:
    bot.say("Are you sure you can use this command")
  
@bot.command(pass_context=True)
async def ping(ctx):
    t = await bot.say ('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await bot.edit_message(t, new_content='Pong! Took: {}ms'.format(int(ms)))
    

@bot.command(pass_context=True)
async def secretmesg(ctx, *args):
  if ctx.message.author.id in ownerID or ownerID2:
    mesg = ' '.join(args)
    await bot.send_message(discord.Object(id='541259959544053761'), mesg)
    
@bot.command(pass_context=True)
async def help(ctx):
  embed = discord.Embed(name='help', description=None, color=0x0000b3)
  embed.set_author(name=ctx.message.author.name)
  embed.add_field(name='Owner', value='not finished', inline=False)
  embed.add_field(name='Cmds', value='List of commands (so far)', inline=False)
  
  
  await bot.say(embed=embed)
  
@bot.command(pass_context=True)
async def owner(ctx):
  if ctx.message.author.id in ownerID or ownerID2:
    embed = discord.Embed(name='owner commands', description=None, color=0x0000b3)
    embed.set_author(name=ctx.message.author.name)
    embed.add_field(name='playing', value='Sets my playing status.', inline=False)
    embed.add_field(name='secretmesg', value='Sends a secret message.', inline=False)
    embed.add_field(name='say', value='Says your message', inline=False)
  
    await bot.say(embed=embed)
  else:
    embed =discord.Embed(name='Error', description=None, color=0xff0000)
    embed.set_author(name=ctx.message.author.name)
    embed.add_field(name='Permission Error', value='Are you sure you have permission to use this command?', inline=False)
    
    await bot.say(embed=embed)
  
@bot.command(pass_context=True)
async def cmds(ctx):
  embed = discord.Embed(name='cmds', description=None, color=0x0000b3)
  embed.set_author(name=ctx.message.author.name)
  embed.add_field(name='ping', value='Replies pong (Not Accurate)', inline=False)
  embed.add_field(name='invite', value='Replies a bot invite', inline=False)
  embed.add_field(name='botinfo', value='Replies a bot info', inline=False)
  
  await bot.say(embed=embed)
  
@bot.command(pass_context=True)
async def invite(ctx):
  """Invite Me"""
  await bot.say("here's my invite link")
  await bot.say(f"https://discordapp.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot")

@bot.command(pass_context=True)
async def botinfo(ctx):
    """Information about this bot"""
    embed = discord.Embed(name='My Information', description=None, color=0x0000b3)
    embed.add_field(name='Version', value="using discord.py v" + discord.__version__, inline=False)
    embed.add_field(name='Developer', value='<@405266248314781696> and <@502562008420450305>', inline=False)
    embed.add_field(name='How many commands?', value=f'{str(len(bot.commands))} commands', inline=False)
    await bot.say(embed=embed)
    
@bot.command(pass_context=True)
async def serverlist(ctx):
  servers = list(bot.guilds)
  for x in range(len(servers)):
      await ctx.author.send(f'name: {servers[x-1].name}\nID: {servers[x-1].id}')
  if ctx.message.guild:
      await bot.say('The list has been send to your DMs!')
  if not ctx.message.guild:
      return
     
  
  



  
  
  
  
  
  
  
  
  
  
  
bot.run(os.environ.get('Token'))
