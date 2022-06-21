import datetime as dt
import discord
from pytz import timezone, UTC


async def welcome(bot, member, guild):
    time = dt.datetime.now(timezone('Europe/Warsaw'))
    if UTC.localize(dt.datetime.utcnow() + dt.timedelta(days=-7)) > member.created_at:
        emb = discord.Embed(title=member,
                            description='Witaj na serwerze, Jesteś naszym {0} użytkownikiem'.format(
                                guild.member_count) + '\n Zapoznaj się z <#963763374133493810>',
                            colour=discord.Colour.from_rgb(24, 167, 161)).set_thumbnail(
            url="https://i.imgur.com/KcTxK73.png").set_footer(text="Dinozaur Pimpuś ∙ Dziś o " + time.strftime("%H:%M"))
        channel = bot.get_channel(963763374133493811)
        await channel.send(embed=emb)
