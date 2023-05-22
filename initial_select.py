import settings
import discord 
from discord.ext import commands
from discord.ui import Button, View

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
   
class FavouriteGameSelect(discord.ui.Select):
    def __init__(self):
        options = [discord.SelectOption(label=str(i), value=str(i)) for i in range(1, 25)]

        super().__init__(options=options, placeholder="What do you like to play?", max_values=4)

    async def callback(self, interaction:discord.Interaction):
        await self.view.respond_to_answer2(interaction, self.values)
        
class SurveyView(discord.ui.View):
    answer1 = None 
    answer2 = None 
    
    @discord.ui.select(
        placeholder="What is your age?",
        options=[
            discord.SelectOption(label="16 - 17", value="16"),
            discord.SelectOption(label="18 - 23", value="18"),
            discord.SelectOption(label="24 - 30", value="24")
        ]        
    )
    async def select_age(self, interaction:discord.Interaction, select_item : discord.ui.Select):
        self.answer1 = select_item.values
        self.children[0].disabled= True
        game_select = FavouriteGameSelect()
        self.add_item(game_select)
        await interaction.message.edit(view=self)
        await interaction.response.defer()

    async def respond_to_answer2(self, interaction : discord.Interaction, choices):
        self.answer2 = choices 
        self.children[1].disabled= True
        await interaction.message.edit(view=self)
        await interaction.response.defer()
        self.stop()
    
def run():
    intents = discord.Intents.all()
    
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event 
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
            
    @bot.command()
    async def survey(ctx):
        view = SurveyView()
        await ctx.send(view=view)
        
        await view.wait()
        
        results = {
            "a1": view.answer1,
            "a2": view.answer2,
        }
        
        await ctx.send(f"{results}")
        await ctx.message.author.send("Thank you for the particitation")
     
        
    bot.run(settings.DISCORD_API_TOKEN, root_logger=True)

if __name__ == "__main__":
    run()