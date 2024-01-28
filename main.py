import discord
import time
import download
import fullscreen
import facecam
import uploadscript
import random
import testclip
import os
from discord.ext import commands
from discord import File

import cv2
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

intents = discord.Intents.default()
intents.messages = True
# Create an instance of the bot
bot = commands.Bot(command_prefix='/')

# Event to run when the bot is ready
@bot.event
async def on_ready():
    file_path0 = os.path.join(os.getcwd(), ".mp4")
    file_path1 = os.path.join(os.getcwd(), "v.mp4")
    file_path2 = os.path.join(os.getcwd(), "clip.mp4")
    file_path3 = os.path.join(os.getcwd(), "cliptest.mp4")

    files_to_remove = [file_path0, file_path2, file_path3]

    for file in files_to_remove:
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f"{file} has been destroyed.")
            except Exception as e:
                print(f"An error occurred while removing {file}: {e}")
        else:
            print(f"The file {file} does not exist.")

    print(f'Bot is ready! Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore messages from the bot itself

    print(f"Author Name: {message.author.name}")

    # Check if the message content is a valid URL
    if message.author.name == "bymikiii":
        if any(url in message.content for url in ('http://', 'https://')):
            # Call the wrapper function with the appropriate context
                await upload(message.author, message.content)
        elif message.attachments:
            # Check if the message contains attachments (files)
                await save_attachments(message.attachments, message)
        elif message.content not in ["1", "2", "3"]:
            # If none of the above conditions are met, send a default message
            await message.channel.send(f"daj pokoj") #{message.author.name} 

    await bot.process_commands(message)

async def save_attachments(attachments, message):
    # Save each attachment to the current directory
    for attachment in attachments:
        filename = "clip.mp4"
        file_path = os.path.join(os.getcwd(), filename)

        # Download and save the file
        await attachment.save(file_path)

        print(f"File saved: {file_path}")

        await upload(message.author, "nourl")

async def upload(ctx, url):
    username = ctx.name
    file_path2 = os.path.join(os.getcwd(), "clip.mp4")

    if url != "nourl":
        response = await ctx.send(download.download_clip(url, 'clip'))
    
    # response2 = await ctx.send('Creating facecam template...')
    # testclip.facecam('clip')

    # await ctx.send(file=File("cliptest.mp4"))
    # test = await ctx.send('Is it good? (1 - yes, 2 - fullscreen, 3 - remove)')
    
    # finaloption = await bot.wait_for('message', check=lambda message: message.author == ctx)
    
    # if '1' in finaloption.content:
    #     final = await ctx.send('Creating facecam clip...')
    #     facecam.edit('clip')
    #     await final.edit(content='Uploading...')
    #     # await final.edit(content=uploadscript.upload())
    #     await ctx.send(file=File("v.mp4"))
    # elif '2' in finaloption.content:
    #     final = await ctx.send('Creating fullscreen clip...')
    #     fullscreen.edit('clip')
    #     await final.edit(content='Uploading...')
    #     # await final.edit(content=uploadscript.upload())
    #     await ctx.send(file=File("v.mp4"))

    # else:
    #     await ctx.send('Clip wasnt uploaded!')

    await ctx.send('Creating fullscreen clip...')
    fullscreen.edit('clip')
    await ctx.send(file=File("v.mp4"))
    
    final = await ctx.send('Uploading...')
    await final.edit(content=uploadscript.upload())

# Run the bot
bot.run('')

