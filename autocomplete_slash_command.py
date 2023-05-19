import enum
import typing
import settings
import discord
from discord.ext import commands
from discord import app_commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        
        bot.tree.copy_global_to(guild=settings.GUILDS_ID)
        await bot.tree.sync(guild=settings.GUILDS_ID)

# we can only use max 25 choices / options when we are using this method
    async def platform_autocompletion(
        interaction: discord.Interaction,
        current: str
    ) -> typing.List[app_commands.Choice[str]]:
        data = []
        for platform_choice in [ 'xbox1', 'playstation1', 'nintendo1', 'gog1', 'xbox2', 'playstation2', 'nintendo2', 'gog2', 'xbox3', 'playstation3', 'nintendo3', 'gog3', 'xbox4', 'playstation4', 'nintendo4', 'gog4', 'xbox5', 'playstation5', 'nintendo5', 'gog5', 'xbox6', 'playstation6', 'nintendo6', 'gog6']:
            if current.lower() in platform_choice.lower():
                data.append(app_commands.Choice(name=platform_choice, value=platform_choice))
        return data 
   
        
    @bot.tree.command()
    @app_commands.autocomplete(item=platform_autocompletion)
    async def platform(interaction: discord.Interaction, item: str):
        print("item", item)
        await interaction.response.send_message(f"{item}", ephemeral=True)
    
    bot.run(settings.DISCORD_API_TOKEN, root_logger=True)

if __name__ == "__main__":
    run()