import discord
import os
import requests
import json

client = discord.Client()

def get_message():
  response = requests.get("")

@client.event
async def on_ready():
  print('We have logged in a {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
      return

  if message.content.startswith('$hello'):
    await message.channel.send('Inshallah BOOM BOOM')
  if message.content.startswith('$bolna lawde'):
    await message.channel.send('Inshallah BOOM BOOM')
  if message.content.startswith('$kaha se hai lawde?'):
    await message.channel.send('Teri maa jis randi khane mai hai uske samne ek tere bhadve baap chowkidari karta hai usko puch lio, bhai hai apna')
  if message.content.startswith('$kaha se hai lawde mystic'):
    await message.channel.send('Chup kar ja lavde, HC Verma gand mai dalke tere baap ke lavde pe jhulli le lunga.')   
     

client.run(os.getenv('TOKEN')) 