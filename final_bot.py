#Importing the Discord API and tools
import discord
from discord.ext import commands

#Importing random, os, requests, json, asyncio and dotenv modules for control over app
import random
import os
import requests
from dotenv import load_dotenv
import json
import asyncio

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

@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='general'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


#Setting up basic commands
@bot.command(name='fun-fact', help='Gives a random fun fact.')
async def facts(ctx, modifier='random'):
    if modifier == 'random':
        r = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
        response = discord.Embed(color=discord.Color.dark_purple())
        response.add_field(name=f"Random Fact: {r.json()['id']}", value=r.json()['text'])
        response.set_footer(text=f"Source: {r.json()['source_url']}")
        await ctx.send(embed=response)
    elif modifier == 'today':
        r = requests.get('https://uselessfacts.jsph.pl/today.json?language=en')
        response = discord.Embed(color=discord.Color.dark_purple())
        response.add_field(name=f"Today's Fun Fact:", value=r.json()['text'])
        response.set_footer(text=f"Source: {r.json()['source_url']}")
        await ctx.send(embed=response)


@bot.command(name='kanye', help='Gives a random Kanye picture and quote.')
async def kanye_quote(ctx):
    kanye_library = ['https://scstylecaster.files.wordpress.com/2015/11/kanye-west-hair.jpg', 'https://www.sohh.com/wp-content/uploads/2018/10/Kanye-West-2.jpg', 'https://pmcfootwearnews.files.wordpress.com/2019/04/kanye.jpg', 'https://dazedimg-dazedgroup.netdna-ssl.com/1080/0-0-1080-720/azure/dazed-prod/1280/1/1281206.jpg', 'https://www.charismanews.com/images/stories/2018/10/Reuters-Kanye-MAGA.jpg', 'https://thefader-res.cloudinary.com/images/w_1440,c_limit,f_auto,q_auto:eco/lno64xcmu85kyu0q9pl4/kanye-west.jpg', 'https://i.dailymail.co.uk/i/newpix/2018/09/07/19/4FD5C0B800000578-6143737-image-m-31_1536344471109.jpg', 'https://kickzandsneakerz.files.wordpress.com/2015/02/kanye_west_funny.png', 'https://www.realstreetradio.com/wp-content/uploads/2018/06/Kanye-West-Might-Have-Low-Key-Exposed-Drake039s-100K-Pusha-T-Offer-On-quotYequot-Album-ndash-1.jpg']
    r = requests.get('https://api.kanye.rest').json()
    response = discord.Embed(color=discord.Color.dark_orange())
    response.set_image(url=random.choice(kanye_library))
    response.add_field(name='Kanye Quote', value=r['quote'])
    response.set_footer(text='Source: https://api.kanye.rest')
    await asyncio.sleep(1)
    await ctx.send(embed=response)

bot.run(TOKEN)
