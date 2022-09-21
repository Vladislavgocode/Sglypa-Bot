import discord
from discord.ext import commands
import youtube_dl
import os
import asyncio
import random
import pyttsx3
from discord.utils import get


bot = commands.Bot(command_prefix="+",intents=discord.Intents.all())
bot.remove_command("help")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.command()
async def sgv(ctx):
    id_server =  f"servers/{ctx.guild.id}"
    # with open(f'{id_server}.txt',"r",encoding='utf-8') as f:
    #         lines = f.readlines()
    #         random_line = random.choice(lines)
    string = "test"
    engine = pyttsx3.init()
    engine.save_to_file(string, f'speechers/voice.mp3')
    engine.runAndWait()
    # f.close()


    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        await asyncio.sleep(2)
        voice = await channel.connect()
        voice.play(discord.FFmpegPCMAudio(executable="audio/ffmpeg.exe",source = 'speechers/voice.mp3'))
        if voice and voice.is_connected():
            await asyncio.sleep(5)
            await voice.disconnect()

bot.run(TOKEN)