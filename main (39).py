import discord
from discord.ext import commands

# Create a new bot object with the command prefix as '$'
bot = commands.Bot(command_prefix='$')

# Event for when the bot is ready to receive commands
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# Command to greet the user who called the command
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')

# Run the bot using your bot token from the Discord Developer Portal
bot.run('your_bot_token_here')

