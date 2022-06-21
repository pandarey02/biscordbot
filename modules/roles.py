import discord
import config
import datetime as dt
from pytz import UTC


async def add(bot, payload, guild):
    if UTC.localize(dt.datetime.utcnow() + dt.timedelta(days=-7)) > payload.member.created_at:
        if payload.member == bot.user:
            return
        if payload.channel_id == 875029163034181633:
            await payload.member.add_roles(discord.utils.get(guild.roles, id=config.role[payload.emoji.name]))

        elif payload.channel_id == 875008016309706773:
            if payload.emoji.name != '✅':
                user = guild.get_member(payload.user_id)
                if discord.utils.get(user.roles, id=875053632217813022):
                    await payload.member.add_roles(discord.utils.get(guild.roles, id=config.zone[payload.emoji.name]))
            else:
                await payload.member.add_roles(discord.utils.get(guild.roles, id=config.zone[payload.emoji.name]))


async def remove(payload, guild):
    if payload.channel_id == 875029163034181633:
        user = guild.get_member(payload.user_id)
        await user.remove_roles(discord.utils.get(guild.roles, id=config.role[payload.emoji.name]))
    elif payload.channel_id == 875008016309706773:
        if payload.emoji.name != '✅':
            user = guild.get_member(payload.user_id)
            if discord.utils.get(user.roles, id=875053632217813022):
                await user.remove_roles(discord.utils.get(guild.roles, id=config.zone[payload.emoji.name]))
