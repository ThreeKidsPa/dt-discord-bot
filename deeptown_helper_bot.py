import discord
from discord.ext import commands
import random
import logging

import guildevent

logging.basicConfig(level=logging.INFO)

description = '''I'm a bot to make it easy for you to keep track of your guild event donations.
There are a number things you can do.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.group(pass_context=True)
async def guildEvent(ctx):
    """Commands for managing guild events"""
    if ctx.invoked_subcommand is None:
        await bot.say("you need to give me a sub command!")

@guildEvent.command(name='start', pass_context=True)
async def _start(ctx):
    """Start a new guild event, removing the old one and any data with it"""
    await bot.say("starting an event")

@guildEvent.command(name='donations', pass_context=True)
async def _donations(ctx):
    """Display a donation summary report"""
    await bot.say("preparing guild event summary report")

@guildEvent.command(name='info', pass_context=True)
async def _info(ctx):
    """Display current event information"""
    await bot.say("displaying information for current guild event")

@guildEvent.command(name='complete', pass_context=True)
async def _complete(ctx):
    """Mark an event as finished"""
    await bot.say("marking an event as over")

@bot.group(description = 'commands for donating materials in support of a guild event', pass_context=True)
async def donate(ctx, material : str, amount : int):
    """Donate materials to a guild event"""
    await bot.say("I'm dealing with a donation command")

@donate.command(name='show', pass_context=True)
async def _show(ctx, menber : discord.Member):
    await bot.say("Showing donation details for member")

@donate.command(name='remove', pass_cotext=True)
async def _remove(ctx, donationId : int):
    await bot.say("removing donation id")

bot.run('NDA5Mzg3NzA1Mjg2MzkzODU2.DVd8Xg.x8ysZuFad6myhPHbd1fU3YbHUeA')