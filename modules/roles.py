import discord
import config
import datetime as dt
from pytz import UTC


async def add(bot, payload, guild):
    if UTC.localize(dt.datetime.utcnow() + dt.timedelta(days=-7)) > payload.member.created_at:
        if payload.member == bot.user:
            return
        if payload.channel_id == 1195316538178293771:
            await payload.member.add_roles(discord.utils.get(guild.roles, id=config.role[payload.emoji.name]))


async def remove(payload, guild):
    if payload.channel_id == 1195316538178293771:
        user = guild.get_member(payload.user_id)
        await user.remove_roles(discord.utils.get(guild.roles, id=config.role[payload.emoji.name]))