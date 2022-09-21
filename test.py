from tokenize import Token
import discord
import os
import asyncio
import youtube_dl
import time
import pyttsx3

from sglypa import TOKEN



client = discord.Client(intents=discord.Intents.all())
TOKEN = os.getenv("DISCORD_TOKEN")

ffmpeg_options = {'options': "-vn"}


@client.event
async def on_message(msg):
    if msg.content.startswith("?play"):
        try:
            voice_client = await msg.author.voice.channel.connect()
        except:
            print("error")

        try:
            string = "test"
            engine = pyttsx3.init()
            engine.save_to_file(string, f'speechers/voice.mp3')
            engine.runAndWait()
            voice_client.play(discord.FFmpegPCMAudio(f'speechers/voice.mp3', **ffmpeg_options))
            if voice_client and voice_client.is_connected():
                await asyncio.sleep(5)
                await voice_client.disconnect()
        except Exception as err:
            print(err)



client.run(TOKEN)