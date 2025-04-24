import discord
from scraper import Scraper
import os
from dotenv import load_dotenv

# Get the token from the environment variable
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def build_message(item):
    embed = discord.Embed(title=item['title'], description=f"Price: {item['price']}", color=0x00ff00, type="rich")
    embed.set_thumbnail(url=item['img_url'])
    embed.url = item['url']
    return embed

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!scrape'):
        scraper = Scraper()
        results = scraper.scrape()
        # await message.channel.send(results)
        embeds = []
        for result in results:
            embed = build_message(result)
            embeds.append(embed)

        await message.channel.send(embeds=embeds)

client.run(TOKEN)
