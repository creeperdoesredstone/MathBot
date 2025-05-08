import nextcord
import functions
from nextcord import Interaction
from nextcord.ext import commands

class Combinatorics(commands.Cog):

	def __init__(self, client):
		self.client = client

	@nextcord.slash_command(name='permutations',
						   description='Returns nPr')
	async def permutations(self, interaction: Interaction, n, r):
		n = int(n)
		r = int(r)
		embed = nextcord.Embed(title='Output',
							  description=functions.permutations(n, r),
							  color=0x66ffff)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

	@nextcord.slash_command(name='combinations',
						   description='Returns nCr')
	async def combinations(self, interaction: Interaction, n, r):
		n = int(n)
		r = int(r)
		embed = nextcord.Embed(title='Output',
							  description=functions.combinations(n, r),
							  color=0x66ffff)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

def setup(client):
	client.add_cog(Combinatorics(client))
