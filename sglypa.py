import discord
from discord.ext import commands
import random
import requests
import re
from typing import Optional, Union
from cloudscraper import CloudScraper
from requests import Session
from itertools import groupby
from discord.utils import get
from discord import FFmpegPCMAudio
import pyttsx3
import asyncio
import os


bot = commands.Bot(command_prefix="+",intents=discord.Intents.all())
bot.remove_command("help")
TOKEN = os.getenv("DISCORD_TOKEN")
user_messages = []

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Разработчик бота cloudy ы :)"))
    

@bot.listen()
async def on_message(ctx):
    id_server =  f"{ctx.guild.id}"
    with open(f'servers/{id_server}.txt', 'a' ,encoding='utf-8') as f:
              if ctx.author != bot.user:
                f.write(f'{ctx.content}')
                f.write('\n')

    with open(f'servers/{id_server}.txt',"r",encoding='utf-8') as f:
            lines = f.readlines()
            random_line = random.choice(lines)
            pattern = re.compile(re.escape('+'))
            with open(f'servers/{id_server}.txt', 'w',encoding='utf-8') as f:
                for line in lines:
                    result = pattern.search(line)
                    if result is None:
                        f.write(line)
                f.close()
    with open(f'servers/{id_server}.txt',"r",encoding='utf-8') as f:
            lines = f.readlines()
            random_line = random.choice(lines)
            pattern = re.compile(re.escape('/'))
            with open(f'servers/{id_server}.txt', 'w',encoding='utf-8') as f:
                for line in lines:
                    result = pattern.search(line)
                    if result is None:
                        f.write(line)
                f.close()

    with open(f'servers/{id_server}.txt',"r",encoding='utf-8') as f:
            lines = f.readlines()
            random_line = random.choice(lines)
            pattern = re.compile(re.escape('@'))
            with open(f'servers/{id_server}.txt', 'w',encoding='utf-8') as f:
                for line in lines:
                    result = pattern.search(line)
                    if result is None:
                        f.write(line)
                f.close()
    
    with open(f'servers/{id_server}.txt',"r",encoding='utf-8') as f:
            lines = f.readlines()
            random_line = random.choice(lines)
            pattern = re.compile(re.escape('play'))
            with open(f'servers/{id_server}.txt', 'w',encoding='utf-8') as f:
                for line in lines:
                    result = pattern.search(line)
                    if result is None:
                        f.write(line)
                f.close()
    
    with open(f'servers/{id_server}.txt',"r",encoding='utf-8') as f:
            lines = f.readlines()
            random_line = random.choice(lines)
            pattern = re.compile(re.escape('<'))
            with open(f'servers/{id_server}.txt', 'w',encoding='utf-8') as f:
                for line in lines:
                    result = pattern.search(line)
                    if result is None:
                        f.write(line)
                f.close()
                
    uniqlines = set(open(f'servers/{id_server}.txt','r', encoding='utf-8').readlines())
    gotovo = open(f'servers/{id_server}.txt','w', encoding='utf-8').writelines(set(uniqlines))

    with open(f'servers/{id_server}.txt') as f:
     lines = f.readlines()
     non_empty_lines = (line for line in lines if not line.isspace())
     with open(f'servers/{id_server}.txt', 'w') as n_f:
         n_f.writelines(non_empty_lines)

    chance = random.randint(0,3)
    if len(user_messages) == len(user_messages)+chance:
            await ctx.reply(random_line)     

color = "#52f464"
sixteenIntegerHex = int(color.replace("#", ""), 16)
readableHex = int(hex(sixteenIntegerHex), 0)

@bot.command()
async def help(ctx):
    
    embed = discord.Embed(title=f"Помощь по командам бота", 
    color=readableHex).add_field(name="Сгенерировать мем",value="``+sgm``").add_field(
    name="Сгенерировать слово",value="``+sg``").add_field(name="Набалаболить слово",
    value="``+sgb``").add_field(name="Зайду в войс (ПОКА НЕДОСТУПНО) :(",
    value="``+sgv``")
    await ctx.reply(embed=embed)

