import nextcord
import functions
from nextcord.ext import commands
from nextcord import Interaction

class Convert(commands.Cog):

	def __init__(self, client):
		self.client = client

	@nextcord.slash_command(name='convert',
						   description='Converts (value) from (base1) to (base2). Available bases are from 2 to 64.')
	async def convert(self, interaction: Interaction, base1, base2, val):
		base1 = int(base1)
		base2 = int(base2)
		if base1 > 1 and base1 < 65:
			if base2 > 1 and base2 < 65:
				embed = nextcord.Embed(title='Output',
									  description=functions.convertVal(base1, base2, val)[0],
									  color=functions.convertVal(base1, base2, val)[1])
			else:
				embed = nextcord.Embed(title='Invalid command!',
									  description='Invalid input (base2) in command. Please try again.',
									  color=0xff0000)
		else:
			embed = nextcord.Embed(title='Invalid command!',
								  description='Invalid input (base1) in command. Please try again.',
								  color=0xff0000)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

def setup(client):
	client.add_cog(Convert(client))
