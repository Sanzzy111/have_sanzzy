import discord
from discord.ext import commands

class MentionResponse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return  # Biar bot gak bales sesama bot
        
        if self.bot.user in message.mentions:
            await message.channel.send(f"Halo {message.author.mention}!, ada yang bisa aku bantu?")

async def setup(bot):
    await bot.add_cog(MentionResponse(bot))
