import nextcord
import functions
from nextcord.ext import commands
from nextcord import Interaction

class Trig(commands.Cog):

	def __init__(self, client):
		self.client = client

	@nextcord.slash_command(name='trig',
						   description='Returns the sin/cos/tan/asin/acos/atan of (value).')
	async def trig(self, interaction: Interaction, type, value):
		value = functions.Math.radians(float(value))
		degVal = float(value)
		if type == 'sin':
			embed = nextcord.Embed(title='Output',
								  description=str(functions.Math.sin(value)),
								  color=0x66ffff)
		elif type == 'cos':
			embed = nextcord.Embed(title='Output',
								  description=str(functions.Math.cos(value)),
								  color=0x66ffff)
		elif type == 'tan':
			embed = nextcord.Embed(title='Output',
								  description=str(functions.Math.tan(value)),
								  color=0x66ffff)
		elif type == 'asin':
			embed = nextcord.Embed(title='Output',
								  description=str(functions.Math.asin(degVal)),
								  color=0x66ffff)
		elif type == 'acos':
			embed = nextcord.Embed(title='Output',
								  description=str(functions.Math.acos(degVal)),
								  color=0x66ffff)
		elif type == 'atan':
			embed = nextcord.Embed(title='Output',
								  description=str(functions.Math.atan(degVal)),
								  color=0x66ffff)
		else:
			embed = nextcord.Embed(title='Invalid command!',
								  description='Please try again. Maybe try using `/help`?',
								  color=0xff0000)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

	@nextcord.slash_command(name='radians',
						   description='Converts (value) to radians')
	async def radians(self, interaction: Interaction, value):
		value = float(value)
		embed = nextcord.Embed(title='Output',
							  description=functions.Math.radians(value),
							  color=0x66ffff)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

	@nextcord.slash_command(name='degrees',
						   description='Converts (value) to degrees')
	async def degrees(self, interaction: Interaction, value):
		value = float(value)
		embed = nextcord.Embed(title='Output',
							  description=functions.Math.degrees(value),
							  color=0x66ffff)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

def setup(client):
	client.add_cog(Trig(client))
