import discord
import os
import asyncio
import youtube_dl
import time

TOKEN = os.getenv("DISCORD_TOKEN")
bot = discord.bot(intents=discord.Intents.all())
voice_bots = {}

yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options = {'options': "-vn"}


@bot.event
async def on_message(msg):
    if msg.content.startswith("?play"):

        try:
            voice_bot = await msg.author.voice.channel.connect()
            voice_bots[voice_bot.guild.id] = voice_bot
        except:
            print("error")

        try:
            url = msg.content.split()[1]

            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

            song = data['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options)

            voice_bots[msg.guild.id].play(player)

        except Exception as err:
            print(err)


    if msg.content.startswith("?pause"):
        try:
            voice_bots[msg.guild.id].pause()
        except Exception as err:
            print(err)

    # This resumes the current song playing if it's been paused
    if msg.content.startswith("?resume"):
        try:
            voice_bots[msg.guild.id].resume()
        except Exception as err:
            print(err)

    # This stops the current playing song
    if msg.content.startswith("?stop"):
        try:
            voice_bots[msg.guild.id].stop()
            await voice_bots[msg.guild.id].disconnect()
        except Exception as err:
            print(err)

bot.run(TOKEN)