import discord, os, aiohttp, io
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("JPEGMAFIA_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print("daaaang peggy")

@client.event
async def on_message(message):
        if len(message.attachments) != 0:
            for attachment in message.attachments:
                if attachment.filename.endswith("jpglarge") or attachment.filename.endswith("jpeglarge"):
                    async with aiohttp.ClientSession() as session:
                        async with session.get(attachment.url) as resp:
                            var = await resp.read()
                            await message.channel.trigger_typing()
                            await message.channel.send(file=discord.File(fp=io.BytesIO(var), filename="conversion.jpg"))
                            return

client.run(TOKEN)