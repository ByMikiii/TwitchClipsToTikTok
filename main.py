import discord
import time
import download
import fullscreen
import facecam
import uploadscript
import random
import os
from discord.ext import commands
from discord import File

import cv2
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip


# Create an instance of the bot
bot = commands.Bot(command_prefix='/')

# Event to run when the bot is ready
@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user}')

# Command example
@bot.command()
async def upload(ctx, url):
    member = ctx.author
    
    response = await ctx.reply(download.main('clip', url))
    await response.edit(content='Choose a video style. (1- facecam, 2- fullscreen)')
    option = await bot.wait_for('message', check=lambda message: message.author == member)
    
    if '1' in option.content:
        response2 = await ctx.reply(content='Creating facecam template...')
        facecam.edit('clip')
    else:
        response2 = await ctx.reply(content='Creating fullscreen template...')
        fullscreen.edit('clip')

    await ctx.send(file=File("cliptest.mp4"))
    test = await ctx.send('Is it good? (1 - yes, 2 - no)')
    
    finaloption = await bot.wait_for('message', check=lambda message: message.author == member)
    
    if '1' in finaloption.content:
        final = await ctx.send('Uploading...')
        await final.edit(content=uploadscript.upload())
    else:
        await ctx.send('Clip wasnt uploaded!')

# Run the bot
bot.run('')