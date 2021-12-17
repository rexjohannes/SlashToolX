import os
import discord
import requests
from discord_slash import SlashCommand

bot = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

rexapi = "https://api.rexum.space"

@bot.event
async def on_ready():
  print('Logged in as')
  print(bot.user.name)
  print(bot.user.id)
  print(f"https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&scope=applications.commands")


@slash.slash(name="invite", description="Sends you SlashToolX Invite Url.")
async def _invite(ctx):
  embed = discord.Embed(title="Invite", description=f"https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&scope=applications.commands", color=discord.Colour.random())
  await ctx.send(embeds=[embed])

@slash.slash(name="joke", description="Sends you funny Jokes.")
async def _joke(ctx):
  r = requests.get(rexapi + "/joke/en/" + os.getenv("REXAPI"))
  embed = discord.Embed(title="Joke", description=r.text, color=discord.Colour.random())
  await ctx.send(embeds=[embed])

@slash.slash(name="dog", description="Sends you cute Dog images.")
async def _dog(ctx):
  r = requests.get(rexapi + "/img/dog/" + os.getenv("REXAPI"))
  embed = discord.Embed(title="Dog", color=discord.Colour.random())
  embed.set_image(url=r.text)
  await ctx.send(embeds=[embed])

@slash.slash(name="cat", description="Sends you cute Cat images.")
async def _cat(ctx):
  r = requests.get(rexapi + "/img/cat/" + os.getenv("REXAPI"))
  embed = discord.Embed(title="Cat", color=discord.Colour.random())
  embed.set_image(url=r.text)
  await ctx.send(embeds=[embed])

@slash.slash(name="otter", description="Sends you cute Otter images.")
async def _otter(ctx):
  r = requests.get(rexapi + "/img/otter/" + os.getenv("REXAPI"))
  embed = discord.Embed(title="Otter", color=discord.Colour.random())
  embed.set_image(url=r.text)
  await ctx.send(embeds=[embed])

@slash.slash(name="squirrel", description="Sends you cute Squirrel images.")
async def _squirrel(ctx):
  r = requests.get(rexapi + "/img/squirrel/" + os.getenv("REXAPI"))
  embed = discord.Embed(title="Squirrel", color=discord.Colour.random())
  embed.set_image(url=r.text)
  await ctx.send(embeds=[embed])

@slash.slash(name="koala", description="Sends you cute Koala images.")
async def _koala(ctx):
  r = requests.get(rexapi + "/img/koala/" + os.getenv("REXAPI"))
  embed = discord.Embed(title="Koala", color=discord.Colour.random())
  embed.set_image(url=r.text)
  await ctx.send(embeds=[embed])

@slash.slash(name="panda", description="Sends you cute Panda images.")
async def _panda(ctx):
  r = requests.get(rexapi + "/img/panda/" + os.getenv("REXAPI"))
  embed = discord.Embed(title="Panda", color=discord.Colour.random())
  embed.set_image(url=r.text)
  await ctx.send(embeds=[embed])

@slash.slash(name="fox", description="Sends you cute Fox images.")
async def _fox(ctx):
  r = requests.get(rexapi + "/img/fox/" + os.getenv("REXAPI"))
  embed = discord.Embed(title="Fox", color=discord.Colour.random())
  embed.set_image(url=r.text)
  await ctx.send(embeds=[embed])

@slash.slash(name="redpanda", description="Sends you cute Red panda images.")
async def _redpanda(ctx):
  r = requests.get(rexapi + "/img/red_panda/" + os.getenv("REXAPI"))
  embed = discord.Embed(title="Red Panda", color=discord.Colour.random())
  embed.set_image(url=r.text)
  await ctx.send(embeds=[embed])

@slash.slash(name="cow", description="Sends you cute Cow images.")
async def _cow(ctx):
  r = requests.get(rexapi + "/img/cow/" + os.getenv("REXAPI"))
  embed = discord.Embed(title="Cow", color=discord.Colour.random())
  embed.set_image(url=r.text)
  await ctx.send(embeds=[embed])

@slash.slash(name="meme", description="Sends you funny Memes.")
async def _meme(ctx):
  r = requests.get(rexapi + "/meme/" + os.getenv("REXAPI"))
  embed = discord.Embed(title="Meme", color=discord.Colour.random())
  embed.set_image(url=r.text)
  await ctx.send(embeds=[embed])

bot.run(os.getenv("TOKEN"))