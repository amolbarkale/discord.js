import random
import settings
import discord
from discord.ext import commands
from discord.ui import View

logger = settings.logging.getLogger("bot")

class SimpleView(discord.ui.View):
    @discord.ui.button(label="Add platform", 
                       style=discord.ButtonStyle.grey)
    # async def another_platform(self, interaction: discord.Interaction, button: discord.ui.Button):
        # await interaction.response.send_message("Searching for platform" )
    async def another_platform(self, interaction: discord.Interaction, button: discord.ui.Button):
        select = discord.ui.Select(
                placeholder="Select a platform",
                options=[
            discord.SelectOption(label="PC", value="PC"),
            discord.SelectOption(label="Console", value="Console"),
            discord.SelectOption(label="Mobile", value="Mobile"),
        ]
        )
        self.add_item(select)
        await interaction.response.send_message(view= self)
 
def run():
    intents = discord.Intents.default()
    intents.message_content = True
    
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

    @bot.command()
    async def select_platform(ctx):
        view = SimpleView()
        await ctx.send(view = view)
        
    bot.run(settings.DISCORD_API_TOKEN, root_logger=True)

if __name__ == "__main__":
    run()