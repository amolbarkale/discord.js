import settings
import discord 
from discord.ext import commands

logger = settings.logging.getLogger("bot")


def run():
    
    intents = discord.Intents.all()
    
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event 
    async def on_ready():
        # await utils.load_videocmds(bot)
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
    


    bot.run(settings.DISCORD_API_TOKEN, root_logger=True)
    
if __name__ == "__main__":
    run()
