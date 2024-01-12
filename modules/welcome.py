import datetime as dt
import discord
from pytz import timezone, UTC


async def welcome(bot, member, guild):
    time = dt.datetime.now(timezone('Europe/Warsaw'))
    if UTC.localize(dt.datetime.utcnow() + dt.timedelta(days=-7)) > member.created_at:
        emb = discord.Embed(title=member,
                            description='Witaj na serwerze 1 roku informatyki, Jesteś naszym {0} użytkownikiem'.format(
                                guild.member_count) + '\n Zapoznaj się z <#1158767794104565852>',
                            colour=discord.Colour.from_rgb(158, 36, 154)).set_thumbnail(
            url="https://imgur.com/a/Y2IVqQH").set_footer(text="Helpdeskbot ∙ Dziś o " + time.strftime("%H:%M"))
        channel = bot.get_channel(1195318251836682280)
        await channel.send(embed=emb)
