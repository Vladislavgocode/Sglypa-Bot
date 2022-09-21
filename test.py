# from tokenize import Token
# import discord
# import os
# from discord.ext import commands
# import asyncio
# import time
# import pyttsx3
# import subprocess
# import espeak

# bot = commands.Bot(command_prefix="+",intents=discord.Intents.all())
# bot.remove_command("help")
# # TOKEN = os.getenv("DISCORD_TOKEN")

# ffmpeg_options = {'options': "-vn"}

# @bot.event
# async def on_ready():
#     await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Разработчик бота cloudy ы :)"))



# # @bot.command()
# # async def sgv(ctx):
# #     voice_client = await ctx.author.voice.channel.connect()
# #     string = "test"
# #     engine = pyttsx3.init()
# #     engine.save_to_file(string, f'speechers/voice.mp3')
# #     engine.runAndWait()
# #     voice_client.play(discord.FFmpegPCMAudio(f'./speechers/voice.mp3', **ffmpeg_options))
# #     if voice_client and voice_client.is_connected():
# #         await asyncio.sleep(5)
# #         await voice_client.disconnect()

# espeak.init()
# speaker = espeak.Espeak()




# bot.run(Token)