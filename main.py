import os
import discord
from modules import roles, startup, welcome, tickets

intents = discord.Intents.all()

bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))
    global guild
    guild = bot.get_guild(1158762932235149452)
    await startup.start(bot)


@bot.event
async def on_member_join(member):
    stat = bot.get_channel(1195315471810039878)
    await welcome.welcome(bot, member, guild)
    await stat.edit(name="『👥』Użytkownicy: " + str(guild.member_count))


@bot.event
async def on_member_remove(member):
    stat = bot.get_channel(1195315471810039878)
    await stat.edit(name="『👥』Użytkownicy: " + str(guild.member_count))


@bot.event
async def on_raw_reaction_add(payload):
    await roles.add(bot, payload, guild)


@bot.event
async def on_raw_reaction_remove(payload):
    await roles.remove(payload, guild)


@bot.slash_command()
async def latency(self):
    await self.respond(str(round(bot.latency * 1000, 2)) + 'ms')


bot.run(os.environ.get("TOKEN"))
