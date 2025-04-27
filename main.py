import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
from dotenv import load_dotenv
import asyncio

# Load environment variables from .env
load_dotenv()

# Set up intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

# Initialize bot with command prefix and intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Event when bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        GUILD_ID = 1360236512188567683  # <-- Ganti dengan ID server kamu
        guild = discord.Object(id=GUILD_ID)
        # Sync commands to specific guild (server)
        synced = await bot.tree.sync(guild=guild)
        print(f"Synced {len(synced)} commands to guild {GUILD_ID}.")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# Function to load all cogs in 'cogs/' folder
async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f"Loaded {filename}")
            except Exception as e:
                print(f"Failed to load {filename}: {e}")

# Start the server (keep_alive)
keep_alive()

# Main function to run the bot
async def main():
    await load_extensions()  # Ensure all cogs are loaded before starting the bot
    await bot.start(os.getenv('DISCORD_TOKEN'))

# Run the bot using asyncio
asyncio.run(main())
