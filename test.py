import discord
import os
import asyncio
import youtube_dl
import time
import pyttsx3



client = discord.Client(intents=discord.Intents.all())


ffmpeg_options = {'options': "-vn"}


@client.event
async def on_message(msg):
    if msg.content.startswith("?play"):

        try:
            voice_client = await msg.author.voice.channel.connect()
            # voice_clients[voice_client.guild.id] = voice_client
        except:
            print("error")

        try:
            # url = msg.content.split()[1]
            string = "test"
            engine = pyttsx3.init()
            engine.save_to_file(string, f'speechers/voice.mp3')
            engine.runAndWait()
            # f.close()
            voice_client.play(discord.FFmpegPCMAudio(f'speechers/voice.mp3', **ffmpeg_options))
            if voice_client and voice_client.is_connected():
                await asyncio.sleep(5)
                await voice_client.disconnect()

        except Exception as err:
            print(err)



client.run("MTAxNTU0NDgwNjYzMTU1OTIyMg.GMCB6O.uFzYjbC3INP0-sEoe2uvfeGF_bmlfNfocT-t-g")