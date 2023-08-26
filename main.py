# Import required modules
import nextcord
import os
from nextcord.ext import commands
from keep_up import keep_awake

# Discord stuff
intents = nextcord.Intents().default()
intents.message_content = True
client = commands.Bot(command_prefix='/', intents=intents)

# First event: logging in
@client.event
async def on_ready():
	await client.change_presence(status=nextcord.Status.idle,
	                             activity=nextcord.Game(' around with math | ' + version[10:len(version)]))
	print("{0.user} is now online.".format(client))

initial_extensions = []

for fn in os.listdir('./cogs'):
	if fn.endswith('.py'):
		initial_extensions.append('cogs.' + fn[:-3])

print(initial_extensions)

if __name__ == '__main__':
	for e in initial_extensions:
		client.load_extension(e)

# Calling the awake function
keep_awake()
# Getting the secret token
client.run(os.getenv('TOKEN'))
