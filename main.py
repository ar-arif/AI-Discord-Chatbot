import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
from prsaw import RandomStuff

rs = RandomStuff(async_mode=True)

token = os.getenv('token')

client = commands.Bot(command_prefix='>')

@client.event
async def on_ready():
    os.system('clear')
    print(f'{client.user.name} is ready to go.')


@client.event
async def on_message(message):
  if client.user == message.author:
    return
  user_input = message.content
  response = await rs.get_ai_response(user_input)
  await message.reply(response)
  await client.process_commands(message)
  print(user_input)

@client.command()
async def ping(ctx):
    lat = str(client.latency)[3] + str(client.latency)[4]
    await ctx.send(f'pong {lat}ms')

keep_alive()
client.run(token)