import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os
import threading
import asyncio
from keep_alive import keep_alive


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
OWNER_ID = 1194983217086857292

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
  
@bot.event
async def on_ready():
    print(f"Bot aktif sebagai {bot.user}")
    try:
        await bot.tree.sync()
        print("Slash command berhasil disinkronkan.")
    except Exception as e:
        print(f"Gagal sync slash command: {e}")

@bot.tree.command(name="sync", description="Sync semua slash command")
async def sync_command(interaction: discord.Interaction):
    if interaction.user.id != OWNER_ID:
        return await interaction.response.send_message("Kamu tidak punya izin.", ephemeral=True)

    await interaction.response.defer(thinking=True)
    try:
        synced = await bot.tree.sync(guild=interaction.guild)
        await interaction.followup.send(f"{len(synced)} command berhasil disinkronkan!", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f"Gagal sync: {e}", ephemeral=True)
async def load_extensions():
    extensions = [
        "cogs.info",
        "cogs.respon",
        "cogs.moderation",
        "cogs.welcome",
        "cogs.say",
        "cogs.serverinfo",
    ]

    for ext in extensions:
        try:
            await bot.load_extension(ext)
            print(f"Berhasil load: {ext}")
        except Exception as e:
            print(f"[Gagal load] {ext} → {e}")

def start_web():
    keep_alive()

web_thread = threading.Thread(target=start_web)
web_thread.start()

async def main():
    await load_extensions()
    if TOKEN:
        await bot.start(TOKEN)
    else:
        print("TOKEN tidak ditemukan di .env!")
asyncio.run(main())
