import settings
import discord 
from discord.ext import commands
    
logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event 
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        logger.info(f"Guild ID: {bot.guilds[0].id}")
        bot.tree.copy_global_to(guild=settings.GUILDS_ID)
        await bot.tree.sync(guild=settings.GUILDS_ID)

       
    @bot.tree.command(description="Welcomes user!", name="greetings") #we can add nsfw = True (optional)
    async def bello(interaction: discord.Interaction):
        print("..............................................")
        await interaction.response.send_message(f"Ciao! {interaction.user.mention}", ephemeral=True)
      
    bot.run(settings.DISCORD_API_TOKEN, root_logger=True)

if __name__ == "__main__":
    run()