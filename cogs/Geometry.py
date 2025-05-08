import nextcord
import functions
from nextcord import Interaction
from nextcord.ext import commands

usingCommand = False
commandAuthor = -1
commandMode = ""
decimalPlaces = 0
inputNum = 0
inputs = [0, 0, 0]

class Geometry(commands.Cog):

	def __init__(self, client):
		self.client = client

	@nextcord.slash_command(name='input',
						   description='Inputs a value.')
	async def inputCommand(self, interaction: Interaction, value: float):

		global inputs
		global inputNum
		global commandMode
		global usingCommand
		
		value = float(value)

		# Modes: rhs, rss, rsa, rha, asa, sas
		
		if usingCommand:
			if interaction.user.id == commandAuthor:
				if inputNum < 3:
					inputs[inputNum] = value
					inputNum += 1
					if inputNum == 1: # Second input
						if commandMode == 'rhs' or commandMode == 'asa':
							embed = nextcord.Embed(title='Input the side.',
												  description='Use /input (side)')
						elif commandMode == 'rss' :
							embed = nextcord.Embed(title='Input the second side.',
												  description='Use /input (second side)')
						else:
							embed = nextcord.Embed(title='Input the angle.',
												  description='Use /input (angle)')
					elif inputNum == 2: # Third input
						if commandMode == 'rha' or commandMode == 'rsa':
							embed = nextcord.Embed(title='Input the mode (1 for opposite, 2 for adjacent).',
												  description='Use /input (side)')
						elif commandMode == 'asa':
							embed = nextcord.Embed(title='Input the second angle.',
												  description='Use /input (second angle)')
						elif commandMode == 'sas':
							embed = nextcord.Embed(title='Input the second side.',
												  description='Use /input (second side)')
						else:
							inputNum += 1

					if inputNum == 3:
						embed = nextcord.Embed(title='Output',											  description=functions.findSideLength(inputs, commandMode, decimalPlaces),
											  color=0x66ffff)
						inputNum = 0
						usingCommand = False
					try:
						embed.set_footer(text=functions.version)
						embed.color = 0x66ffff
					except:
						return
					else:
						await interaction.response.send_message(embed=embed)
		else:
			embed = nextcord.Embed(title='You cannot use this command!',
								  description='Use `/sidecalc` first.',
								  color=0xff0000)
			embed.set_footer(text=functions.version)
			await interaction.response.send_message(embed=embed)
	
	@nextcord.slash_command(name='sidecalc',
						   description='Returns the missing side of a triangle.')
	async def sidecalc(self, interaction: Interaction, mode, places):
		modes = ['rhs', 'rss', 'rha', 'rsa', 'asa', 'sas']
		mode = mode.lower()
		
		global usingCommand
		global commandAuthor
		global commandMode
		global decimalPlaces

		decimalPlaces = int(places)
		
		if not usingCommand:
			if mode in modes:
				usingCommand = True
				commandAuthor = interaction.user.id
				commandMode = mode
				if mode == 'rhs' or mode == 'rha':
					embed = nextcord.Embed(title='Input the hypoteneuse.',
										   description='Use /input (hypoteneuse)',
										  color=0x66ffff)
				elif mode == 'asa':
					embed = nextcord.Embed(title='Input the first angle.',
										   description='Use /input (first angle)',
										  color=0x66ffff)
				else:
					embed = nextcord.Embed(title='Input the first side.',
										   description='Use /input (first side)',
										  color=0x66ffff)
			else:
				embed = nextcord.Embed(title='Is invalid mode',
									  color=0xff0000)
		else:
			embed = nextcord.Embed(title='The command is not free to use',
								  color=0xff0000)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

	@nextcord.slash_command(name='area', description="Bruh.")
	async def regulararea(self, interaction: Interaction, shape, sideLength):
		shape = shape.lower()
		sideLength = float(sideLength)
	
		embed = nextcord.Embed(title='Output',
			   description=functions.findArea(sideLength, shape),
			   color=0x66ffff)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

def setup(client):
	client.add_cog(Geometry(client))
