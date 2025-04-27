import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="info", description="Show aesthetic information about the bot.")
    async def info(self, interaction: discord.Interaction):
        bot_user = self.bot.user
        owner = await self.bot.fetch_user(11949832170868572928)  # Ganti ini ke ID kamu

        embed = discord.Embed(
            title=f"✨ Welcome to {bot_user.name}! ✨",
            description=(
                "```A multifunctional Discord bot built for an amazing experience!```\n"
                "*Helping you manage your server easily and stylishly.*"
            ),
            color=discord.Color.from_rgb(64, 224, 208)  # Warna turqoise cantik
        )

        # Thumbnail dan Gambar besar
        if bot_user.avatar:
            embed.set_thumbnail(url=bot_user.avatar.url)
            embed.set_image(url=bot_user.avatar.url)

        embed.add_field(name="**Bot Name**", value=f"`{bot_user.name}`", inline=True)
        embed.add_field(name="**Owner**", value=f"`{owner.name}`", inline=True)
        embed.add_field(name="**Status**", value=":sparkles: Online and ready!", inline=True)

        embed.add_field(
            name="**Available Commands**",
            value=(
                "> **Moderation:**\n"
                "`/kick` `/ban` `/clear` `/mute` `/unmute`\n\n"
                "> **Messaging:**\n"
                "`/say` `/say_embed`\n\n"
                "> **Info:**\n"
                "`/info`"
            ),
            inline=False
        )

        embed.add_field(
            name="**Support**",
            value="Need help? Contact the bot owner!",
            inline=False
        )

        embed.set_footer(text="Created with ❤️", icon_url=bot_user.avatar.url)

        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Info(bot))
