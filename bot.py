import asyncio
from discord.ext import commands
import sys

bot = commands.Bot(command_prefix="kjjjjj fé pra tu <3", description='''Apenas fé meu bom.''', self_bot=True)

@bot.event
async def on_ready():
    print(f'Logged as {bot.user.name}#{bot.user.discriminator}')
    try:
        number = 0
        while True:
            channel = bot.get_channel(818226777381535754)
            await channel.send("!work")
            await asyncio.sleep(3)
            await channel.send("!deposit all")
            number += 1
            print(f'{bot.user.name} coletado {number}x.')
            await asyncio.sleep(600)
                
    except:
        print(f'Error as {bot.user.name}#{bot.user.discriminator}')
         
bot.run(sys.argv[1], bot=False)
    