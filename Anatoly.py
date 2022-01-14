import discord
from discord.ext import commands

from bs4 import BeautifulSoup
from lxml import etree
import requests

import datetime
import asyncio

def __init__(self, *args, **kwargs):
  super().__init__(*args, **kwargs)
  

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='?', intents=intents)

@client.event
async def on_ready():
  print("Up and running")
  await my_background_task()

@client.command()
@commands.has_permissions(manage_messages=True)
async def mntk(ctx):
  embed = discord.Embed(
    title="Bot Commands",
    description="Vitaj cavo u nas doma",
    color=discord.Colour.green()
  )
  embed.set_thumbnail(url="https://i.imgur.com/RASv4KS.jpeg")

  embed.add_field(
    name="?mntk",
    value="ten príkaz",
    inline=True
  )

  await ctx.send(embed=embed)

@client.event
async def on_raw_reaction_add(payload):
  if payload.message_id != 923669203045736458:
    return

  #print(self.target_message_id)
  guild = client.get_guild(payload.guild_id)

  print(payload.emoji.name)

  if(payload.emoji.name == "🕹️"):
    role = discord.utils.get(guild.roles, name="GameDevelopment")
    await payload.member.add_roles(role)
  elif(payload.emoji.name == "💣"):
    role = discord.utils.get(guild.roles, name="Csgo")
    await payload.member.add_roles(role)
  elif(payload.emoji.name == "⚔️"):
    role = discord.utils.get(guild.roles, name="Lol")
    await payload.member.add_roles(role)
  elif(payload.emoji.name == "🏹"):
    role = discord.utils.get(guild.roles, name="ThetanArena")
    await payload.member.add_roles(role)
  elif(payload.emoji.name == "📰"):
    role = discord.utils.get(guild.roles, name="Aktualne spravy")
    await payload.member.add_roles(role)
  elif(payload.emoji.name == "💰"):
    role = discord.utils.get(guild.roles, name="Crypto")
    await payload.member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
  if payload.message_id != 923669203045736458:
    return

  guild = client.get_guild(payload.guild_id)
  member = guild.get_member(payload.user_id)

  print(payload.emoji.name)

  if(payload.emoji.name == "🕹️"):
    role = discord.utils.get(guild.roles, name="GameDevelopment")
    await member.remove_roles(role)
  elif(payload.emoji.name == "💣"):
    role = discord.utils.get(guild.roles, name="Csgo")
    await member.remove_roles(role)
  elif(payload.emoji.name == "⚔️"):
    role = discord.utils.get(guild.roles, name="Lol")
    await member.remove_roles(role)
  elif(payload.emoji.name == "🏹"):
    role = discord.utils.get(guild.roles, name="ThetanArena")
    await member.remove_roles(role)
  elif(payload.emoji.name == "📰"):
    role = discord.utils.get(guild.roles, name="Aktualne spravy")
    await member.remove_roles(role)
  elif(payload.emoji.name == "💰"):
    role = discord.utils.get(guild.roles, name="Crypto")
    await member.remove_roles(role)


def CheckFon():
    webpage = requests.get("https://fontech.startitup.sk/")
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))
    global oldname
    oldname=None

    try:
        titul = dom.xpath('/html/body/div[4]/div[7]/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div')[0].text
        img_temp = dom.xpath("/html/body/div[4]/div[7]/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/@data-bg")
        link_temp = dom.xpath("/html/body/div[4]/div[7]/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/a/@href")
    except:
        titul = "null"
        img_temp = "null"
        link_temp = "null"

    #print(titul)
    link = link_temp[0]
    #print(link)
    img = img_temp[0]
    img = img.replace("url","")
    img = img.replace("(","")
    img = img.replace(")","")
    #print(img)

    if oldname != titul and titul != None and img != None:
        oldname = titul
        return titul,img,link
    else:
        titul = None
        img = None
        link = None
        return titul,img,link

def CheckHz():
    webpage = requests.get("https://hernazona.aktuality.sk/")
    soup = BeautifulSoup(webpage.content, "html.parser")
    dom = etree.HTML(str(soup))
    global oldname
    oldname=None

    try:
        titul = dom.xpath('/html/body/div[1]/div/div/div[2]/div[4]/div[1]/div[3]/div/div/div/div[1]/div/div/a/h2')[0].text
        img_temp = dom.xpath("/html/body/div[1]/div/div/div[2]/div[4]/div[1]/div[3]/div/div/div/div[1]/div/a/picture/source[1]/@data-srcset")
        link_temp = dom.xpath("/html/body/div[1]/div/div/div[2]/div[4]/div[1]/div[3]/div/div/div/div[1]/div/a/@href")
    except:
        titul = "null"
        img_temp = "null"
        link_temp = "null"

    #print(titul)
    link = "https://hernazona.aktuality.sk" + link_temp[0]
    #print(link)
    img = img_temp[0]
    img = img.replace("url","")
    img = img.replace("(","")
    img = img.replace(")","")
    #print(img)

    if oldname != titul and titul != None and img != None:
        oldname = titul
        return titul,img,link
    else:
        titul = None
        img = None
        link = None
        return titul,img,link


async def my_background_task():
  oldname = "debug"
  hzname = "debug"
  while True:
    channel = client.get_channel(921514636132622386)
    titul,img,link = CheckFon()
    print(titul)
    if titul != None and titul != "null" and img != "n":
      if titul != oldname:
        oldname = titul
        embed = discord.Embed(
        title=titul,
        description=link,
        color=discord.Colour.red()
        )
        embed.set_thumbnail(url=img)

        await channel.send(embed=embed)  
        
    elif titul != None and titul != "null":
       if titul != oldname:
        oldname = titul
        embed = discord.Embed(
        title=titul,
        description=link,
        color=discord.Colour.red()
        )
        #embed.set_thumbnail(url=img)

        await channel.send(embed=embed)

    await asyncio.sleep(2)

    channel = client.get_channel(931648345800331304)
    titul,img,link = CheckHz()
    print(titul)
    if titul != None and titul != "null" and img != "n":
      if titul != hzname:
        hzname = titul
        embed = discord.Embed(
        title=titul,
        description=link,
        color=discord.Colour.green()
        )
        embed.set_thumbnail(url=img)

        await channel.send(embed=embed)  
        
    elif titul != None and titul != "null":
       if titul != hzname:
        hzname = titul
        embed = discord.Embed(
        title=titul,
        description=link,
        color=discord.Colour.green()
        )
        #embed.set_thumbnail(url=img)

        await channel.send(embed=embed)
    
    await asyncio.sleep(60)


client.run('TOKEN')