@bot.command()
async def sgm(ctx):
    id_server =  f"{ctx.guild.id}"
    with open(f'servers/{id_server}.txt',"r",encoding='utf-8') as f:
            lines = f.readlines()
            random_line = random.choice(lines)
            f.close()

    username = 'dlyabota'
    password = '2YfjjyJAr3yL8r9'
    userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0"

    data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
    images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]
    URL = 'https://api.imgflip.com/caption_image'
    text0 = random.choice(lines)
    text1 = random.choice(lines)
    data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
    images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]

    params = {
    'username':username,
    'password':password,
    'template_id':images[random.randint(0,100)]['id'],
    'text0':text0,
    'text1':text1
    }
    response = requests.request('POST',URL,params=params).json()
    await ctx.reply(response["data"]["page_url"])

@bot.command()
async def sg(ctx):
    id_server =  f"servers/{ctx.guild.id}"
    with open(f'{id_server}.txt',"r",encoding='utf-8') as f:
            lines = f.readlines()
            random_line = random.choice(lines)
            print(random_line)
            f.close()
    await ctx.reply(random_line)


def fetch(query: str, intro: int, session: CloudScraper) -> str:
    with session.post(
        "https://yandex.ru/lab/api/yalm/text3",
        json={"query": query, "intro": intro, "filter": 1},
    ) as resp:
        r = resp.json()
    return f"{r['query']}{r['text']}"


def balaboba(
    query: str,
    *,
    intro: int = 0,
    session: Optional[Union[CloudScraper, Session]] = None,
) -> str:
    """Отправка запроса Яндекс Балабобе.
    Args:
        query (str): Текст для Балабобы.
        intro (int, optional): Вариант стилизации.
            0 - Без стиля. По умолчанию.
            1 - Теории заговора.
            2 - ТВ-репортажи.
            3 - Тосты.
            4 - Пацанские цитаты.
            5 - Рекламные слоганы.
            6 - Короткие истории.
            7 - Подписи в Instagram.
            8 - Короче, Википедия.
            9 - Синопсисы фильмов.
            10 - Гороскоп.
            11 - Народные мудрости.
            18 - Новый Европейский Театр.
        session (Optional[Union[CloudScraper, Session]], optional):
            По умолчанию None.
    Returns:
        str: Ответ Балабобы.
    Examples:
        >>> response = balaboba("Привет")
        >>> response = balaboba("Привет", intro=11)
        >>> from cloudscraper import create_scraper
        ... with create_scraper() as session:
        ...     response = balaboba("Привет", session=session)
    """
    if isinstance(session, CloudScraper):
        return fetch(query, intro, session)
    if isinstance(session, Session):
        with CloudScraper.create_scraper(session) as s:
            return fetch(query, intro, s)
    with CloudScraper.create_scraper() as scraper:
        return fetch(query, intro, scraper)

@bot.command()
async def sgb(ctx):
    id_server =  f"{ctx.guild.id}"
    with open(f'servers/{id_server}.txt',"r",encoding='utf-8') as f:
            lines = f.readlines()
            random_line = random.choice(lines)
            f.close()
    response = balaboba(random_line, intro=0)
    await ctx.reply(response)


# @bot.command()
# async def sgv(ctx):
#     id_server =  f"servers/{ctx.guild.id}"
#     with open(f'{id_server}.txt',"r",encoding='utf-8') as f:
#             lines = f.readlines()
#             random_line = random.choice(lines)
#             string = random_line
#             engine = pyttsx3.init()
#             engine.save_to_file(string, f'speechers/voice.mp3')
#             engine.runAndWait()
#             f.close()
#     channel = ctx.message.author.voice.channel
#     voice = get(bot.voice_clients, guild = ctx.guild)
#     if voice and voice.is_connected():
#         await voice.move_to(channel)
#     else:
#         await asyncio.sleep(2)
#         voice = await channel.connect()
#         voice.play(discord.FFmpegPCMAudio(executable="audio/ffmpeg.exe",source = 'speechers/voice.mp3'))
#         if voice and voice.is_connected():
#             await asyncio.sleep(5)
#             await voice.disconnect()

bot.run(TOKEN)
