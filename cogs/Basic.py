  import nextcord
  import functions
  from nextcord.ext import commands
  from nextcord.ui import Button, View
  from nextcord import Interaction
  import json

  helpGuide = json.load(open("HelpText.json"))
  def createHelpEmbed(pageNum=0, inline=False):
    pageNum = pageNum % len(list(helpGuide))
    pageTitle = list(helpGuide)[pageNum]
    embed = nextcord.Embed(color=0x66ffff,
                 title=pageTitle,
                 description='Here are the commands in this category:')
    for key, val in helpGuide[pageTitle].items():
      embed.add_field(name='/'+key, value=val, inline=inline)
      embed.set_footer(text=functions.version + ' | ' + f"Page {pageNum+1} of {len(list(helpGuide))}")
    return embed

  def getCmdStats():
    totalCmds = 0
    maxCategory = ""; maxLength = 0
    leastCategory = ""; leastLength = 99999
    for pageNum in range(len(list(helpGuide))):
      pageTitle = list(helpGuide)[pageNum]
      if len(list(helpGuide[pageTitle])) > maxLength:
        maxLength = len(list(helpGuide[pageTitle]))
        maxCategory = pageTitle
      if len(list(helpGuide[pageTitle])) < leastLength:
        leastLength = len(list(helpGuide[pageTitle]))
        leastCategory = pageTitle
      for key, val in helpGuide[pageTitle].items():
        totalCmds += 1
    return [totalCmds, maxCategory + " (" + str(maxLength) + " commands)", leastCategory + " (" + str(leastLength) + " command)"]

  class Basic(commands.Cog):

    def __init__(self, client):
      self.client = client

    @nextcord.slash_command(name='help',
              description='Get details about the commands of MathBot.')
    async def help(self, interaction: Interaction, command=""):
      currentPage = 0
      async def nextCallback(interaction):
        nonlocal currentPage, sentMessage
        currentPage += 1
        await sentMessage.edit(embed=createHelpEmbed(pageNum=currentPage, inline=False), view=myView)
      async def previousCallback(interaction):
        nonlocal currentPage, sentMessage
        currentPage -= 1
        await sentMessage.edit(embed=createHelpEmbed(pageNum=currentPage, inline=False), view=myView)
      async def firstCallback(interaction):
        nonlocal currentPage, sentMessage
        currentPage = 0
        await sentMessage.edit(embed=createHelpEmbed(pageNum=currentPage, inline=False), view=myView)
      async def lastCallback(interaction):
        nonlocal currentPage, sentMessage
        currentPage = len(list(helpGuide)) - 1
        await sentMessage.edit(embed=createHelpEmbed(pageNum=currentPage, inline=False), view=myView)

      if command != "":
        if command in functions.commands:
          embed = nextcord.Embed(color=0x66ffff)
          for i in range(len(list(helpGuide))):
            pageTitle = list(helpGuide)[i]
            for key, val in helpGuide[pageTitle].items():
              if command == key[0:len(command)]:
                embed.add_field(name="/"+key, value=val, inline=False)
        else:
          embed = nextcord.Embed(title='Invalid command!',
                      description='Invalid input (command) in command. Please try again.',
                      color=0xff0000)
        embed.set_footer(text=functions.version)
        await interaction.response.send_message(embed=embed)
      else:
        nextButton = Button(label='>', style=nextcord.ButtonStyle.blurple)
        nextButton.callback = nextCallback
        previousButton = Button(label='<', style=nextcord.ButtonStyle.blurple)
        previousButton.callback = previousCallback
        firstButton = Button(label='|<', style=nextcord.ButtonStyle.green)
        firstButton.callback = firstCallback
        lastButton = Button(label='>|', style=nextcord.ButtonStyle.green)
        lastButton.callback = lastCallback

        myView = View(timeout=None)
        myView.add_item(firstButton)
        myView.add_item(previousButton)
        myView.add_item(nextButton)
        myView.add_item(lastButton)

        sentMessage = await interaction.response.send_message(embed=createHelpEmbed(pageNum=0, inline=False), view=myView)

    @nextcord.slash_command(name='ping',
                 description='For testing purposes. Returns "Pong!" if successful.')
    async def ping(self, interaction: Interaction):
      embed = nextcord.Embed(title='Output',
                  description='🏓 Pong!',
                  color=0x66ffff)
      bot_latency = round(self.client.latency * 1000)
      embed.set_footer(text=functions.version + " | Latency: " + str(bot_latency) + "ms")
      await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="cmd_stats",
                  description="Returns the stats of MathBot's commands.")
    async def cmd_stats(self, interaction: Interaction):
      embed=nextcord.Embed(title="MathBot's command stats:",
                 color=0x66ffff)
      embed.add_field(name="Number of categories", value=len(list(helpGuide)), inline=False)
      embed.add_field(name="Number of commands", value=getCmdStats()[0], inline=False)
      embed.add_field(name="Category that has the most commands", value=getCmdStats()[1], inline=False)
      embed.add_field(name="Category that has the least commands", value=getCmdStats()[2], inline=False)
      await interaction.response.send_message(embed=embed)

    @commands.Cog.listener()
    async def on_message(interaction: Interaction, message):
      if "<@885042856148996096>" in message.content:
        embed = nextcord.Embed(title=str(message.author)[:-2] + " pinged MathBot!（•‿•）",
                    color=0x66ffff)
        embed.set_footer(text=functions.version)
        if functions.rand.randint(1, 2) == 1:
          embed.description = "why u ping me?"
        else:
          embed.description = "why'd thou summoneth me?"
        channel = message.channel
        await channel.send(embed=embed)

    @nextcord.slash_command(name='listservers',
                description='Lists how many servers MathBot is in.')
    async def listservers(self, interaction: Interaction):
      embed = nextcord.Embed(title="MathBot's server count:",
                  description=str(len(self.client.guilds)) + " servers",
                  color=0x66ffff)
      embed.set_footer(text=functions.version)
      await interaction.response.send_message(embed=embed)

  def setup(client):
    client.add_cog(Basic(client))
