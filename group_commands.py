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
    async def add(ctx, one:int, two:int):
        """"Try something with !add 1 2 command"""
        await ctx.send(one + two)
        
    @bot.command()
    async def substract(ctx, one:int, two:int):
        """"Try something with !add 1 2 command"""
        await ctx.send(one - two)
        
    bot.run(settings.DISCORD_API_TOKEN, root_logger=True)


if __name__ == "__main__":
    run()