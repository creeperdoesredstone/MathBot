import nextcord
import functions
from nextcord.ext import commands
from nextcord import Interaction

class Random(commands.Cog):

	def __init__(self, client):
		self.client = client

	@nextcord.slash_command(name='random',
						   description='Generates a random value between 0 and 1.')
	async def random(self, interaction: Interaction):
		embed = nextcord.Embed(title='Output',
							  description=str(functions.rand.random()),
							  color=0x66ffff)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

	@nextcord.slash_command(name='randint',
						   description='Generates a random integer between (min) and (max).')
	async def randint(self, interaction: Interaction, min, max):
		min = int(min)
		max = int(max)
		embed = nextcord.Embed(title='Output',
							  description=str(functions.rand.randint(min, max)),
							  color=0x66ffff)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

	@nextcord.slash_command(name='roll',
						   description='Rolls a dice.')
	async def roll(self, interaction: Interaction):
		embed = nextcord.Embed(title='Output',
							  description=str(functions.rand.randint(1, 6)),
							  color=0x66ffff)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

def setup(client):
	client.add_cog(Random(client))
