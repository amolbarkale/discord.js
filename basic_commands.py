import settings
import random
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} ID:{bot.user.id}")

    @bot.command(
        aliases=["p"],
        help="This is help",
        description="This is description",
        brief="This is breif",
        enabled=True,
        hidden=True
    )
    async def ping(ctx):
        """"Answers with pong!"""
        await ctx.send("pong!")
        
    @bot.command()
    async def say(ctx, what="WHAT?"):
        """"Answers with !say command"""
        await ctx.send(what)
        
    @bot.command()
    async def say2(ctx, *what):
        """"Answers with !say2 command"""
        await ctx.send(" ".join(what))
        
    @bot.command()
    async def say3(ctx, what = "WHAT?", why = "WHY?"):
        """"Answers with !say3 command"""
        await ctx.send(what + why)
    
    @bot.command()
    async def choices(ctx, *options):
        """"Try something with !choices 1 2 3 4 5 6 command"""
        await ctx.send(random.choice(options))
             
    bot.run(settings.DISCORD_API_TOKEN, root_logger=True)

if __name__ == "__main__":
    run()