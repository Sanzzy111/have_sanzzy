import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os
import threading
import asyncio
from keep_alive import keep_alive

# Load token dan konfigurasi lainnya
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
OWNER_ID = 1194983217086857292
GUILD_ID = 1360236512188567683  # Ganti ini ke ID server kamu!

# Inisialisasi intents dan bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Event on_ready
@bot.event
async def on_ready():
    print(f"Bot aktif sebagai {bot.user}")
    try:
        guild = discord.Object(id=GUILD_ID)  # Sync hanya untuk 1 guild
        await bot.tree.sync(guild=guild)
        print("✅ Slash command berhasil disinkronkan ke development server.")
    except Exception as e:
        print(f"❌ Gagal sync slash command: {e}")

# Command untuk sync slash command
@bot.tree.command(name="sync", description="Sync semua slash command")
async def sync_command(interaction: discord.Interaction):
    if interaction.user.id != OWNER_ID:
        return await interaction.response.send_message("Kamu tidak punya izin.", ephemeral=True)

    await interaction.response.defer(thinking=True)
    try:
        synced = await bot.tree.sync(guild=interaction.guild)
        await interaction.followup.send(f"✅ {len(synced)} command berhasil disinkronkan ke server ini!", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f"❌ Gagal sync: {e}", ephemeral=True)

# Fungsi untuk load semua extension
async def load_extensions():
    extensions = [
        "cogs.info",
        "cogs.respon",
        "cogs.moderation",
        "cogs.welcome",
        "cogs.say",
        "cogs.serverinfo",
        "cogs.lock",
        "cogs.buttons",

    ]

    for ext in extensions:
        try:
            await bot.load_extension(ext)
            print(f"Berhasil load: {ext}")
        except Exception as e:
            print(f"[Gagal load] {ext} → {e}")

# Thread untuk keep-alive (jika dibutuhkan)
def start_web():
    keep_alive()

# Memulai thread untuk keep-alive
web_thread = threading.Thread(target=start_web)
web_thread.start()

# Fungsi utama untuk menjalankan bot
async def main():
    await load_extensions()  # Load semua extension terlebih dahulu
    if TOKEN:
        await bot.start(TOKEN)
    else:
        print("❌ TOKEN tidak ditemukan di .env!")

# Memulai event loop bot
asyncio.run(main())
