import discord
from discord.ext import commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=":", intents=intents)
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def  on_member_join(member):
    channel = bot.get_channel(800648407236345866)
    #print(f'{member} joins!')
    await channel.send(f'{member} join!')

@bot.event
async def  on_member_remove(member):
    channel = bot.get_channel(800648419848617994)
    #print(f'{member} leave!')
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')


bot.run('ODAwNTUyNzQyODk1NzQ3MTIz.YATy1w.NAjfIJPIGD_feZwH2Vkbwm7I70M')


