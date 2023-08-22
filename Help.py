import nextcord
import functions
from nextcord.ext import commands
from nextcord import Interaction

class Help(commands.Cog):

	def __init__(self, client):
		self.client = client

	@nextcord.slash_command(name='help',
					  description='Get details about the commands of MathBot.')
	async def help(self, interaction: Interaction):
		embed = nextcord.Embed(title='Someone used /help!',
							   description="""You can run these commands:
	  `/help:` Generates this message.
	  `/random:` Generates a random value between 0 and 1.
	  `/randint (min) (max):` Generates a random integer between (min) and (max).
	  `/roll:` Rolls a dice.
	  `/calc (expression):` Evaluates an expression (could be 1 or multiple arguments) and returns the result of that expression. Available operations are `+`, `-`, `*`, `/`, `%`, `**`.
	  `/basecalc (base) (expression):` Evaluates an expression (could be 1 or multiple arguments) and returns the result of that expression in base (base). Available operations are `+`, `-`, `*`, `/`, `%`, `**`. Available bases are from 2 to 64.
	  `/trig (operation) (value):` Returns the calculated number after passed through a trigonometry operation. Available operations are `sin`, `cos`, `tan`, `asin`, `acos`, `atan`.
	  `/pytriangle (side) (side):` Returns the hypotenuse of a right triangle.
	  `/fib (n):` Returns the nth term in the Fibonacci sequence, assuming n is a positive integer and n < 1475.
	  `/root (n) (value):` Returns the nth root of (value).
	  `/constant (c):` Returns a constant. Available constants are `pi`, `e`, `phi`, `ec`, `tau`, `i`.
	  `/convert (base1) (base2) (value):` Converts (value) from (base1) to (base2). Available bases are from 2 to 64. Any digit that has a value between 10 and 35, the numbers that are represented by letters **MUST** be written in capitals. Any digit that has a value between 36 and 61 **MUST** be written in lowercase.
	  `/factors (n):` Returns the prime factors of n, assuming n is a positive integer and n has less than 61 digits.
	  `/factorial (n):` Returns n!, assumming n is a positive integer and n < 1495.
	  `/term (n) (sequence):` Returns the nth term of a linear sequence. Terms are separated by commas.
	  `/radians (value):` Converts (value) to radians.
	  `/degrees (value):` Converts (value) to degrees.
   	  `/sum (n):` Returns the sum of the first (n) numbers, assuming n is a positive integer.
	  `/g_sequence (n) (r):` Returns the nth term a geometric series with a common ratio of r.""",
							   color=0x66ffff)
		embed.set_footer(text=functions.version)
		await interaction.response.send_message(embed=embed)

def setup(client):
	client.add_cog(Help(client))
