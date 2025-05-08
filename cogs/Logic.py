import nextcord
import functions
from nextcord.ext import commands
from nextcord import Interaction

class Logic(commands.Cog):

	def __init__(self, client):
		self.client = client

	@nextcord.slash_command(name='logic',
						   description='Returns the result of a binary logic operation.')
	async def logic(self, interaction: Interaction, operation, val1, val2):
		r = functions.logicOp(operation, val1, val2)
		embed = nextcord.Embed(title=r[0],
							  description=r[1],
							  color=r[2])
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

def setup(client):
	client.add_cog(Logic(client))
