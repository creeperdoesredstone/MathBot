import nextcord
import functions
from nextcord.ext import commands
from nextcord import Interaction

# Constants
pi = 3.1415926538979323846
e = 2.7182818284590452354
phi = 1.6180339887498948482
ec = 0.5772156649015328606
tau = 6.2831853077958647692
π = pi
φ = phi
γ = ec
τ = tau

class Calculations(commands.Cog):

	def __init__(self, client):
		self.client = client

	@nextcord.slash_command(name='calc',
						   description='Returns the result of (expression). Available operations are +, -, *, /, %, **.')
	async def calc(self, interaction: Interaction, expression):
		embed = nextcord.Embed(title='Output',
							  description=functions.calculate(expression)[0],
							  color=functions.calculate(expression)[1])
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

	@nextcord.slash_command(name='basecalc',
						   description='Returns the result of (expression) converted to (base). Available bases are from 2 to 64.')
	async def basecalc(self, interaction: Interaction, expression, base):
		base = int(base)
		if base > 1 and base < 65:
			embed = nextcord.Embed(title='Output',
								  description=functions.convertVal(10, base, functions.calculate(expression)[0])[0],
								  color=functions.convertVal(10, base, functions.calculate(expression)[0])[1])
		else:
			embed = nextcord.Embed(title='Out of bounds!',
								  description='Invalid input (base) in command. Maybe try using `/help`?',
								  color=0xff0000)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

	@nextcord.slash_command(name='root',
						   description='Returns the nth root of (value)')
	async def root(self, interaction: Interaction, n, value):
		n = int(n)
		value = float(value)
		if value >= 0:
			embed = nextcord.Embed(title='Output',
								  description=functions.nthRoot(value, n),
								  color=0x66ffff)
		else:
			if n % 2 == 0:
				embed = nextcord.Embed(title='Output',
									  description=str(functions.nthRoot(abs(value), n))+'i',
									  color=0x66ffff)
			else:
				embed = nextcord.Embed(title='Output',
									  description=functions.nthRoot(value, n),
									  color=0x66ffff)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

	@nextcord.slash_command(name='factors',
						   description='Returns the prime factors of n, assuming n is a positive integer')
	async def factors(self, interaction: Interaction, n):
		n = int(n)
		if n > 0:
			embed = nextcord.Embed(title='Output',
								  description=functions.factor(n),
								  color=0x66ffff)
		else:
			embed = nextcord.Embed(title='Out of bounds!',
								  description='Invalid input (n) in command. Please try again.',
								  color=0xff0000)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

	@nextcord.slash_command(name='factorial',
						   description='Returns n!, assuming n is a positive integer or 0 and n < 1495')
	async def factorial(self, interaction: Interaction, n):
		n = int(n)
		if n >= 0 and n < 1495:
			embed = nextcord.Embed(title='Output',
								  description=functions.Math.factorial(n),
								  color=0x66ffff)
		else:
			embed = nextcord.Embed(title='Out of bounds!',
								  description='Invalid input (n) in command. Please try again.',
								  color=0xff0000)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

	@nextcord.slash_command(name='sum',
						   description='Returns the sum of the first (n) numbers, assuming n is a positive integer')
	async def sum(self, interaction: Interaction, n):
		e = '(' + n + '*(' + n + '+1))/2'
		n = int(n)
		if n > 0:
			embed = nextcord.Embed(title='Output',
								  description=functions.calculate(e)[0],
								  color=functions.calculate(e)[1])
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

def setup(client):
	client.add_cog(Calculations(client))
