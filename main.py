# https://discord.com/oauth2/authorize?client_id=1064982556002500678&permissions=8&scope=bot%20applications.commands
import discord
from discord.ext import commands

import config
from tts import TTS


intents = discord.Intents.default()
intents.message_content = True
# intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
TTSClient = TTS()

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def tts(ctx):
    await ctx.message.delete()

    file = TTSClient.synthesize(ctx)
    await ctx.send(file=discord.File(file, filename=f"{ctx.author.name}.wav"))
    TTSClient.delete_audio(file)

bot.run(config.CLIENT_TOKEN)