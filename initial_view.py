
import settings
import discord 
from discord.ext import commands
import utils
    
logger = settings.logging.getLogger("bot")

class SimpleView(discord.ui.View):
    
    foo : bool = None
    
    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)
    
    async def on_timeout(self) -> None:
        await self.message.channel.send("Timedout")
        await self.disable_all_items()
    
    @discord.ui.button(label="Add games manually", 
                       style=discord.ButtonStyle.success)
    async def hello(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("game added successfully")
        self.foo = True
        self.stop()
        
    @discord.ui.button(label="Cancel", 
                       style=discord.ButtonStyle.red)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Cancelled")
        self.foo = False
        self.stop()
        
    @discord.ui.button(label="Add games from list", 
                       style=discord.ButtonStyle.blurple)
    async def from_list(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Fetching the game list")
        self.foo = False
        self.stop()
        
    @discord.ui.button(label="Another platform", 
                       style=discord.ButtonStyle.grey)
    async def another_platform(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Searching for platform")
        self.foo = False
        self.stop()
    
        
def run():
    intents = discord.Intents.default()
    intents.message_content = True
    
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event 
    async def on_ready():
        # await utils.load_videocmds(bot)
        logger.info(f"User: {bot.user} ID:{bot.user.id}")

    
    @bot.command()
    async def button(ctx):
        view = SimpleView(timeout=50)
        # button = discord.ui.Button(label="Click me")
        # view.add_item(button)
        
        message = await ctx.send(view=view)
        view.message = message
        
        await view.wait()
        await view.disable_all_items()
        
        if view.foo is None:
            logger.error("Timeout")
            
        elif view.foo is True:
            logger.error("Ok")
            
        else:
            logger.error("cancel")
        
        
        
    bot.run(settings.DISCORD_API_TOKEN, root_logger=True)

if __name__ == "__main__":
    run()