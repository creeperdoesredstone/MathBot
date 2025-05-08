import nextcord
import functions
from nextcord.ext import commands
from nextcord import Interaction

class Calculus(commands.Cog):

    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name='derive',
                             description='Returns the derivative of (expression)')
    async def derive(self, interaction: Interaction, expression):
        r = functions.derive(expression)
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
    @nextcord.slash_command(name='log',
                             description='Returns the log of (n) with base (base)')
    async def log(self, interaction: Interaction, n, base):
        bases = ['e', 'pi', 'phi', 'tau', 'ec']
        basesVal = [functions.e, functions.pi, functions.phi, functions.tau, functions.ec]
        n = float(n)
        try:
            base = float(base)
        except:
            if base in bases:
                base = basesVal[bases.index(base)]
        embed = nextcord.Embed(title='Output',
                                 description=functions.Math.log(n, base),
                                color=0x66ffff)
        embed.set_footer(text=functions.version)
        await interaction.response.send_message(embed=embed)
    @nextcord.slash_command(name='integrate',
                                                 description='Integrates (expression) with respect to (variable).')
    async def integrate(self, interaction: Interaction, expression, lowerBound, upperBound):
        interval = 0.625
        result = 0
        x = float(lowerBound)
        fMidX = expression.replace("x", f"(x + ({interval}/2))")
        while x < float(upperBound):
            result += eval(fMidX) * interval
            x += interval
        await interaction.response.send_message(f"Output: {result}")

def setup(client):
    client.add_cog(Calculus(client))
