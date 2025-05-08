import nextcord
import functions
from nextcord.ext import commands
from nextcord import Interaction

class Graphing(commands.Cog):
	def __init__(self, client):
		self.client = client

	@nextcord.slash_command(name='plot',
						   description='Plots a graph.')
	async def plot(self, interaction: Interaction, equation, range):
		e = equation
		equation = equation.lower()
		equation = equation.replace(' ', '')
		if equation[0:2] != "y=":
			await interaction.response.send_message("Equation must start with y=.")
		equation = equation.replace('^', '**')
		equation = equation.replace('log', 'math.log')
		equation = equation.replace('ln', 'math.log')
		equation = equation.replace('sin', 'math.sin')
		equation = equation.replace('cos', 'math.cos')
		equation = equation.replace('tan', 'math.tan')
		equation = equation.replace('asin', 'math.asin')
		equation = equation.replace('acos', 'math.acos')
		equation = equation.replace('atan', 'math.atan')
		equation = equation.replace('sqrt', 'math.sqrt')
		equation = equation.replace('pi', 'math.pi')
		equation = equation.replace('e', 'math.e')
		equalIdx = None
		equal = False
		idx = 0
		for i in equation:
			if i == '=':
				if not equal:
					equal = True
					equalIdx = idx
				else:
					embed = nextcord.Embed(title='Invalid equation!',
										  description='Equations can only have one equal sign.',
										  color=0xff0000)
					embed.set_footer(text=functions.version)
					await interaction.response.send_message(embed=embed)
					return
			idx += 1
		if equalIdx == None:
			embed = nextcord.Embed(title='Invalid equation!',
								  description='You must enter an equal sign.',
								  color=0xff0000)
		yList = []
		range = abs(int(range))
		ranges = 2*range+1
		idx = 0
		while idx < ranges:
			x = idx-range
			y = eval(equation[equalIdx+1:len(equation)])
			yList.append(y)
			idx += 1
		
		import matplotlib.pyplot as plt
		import numpy as np
		
		x = np.arange(0-range, range+1, 1)
		y = yList
		plt.clf()
		plt.plot(x, y)
		plt.xlabel('X')
		plt.ylabel('Y')
		plt.title(e)
		plt.grid(True)
		
		plt.savefig('Graph.png')
		await interaction.response.send_message(file=nextcord.File('Graph.png'))

def setup(client):
	client.add_cog(Graphing(client))
