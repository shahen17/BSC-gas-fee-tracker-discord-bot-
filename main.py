import discord
import requests
import json
import http.client

from config import *


client = discord.Client()

def gas_track():
    my_api = "https://api.bscscan.com/api?module=gastracker&action=gasoracle&apikey=apikeyhere"
    response = requests.get(f'{my_api}')
    result = response.json()['result']
    result_format = json.dumps(result, indent=2)
    index1 = result_format.index('SafeGasPrice')
    index2 = result_format.index('ProposeGasPrice')
    index3 = result_format.index('FastGasPrice')
    index4 = result_format.index('UsdPrice')
    stat = result_format[index1:index2]
    stat2 = result_format[index4:200]
    statlist1 = []
    statlist2 = []
    statlist1.append(stat)
    statlist2.append(stat2)
    for i in statlist1:
        format_a = i.replace('"', '').replace(':', '').replace(',', '')
    for i in statlist2:
        format_b = i.replace('"', '').replace(':', '').replace(',', '').replace('}', '')
    return format_a

def bsc_price():
    my_api = "https://api.bscscan.com/api?module=gastracker&action=gasoracle&apikey=apikeyhere"
    response = requests.get(f'{my_api}')
    result = response.json()['result']
    result_format = json.dumps(result, indent=2)
    index1 = result_format.index('SafeGasPrice')
    index2 = result_format.index('ProposeGasPrice')
    index3 = result_format.index('FastGasPrice')
    index4 = result_format.index('UsdPrice')
    stat = result_format[index1:index2]
    stat2 = result_format[index4:200]
    statlist1 = []
    statlist2 = []
    statlist1.append(stat)
    statlist2.append(stat2)
    for i in statlist1:
        format_a = i.replace('"', '').replace(':', '').replace(',', '')
    for i in statlist2:
        format_b = i.replace('"', '').replace(':', '').replace(',', '').replace('}', '')
    return format_b

@client.event
async def on_ready():
    print('Chicken bot is logged IN --BY SHAHEN--{0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$gas'):
        avc = discord.Embed(
            colour=discord.Colour.blue(),
            title="LIVE-QUOTES",
            description=""

        )
        avc.add_field(
            name="Gas fee in (USD)",
            value=gas_track(),
            inline=False,

        )
        await message.channel.send(embed=avc)


    if message.content.startswith('$bnb'):
        avc = discord.Embed(
            colour=discord.Colour.blue(),
            title="LIVE-QUOTES",
            description=""

        )
        avc.add_field(
            name="BNB Price",
            value=bsc_price(),
            inline=False,

        )
        await message.channel.send(embed=avc)


my_secret = Token
client.run(my_secret)





