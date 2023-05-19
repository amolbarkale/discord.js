import random
import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
    
    @bot.command()
    async def modal(ctx):
        embed = discord.Embed(
            color=discord.Colour.dark_teal(),
            description="this is the game description",
            title="this is the game title"
        )
        embed.set_footer(text="this is the footerc")
        embed.set_author(name="Halo 3", url="https://www.halowaypoint.com/")

        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/en/thumb/5/5c/Halo-_Reach_box_art.png/220px-Halo-_Reach_box_art.png")
        embed.set_image(url="https://upload.wikimedia.org/wikipedia/en/8/80/Halo_-_Combat_Evolved_%28XBox_version_-_box_art%29.jpg")

        embed.add_field(name="Game", value="https://www.halowaypoint.com/", inline=False)
        embed.add_field(name="Website", value="https://www.halowaypoint.com/")
        embed.insert_field_at(1, name="Nintendo", value= "https://www.nintendo.com/store/products/halo-mash-up-70050000003743-switch/")
        await ctx.send(embed=embed)

    bot.run(settings.DISCORD_API_TOKEN, root_logger=True)

if __name__ == "__main__":
    run()