import discord
import os
from discord.ext import commands
import asyncio
import time
import pyttsx3

from sglypa import TOKEN

import ctypes
import ctypes.util

find_opus = ctypes.util.find_library('opus')
discord.opus.load_opus(find_opus)


bot = commands.Bot(command_prefix="+",intents=discord.Intents.all())
bot.remove_command("help")
TOKEN = os.getenv("DISCORD_TOKEN")

ffmpeg_options = {'options': "-vn"}


@bot.command()
async def sgv(ctx):
    voice_client = await ctx.author.voice.channel.connect()
    string = "test"
    engine = pyttsx3.init()
    engine.save_to_file(string, '/voice.mp3')
    engine.runAndWait()
    voice_client.play(discord.FFmpegPCMAudio('/voice.mp3', **ffmpeg_options))
    if voice_client and voice_client.is_connected():
        await asyncio.sleep(5)
        await voice_client.disconnect()




bot.run(TOKEN)