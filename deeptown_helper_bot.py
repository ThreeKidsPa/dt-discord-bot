import discord
from discord.ext import commands
import random
import logging

logging.basicConfig(level=logging.INFO)

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(description = 'For donating materials in support of a guild event')
async def donate():
    """Donate materials to a guild event"""
    await bot.say("I'm dealing with a donation command")

@bot.command(description = 'Manages the current guild event')
async def guildEvent(subcmd : str)
    """Use this command to establish a new guild event, or get information about the current event"""
    await bot.say("Processing a guildEvent request")

@bot.command()
async def showDonations()
    """Command to show donations for the current event"""
    await bot.say("show current donations")

@bot.command()
async def retractDonation()
    """Command to retract a donation submitted in error"""
    await bot.say("retracting a donation")

@bot.command()
async def showEventSummary()
    """Summarize total contributions by each member for a guild event"""
    await bot.say("guild event summary")



@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')

bot.run('NDA5Mzg3NzA1Mjg2MzkzODU2.DVd8Xg.x8ysZuFad6myhPHbd1fU3YbHUeA')