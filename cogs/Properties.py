import nextcord
import functions
from functions import joinList
from nextcord import Interaction
from nextcord.ext import commands

class Properties(commands.Cog):

	def __init__(self, client):
		self.client = client

	@nextcord.slash_command(name='properties',
						   description='Returns the properties of (number)')
	async def properties(self, interaction: Interaction, number):
		embed = nextcord.Embed(title='Properties of ' + number,
							   color=0x66ffff)

		number = int(number)
		factors = functions.factor(number)
		embed.add_field(name='Factorization',
						value=joinList(factors, 0, ' * '),
						inline=False)
		embed.add_field(name='',
						value='',
						inline=False)
		embed.add_field(name='Previous integer',
						value=number-1,
						inline=True)
		embed.add_field(name='Next integer',
						value=number+1,
						inline=True)
		embed.add_field(name='',
						value='',
						inline=False)
		embed.add_field(name='Is prime?',
						value='Yes' if len(factors)==1 and factors[0]!=1 else 'No',
						inline=True)
		if number % 10 == 1 and number != 11:
			embed.add_field(name=str(number)+'st prime',
							value=functions.nthPrime(number),
							inline=True)
		elif number % 10 == 2 and number != 12:
			embed.add_field(name=str(number)+'nd prime',
							value=functions.nthPrime(number),
							inline=True)
		elif number % 10 == 3 and number != 13:
			embed.add_field(name=str(number)+'rd prime',
							value=functions.nthPrime(number),
							inline=True)
		else:
			embed.add_field(name=str(number)+'th prime',
							value=functions.nthPrime(number),
							inline=True)
		embed.add_field(name='',
						value='',
						inline=False)
		embed.add_field(name='Is a Fibonacci number?',
						value='Yes' if functions.isFib(number) else 'No',
						inline=True)
		embed.add_field(name='Is a Palindrome number?',
						value='Yes' if functions.isPalin(number) else 'No',
						inline=True)
		embed.add_field(name='',
						value='',
						inline=False)
		embed.add_field(name='Binary',
						value=functions.convertVal(10, 2, str(number))[0],
						inline=True)
		embed.add_field(name='Hexadecimal',
						value=functions.convertVal(10, 16, str(number))[0],
						inline=True)
		embed.add_field(name='',
						value='',
						inline=False)
		embed.add_field(name='Square',
						value=number*number,
						inline=True)
		embed.add_field(name='Square root',
						value=functions.Math.sqrt(number),
						inline=True)
		embed.add_field(name='',
						value='',
						inline=False)
		embed.add_field(name='Natural logarithm',
						value=functions.Math.log(number),
						inline=True)
		embed.add_field(name='Decimal logarithm',
						value=functions.Math.log10(number),
						inline=True)
		embed.add_field(name='',
						value='',
						inline=False)
		embed.add_field(name='Sine',
					    value=functions.Math.sin(functions.Math.radians(number)),
					    inline=True)
		embed.add_field(name='Cosine',
					    value=functions.cosine(number),
					    inline=True)
		embed.add_field(name='Tangent',
					    value=functions.Math.tan(functions.Math.radians(number)),
					    inline=True)
		
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

def setup(client):
	client.add_cog(Properties(client))
