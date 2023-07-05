import discord
import time
import request_upload
from discord.ext import commands

# Create an instance of the bot
bot = commands.Bot(command_prefix='/')

# Event to run when the bot is ready
@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user}')

# Command example
@bot.command()
async def upload(ctx, video_style, url):
    response = await ctx.reply(f'Uploading...')
    request_upload.request_upload(url, video_style)

# Run the bot
bot.run('')