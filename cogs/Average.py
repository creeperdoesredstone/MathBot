import nextcord
import functions
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class Average(commands.Cog):

	def __init__(self, client):
		self.client = client

	@nextcord.slash_command(name='average',
							description='Calculates the average of semicolon-separated numbers.')
	async def average(self, interaction: Interaction,
					  values: str = SlashOption(description="Numbers separated by semicolons (e.g. 1;2;3.5)")):
		result = functions.average(values)
		embed = nextcord.Embed(title=result[0],
							   description=result[1],
							   color=result[2])
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

def setup(client):
	client.add_cog(Average(client))
