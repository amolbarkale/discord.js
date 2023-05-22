from re import A
import settings
import discord
from discord.ext import commands
from discord import app_commands
from typing import List

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.all()

    bot = commands.Bot(command_prefix="!",
    intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

        bot.tree.copy_global_to(guild=settings.GUILDS_ID)
        await bot.tree.sync(guild=settings.GUILDS_ID)

    @bot.tree.command()
    async def add_game(interaction: discord.Interaction, name: str):
        await interaction.response.send_message(f'You have added **{name}** in your bucket ✅')

    @add_game.autocomplete('name')
    async def games_autocomplete(
        interaction: discord.Interaction,
        current: str,
    ) -> List[app_commands.Choice[str]]:
        games = [
        "Minecraft",     "Metal Gear Solid 4: Guns of the Patriots",
        "Uncharted 2: Among Thieves"
        "The Last of Us Remastered",
        "Grand Theft Auto V: Premium Edition",
        "Grand Theft Auto V: The Criminal Enterprise Starter Pack",
        "Grand Theft Auto V: The Doomsday Heist",
        "Grand Theft Auto Online",
        "Minecraft: Java Edition",
        "Minecraft: Bedrock Edition",
        "Minecraft Dungeons",
        "Minecraft Earth",
        "Minecraft: Story Mode"
        "Among Us",
        "Fortnite Battle Royale",
        "Roblox",
        "Call of Duty: Warzone",
        "Fall Guys: Ultimate Knockout",
        "Dota 2",
        "League of Legends",
        "Counter-Strike: Global Offensive",
        "Grand Theft Auto Online",
        "PlayerUnknown's Battlegrounds"]
        return [
            app_commands.Choice(name=game, value=game)
            for game in games if current.lower() in game.lower()  
        ][:25]
        

   
     
    bot.run(settings.DISCORD_API_TOKEN, root_logger=True)

if __name__ == "__main__":
    run()
    
    
