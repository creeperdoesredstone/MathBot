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
						   description='Returns the result of (expression). Available operations are +, -, *, /, %, ^.')
	async def calc(self, interaction: Interaction, expression):
		embed = nextcord.Embed(title='Output',
							  description=functions.calculate(expression, False)[0],
							  color=functions.calculate(expression, False)[1])
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
						   description='Returns the sum of the numbers from (lower) to (upper)')
	async def sum(self, interaction: Interaction, lower, upper):
		# ((u²+u)/2)-(((l-1)²+l-1)/2)
		e = '((' + upper + "^2+" + upper + ")/2)-(((" + lower + "-1)^2+" + lower + "-1)/2)"
		lower = int(lower)
		upper = int(upper)
		if lower > 0 and upper > lower:
			embed = nextcord.Embed(title='Output',
								  description=functions.calculate(e)[0],
								  color=functions.calculate(e)[1])
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

	@nextcord.slash_command(name='solve',
						   description='Solves for x')
	async def solve(self, interaction: Interaction, equation):
		r = functions.solveEquation(equation)
		if r[1] == 0x66ffff:
			embed = nextcord.Embed(title='Output',
								  description=r[0],
								  color=r[1])
		else:
			embed = nextcord.Embed(title='Invalid command!',
								  description=r[0],
								  color=r[1])
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

	@nextcord.slash_command(name='round',
						   description='Rounds (value).')
	async def round(self, interaction: Interaction, value, mode=""):
		value = float(value)
		mode = mode.lower()
		embed = nextcord.Embed(title="Output",
							  color=0x66ffff)
		if mode == "floor":
			embed.description = functions.Math.floor(value)
		elif mode == "ceil" or mode == "ceiling":
			embed.description = functions.Math.ceil(value)
		elif mode == "":
			embed.description = round(value)
		else:
			embed.title = "Invalid mode!"
			embed.description = "Please enter a valid mode."
			embed.color = 0xff0000
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

def setup(client):
	client.add_cog(Calculations(client))
