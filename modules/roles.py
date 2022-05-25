import discord
import config


async def add(bot, payload, guild):
    if payload.member == bot.user:
        return
    if payload.channel_id == 963763374133493812:
        await payload.member.add_roles(discord.utils.get(guild.roles, id=config.role[payload.emoji.name]))

    elif payload.channel_id == 963763374133493810:
        if payload.emoji.name != '✅':
            user = guild.get_member(payload.user_id)
            if discord.utils.get(user.roles, id=963763373001048138):
                await payload.member.add_roles(discord.utils.get(guild.roles, id=config.zone[payload.emoji.name]))
        else:
            await payload.member.add_roles(discord.utils.get(guild.roles, id=config.zone[payload.emoji.name]))


async def remove(payload, guild):
    if payload.channel_id == 963763374133493812:
        user = guild.get_member(payload.user_id)
        await user.remove_roles(discord.utils.get(guild.roles, id=config.role[payload.emoji.name]))
    elif payload.channel_id == 963763374133493810:
        if payload.emoji.name != '✅':
            user = guild.get_member(payload.user_id)
            if discord.utils.get(user.roles, id=963763373001048138):
                await user.remove_roles(discord.utils.get(guild.roles, id=config.zone[payload.emoji.name]))
