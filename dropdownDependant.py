import discord
import settings
from discord.ext import commands
titlee = ["Title 1", "Title 2", "Title 3", "Title 4", "Title 5", "Title 6", "Title 7", "Title 8", "Title 9", "Title 10", "Title 11", "Title 12", "Title 13", "Title 14", "Title 15", "Title 16", "Title 17", "Title 18", "Title 19", "Title 20", "Title 21", "Title 22", "Title 23", "Title 24", "Title 25", "Title 26"]
options = [discord.SelectOption(label=title) for title in titlee]

def run():
    intents = discord.Intents.all()    
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')

    @bot.command()
    async def dropdowns(ctx):
        initial_dropdown = discord.ui.Select(
            placeholder='Select an optionn',
            custom_id='dropdown1',
            options=options
        )

        view = discord.ui.View()
        view.add_item(initial_dropdown)

        await ctx.send(content='Please select an option:', view=view)

    @bot.event
    async def on_interaction(interaction):
        if not isinstance(interaction, discord.Interaction):
            return

        selected_value = interaction.data['values'][0]

        if interaction.data['custom_id'] == 'dropdown1':
            second_dropdown = discord.ui.Select(
                placeholder='Select an option',
                custom_id='dropdown2',
                disabled=True  # Disable the second dropdown initially until options are generated
            )

            # view = interaction.messagestst
            # view.clear_items()
            view = discord.ui.View()
            view.add_item(second_dropdown)

            await interaction.response.edit_message(content='Please select another option:', view=view)

            # Generate options based on the selected value from the first dropdown
            options = generate_options(selected_value)

            # Enable and update the second dropdown with the generated options
            second_dropdown.disabled = False
            for option in options:
                second_dropdown.add_option(option)

            await interaction.message.edit(view=view)

        elif interaction.data['custom_id'] == 'dropdown2':
            third_dropdown = discord.ui.Select(
                placeholder='Select an option',
                custom_id='dropdown3',
                min_values=1,
                max_values=1
            )

            view = interaction.message.view
            view.clear_items()
            view.add_item(third_dropdown)

            await interaction.response.edit_message(content='Please select the final option:', view=view)

            # Generate options based on the selected value from the second dropdown
            options = generate_options(selected_value)

            # Update the third dropdown with the generated options
            for option in options:
                third_dropdown.add_option(option)

            await interaction.message.edit(view=view)

        elif interaction.data['custom_id'] == 'dropdown3':
            selected_values = interaction.data['values']

    def generate_options(selected_value):
         return [
            discord.SelectOption(label=f'{selected_value} Option A', value=f'{selected_value}_optionA'),
            discord.SelectOption(label=f'{selected_value} Option B', value=f'{selected_value}_optionB'),
            discord.SelectOption(label=f'{selected_value} Option C', value=f'{selected_value}_optionC')
        ]

    bot.run(settings.DISCORD_API_TOKEN, root_logger=True)

if __name__ == "__main__":
    run()