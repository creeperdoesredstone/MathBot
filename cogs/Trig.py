import nextcord
import functions
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class Trig(commands.Cog):

	def __init__(self, client):
		self.client = client

	@nextcord.slash_command(name='trig',
						   description='Returns the sin/cos/tan/asin/acos/atan of (value).')
	async def trig(self, interaction: Interaction, value,
				   operation: int = SlashOption(
					   name = 'Operations',
					   choices = {'sin':1, 'cos':2, 'tan':3, 'asin':4, 'acos':5, 'atan':6}
	)):
		value = functions.Math.radians(float(value))
		degVal = float(value)
		if operation == 1:
			embed = nextcord.Embed(title='Output',
								  description=str(functions.Math.sin(value)),
								  color=0x66ffff)
		elif operation == 2:
			embed = nextcord.Embed(title='Output',
								  description=str(functions.cosine(degVal)),
								  color=0x66ffff)
		elif operation == 3:
			embed = nextcord.Embed(title='Output',
								  description=str(functions.Math.tan(value)),
								  color=0x66ffff)
		elif operation == 4:
			embed = nextcord.Embed(title='Output',
								  description=str(functions.Math.asin(degVal)),
								  color=0x66ffff)
		elif operation == 5:
			embed = nextcord.Embed(title='Output',
								  description=str(functions.Math.acos(degVal)),
								  color=0x66ffff)
		elif operation == 6:
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
