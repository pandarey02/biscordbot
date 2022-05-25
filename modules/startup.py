import config


async def start(bot):
    i = 0
    msg = [963781199770304522, 963781422995345438, 963781510555664434, 974365474580205578]
    for rc in config.rc:
        for e in rc:
            channel = bot.get_channel(963763374133493812)
            msi = await channel.fetch_message(msg[i])
            await msi.add_reaction(e)
        i = i + 1

    channel = bot.get_channel(963763374133493810)
    msg = await channel.fetch_message(974366425118548078)
    await msg.add_reaction('✅')
    for rc in config.rc1:
        msg = await channel.fetch_message(974368463097315378)
        await msg.add_reaction(rc)
