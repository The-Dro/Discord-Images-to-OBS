import discord
import os
import time
import re
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')
JSON_FILE_PATH = 'image_data.json'

if not TOKEN or not CHANNEL_ID:
    raise ValueError("DISCORD_TOKEN and DISCORD_CHANNEL_ID must be set in .env file")

# Create an instance of discord.Intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

# Pass intents to the discord.Client() constructor
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.channel.id == int(CHANNEL_ID):
        print(f'Message received in correct channel: {message.content}')
        print(f'Attachments: {message.attachments}')
        if message.attachments or any(re.findall(r'(http[s]?:\/\/[^\s]+(\.jpg|\.png|\.jpeg))', message.content)):
            image_url = message.attachments[0].url if message.attachments else re.findall(r'(http[s]?:\/\/[^\s]+(\.jpg|\.png|\.jpeg))', message.content)[0][0]
            try:
                # Get author information
                author_name = message.author.display_name or message.author.name
                message_timestamp = message.created_at.timestamp()
                
                # Write image data to JSON file for polling
                image_data = {
                    'url': image_url,
                    'timestamp': time.time(),
                    'author': author_name,
                    'message_timestamp': message_timestamp
                }
                with open(JSON_FILE_PATH, 'w') as file:
                    json.dump(image_data, file)
                print(f'JSON file updated with image URL: {image_url} from {author_name}')
            except Exception as e:
                print(f'Error updating files: {e}')
        else:
            print('No attachments or image links found in the message')

client.run(TOKEN)