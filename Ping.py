import nextcord
import functions
from nextcord.ext import commands
from nextcord import Interaction

class Ping(commands.Cog):

	def __init__(self, client):
		self.client = client

	@nextcord.slash_command(name='ping',
						   description='For testing purposes. Returns "Pong!" if successful.')
	async def ping(self, interaction: Interaction):
		embed = nextcord.Embed(title='Output',
							  description='🏓 Pong!',
							  color=0x66ffff)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

def setup(client):
	client.add_cog(Ping(client))
