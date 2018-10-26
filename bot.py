import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random
import youtube_dl

startup_extensions = [
  'cogs.message'
]

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot = commands.Bot(command_prefix='f!')
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
  const Discord = require("discord.js");
  const client = new Discord.client();
  
  const newUsers = [];
  
  client.on("ready", () => {console.log("I am ready!")'});
  client.on("message", (message) => {
    if (message.content.startsWith("ping")) {message.channel.send("!");}}];

  client.on("guildMemberADD", (member) => {
    const guild = member .guild;
    if (!newUsers[guild.id] newUsers[guild.id] = new Discord.Collection();
        newUsers[guild.id].set(member.id, member.user);
        
        if (newUsers[guild.id).size > 10) {
           const userlist = newUsers[guild.id].map(u => u.toString()).join("");
          guild.channels.find(channel => channel.name === "general").send("Welcome our new users!\n" + userlist);
          newUsers[guild.id].clear();}});
  client.on("guildMemberRemove", (member) => {
    const guild = member.guild;
    if (newUsers[guild.id].has(member.id))
  newUsers.delete(member.id);});
  client.login("SuperSecretBotTokenHere");
   
        
        
       
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
bot.run(os.environ.get('Token'))
