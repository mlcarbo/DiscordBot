#Importing the Discord API and tools
import discord
from discord.ext import commands

#Importing random, os, requests, and dotenv modules for control over app
import random
import os
import requests
from dotenv import load_dotenv
import json

#Setting up global variable and initializing the bot instance with prefix
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')

#Setting up the command line notifications
@bot.event
async def on_ready():
    print(f'{bot.user.name} has been deployed!')

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandeled message: {args[0]}\n')
            print('Error Handled!')
        else:
            raise

#Setting up basic commands
@bot.command(name='fun-fact')
async def facts(ctx, modifier='random'):
    if modifier == 'random':
        r = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
        response = discord.Embed(decription='Fun Fact', color=discord.Color.dark_purple())
        response.add_field(name=f"Random Fact: {r.json()['id']}", value=r.json()['text'])
        response.set_footer(text=f"Source: {r.json()['source_url']}")
        await ctx.send(embed=response)

bot.run(TOKEN)
