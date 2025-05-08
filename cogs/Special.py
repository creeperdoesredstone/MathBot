import nextcord
import functions
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class Special(commands.Cog):

	def __init__(self, client):
		self.client = client

	@nextcord.slash_command(name='pytriangle',
						   description='Returns the hypoteneuse of a right triangle')
	async def pytriangle(self, interaction: Interaction, side1, side2):
		try:
			side1 = float(side1)
		except:
			embed = nextcord.Embed(title='Invalid command!',
								  description='Invalid input (side1) in command. Please try again.',
								  color=0xff0000)
		else:
			try:
				side2 = float(side2)
			except:
				embed = nextcord.Embed(title='Invalid command!',
									  description='Invalid input (side2) in command. Please try again.',
									  color=0xff0000)
			else:
				embed = nextcord.Embed(title='Output',
									  description=functions.pyTriangle(side1, side2),
									  color=0x66ffff)
		finally:
			embed.set_footer(text=functions.version)
			await interaction.response.send_message(embed=embed)

	@nextcord.slash_command(name='fib',
						   description='Returns the nth term in the Fibonacci sequence')
	async def fib(self, interaction: Interaction, n):
		try:
			n = int(n)
		except:
			embed = nextcord.Embed(title='Invalid command!',
								  description='Invalid input (n) in command. Please try again.',
								  color=0xff0000)
		else:
			if n >= 0 and n < 1475:
				embed = nextcord.Embed(title='Output',
									  description=functions.nthTermOfFib(n),
									  color=0x66ffff)
			else:
				embed = nextcord.Embed(title='Out of bounds!',
									  description='Invalid input (n) in command. Please try again.',
									  color=0xff0000)
		finally:
			embed.set_footer(text=functions.version)
			await interaction.response.send_message(embed=embed)

	@nextcord.slash_command(name='constant',
						   description='Returns a constant up to (dp) digits of accuracy. Available constants are pi, e, phi, ec, tau, i')
	async def constant(self, interaction: Interaction, dp,
					  c: int = SlashOption(
						  name = 'constants',
						  choices = {'pi':1, 'e':2, 'phi':3, 'ec':4, 'tau':5, 'i':6, 'your mom':7},
						  description = 'Choose a constant.',
					  	),
					):
		t = 'Output'
		try:
			dp = int(dp)
		except:
			t = 'Invalid choice!'
			o = ['Invalid input (c) in command. Please try again.', 0xff0000]
		else:
			strPi = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
			strE = '2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274'
			strPhi = '1.6180339887498948482045868343656381177'
			strEc = '0.577215664901532860606512090082402431042'
			strTau = '6.2831853071795864769252867665590057683943'
			strI = '0.577215664901532860606512090082402431042'
			if c == 1:
				if dp < 1 or dp > 100:
					o = ['Invalid input (dp) in command. Please try again.', 0xff0000]
				else:
					o = [f'π ≈ {strPi[0:dp+2]}', 0x66ffff]
			elif c == 2:
				if dp < 1 or dp > 100:
					o = ['Invalid input (dp) in command. Please try again.', 0xff0000]
				else:
					o = [f'e ≈ {strE[0:dp+2]}', 0x66ffff]
			elif c == 3:
				o = ['φ ≈ 1.6180339887498948482', 0x66ffff]
			elif c == 4:
				o = ['γ ≈ 0.5772156649015328606', 0x66ffff]
			elif c == 5:
				o = ['τ ≈ 6.2831853077958647692', 0x66ffff]
			elif c == 6:
				o = ['i = The square root of -1', 0x66ffff]
			elif c == 7:
				t = 'Fatal error!'
				o = ['Constant too big to display.', 0xff0000]
			else:
				t = 'Invalid choice!'
				o = ['Invalid input (c) in command. Please try again.', 0xff0000]
		embed = nextcord.Embed(title=t,
							  description=o[0],
							  color=o[1])
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

	@nextcord.slash_command(name='term',
						   description='Returns the nth term in a linear sequence')
	async def term(self, interaction: Interaction, n, sequence):
		n = int(n)
		embed = nextcord.Embed(title='Output',
							  description=functions.nthTermOfSeq(n, sequence),
							  color=0x66ffff)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

	@nextcord.slash_command(name='g_series',
						   description='Returns n terms of a geometric series with a common ratio of r')
	async def g_series(self, interaction: Interaction, n, start, r):
		n = int(n)
		r = int(r)
		embed = nextcord.Embed(title='Output',
							  description=functions.gSequence(n, start, r),
							  color=0x66ffff)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

	@nextcord.slash_command(name='g_sequence',
							description='Generates a linear sequence with n terms')
	async def g_sequence(self, interaction: Interaction, n, start, difference):
		n = int(n)
		start = float(start)
		difference = float(difference)
		embed = nextcord.Embed(title='Output',
							  description=functions.joinList(functions.generateSeq(n, start, difference), 0, ", "),
							  color=0x66ffff)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

	@nextcord.slash_command(name='prime',
                           description='Returns the nth prime')
	async def prime(self, interaction: Interaction, n):
		n = int(n)
		if 0 < n and n < 56561:
			embed = nextcord.Embed(title='Output',
	                              description=functions.nthPrime(n),
	                              color=0x66ffff)
		else:
			embed = nextcord.Embed(title='Out of bounds!',
	                              description='Invalid input (n) in command. Please try again.',
	                              color=0xff0000)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

def setup(client):
	client.add_cog(Special(client))
