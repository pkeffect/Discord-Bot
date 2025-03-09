import json
import logging
import os
import platform
import random
import sys
import aiosqlite
import discord
from discord.ext import commands, tasks
from discord.ext.commands import Context
from dotenv import load_dotenv

load_dotenv()

# This should be in your .env
TOKEN = os.getenv("DISCORD_TOKEN")

# Define intents
intents = discord.Intents.all()
intents.bans = True
intents.dm_messages = True
intents.dm_reactions = True
intents.dm_typing = True
intents.emojis = True
intents.emojis_and_stickers = True
intents.guild_messages = True
intents.guild_reactions = True
intents.guild_scheduled_events = True
intents.guild_typing = True
intents.guilds = True
intents.integrations = True
intents.invites = True
intents.messages = True # `message_content` is required to get the content of the messages
intents.reactions = True
intents.typing = True
intents.voice_states = True
intents.webhooks = True
intents.members = True
intents.message_content = True
intents.presences = True

# LOGGING: Add later

# Set up the bot with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event that triggers when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in to Discord as {bot.user.name} (ID: {bot.user.id})')
    print('------ Congrats! ------')

# Command to respond to
@bot.command()
async def hello(ctx):
    await ctx.send('Hello! 👋 How can I assist you today?')

# Command to ping the bot
@bot.command()
async def ping(ctx):
    await ctx.send('Pong! 🏓')

# Run the bot
bot.run(os.getenv("DISCORD_TOKEN"))