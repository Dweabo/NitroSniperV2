import discord
import datetime
import requests
import asyncio

token = "mfa.6XrQjdpoBJIAKw3oPL05jddkMot70MuBIgcjx_1GMy-CrzUWze4gr7AEoF5JCoz_gaRc5WMO1uSx1csravMu"#Replace with discord token
client = discord.Client()


@client.event
async def on_connect():
    x=1
    while True:
            await client.change_presence(activity=discord.Streaming(name="3.14", url='https://www.twitch.tv/'))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Streaming(name="3.141", url='https://www.twitch.tv/'))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Streaming(name="3.1415", url='https://www.twitch.tv/'))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Streaming(name="3.14159", url='https://www.twitch.tv/'))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Streaming(name="3.141592", url='https://www.twitch.tv/'))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Streaming(name="3.1415926", url='https://www.twitch.tv/'))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Streaming(name="3.14159265", url='https://www.twitch.tv/'))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Streaming(name="3.141592653", url='https://www.twitch.tv/'))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Streaming(name="3.1415926535", url=url='https://www.twitch.tv/'))
            await asyncio.sleep(5)
            await client.change_presence(activity=discord.Streaming(name="3.14159265359", url=url='https://www.twitch.tv/'))
            x += 1
    print("Ready")



@client.event
async def on_message(message):
    if "discord.gift/" in message.content:
        print("Found Nitro Gift")

        indexNum = message.content.find("discord.gift/")
        indexNum += 13
        giftCode = message.content[indexNum:indexNum+16]

        print("Gift Code:",giftCode)

        URL = "https://discordapp.com/api/v6/entitlements/gift-codes/" + giftCode + "/redeem"

        headers = {
            "authorization": "{}".format(token),
        }

        requestResponse = requests.post(url=URL, data="", headers=headers)

        print(f"[{datetime.datetime.now()}] Attempting to Redeem")

        if requestResponse.status_code == 200:
            print(f"[{datetime.datetime.now()}] Successfully Attempted To Redeem Nitro")
        else:
            print(f"[{datetime.datetime.now()}] Failed To Redeem Nitro")

client.run(token, bot=False)
