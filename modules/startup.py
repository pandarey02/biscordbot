import config


async def start(bot):
    i = 0
    msg = [979066932760301568, 979066989798629406, 979067030609207387, 979067154269888593]
    for rc in config.rc:
        for e in rc:
            channel = bot.get_channel(963763374133493812)
            msi = await channel.fetch_message(msg[i])
            await msi.add_reaction(e)
        i = i + 1

    channel = bot.get_channel(963763374133493810)
    msg = await channel.fetch_message(979070646246068234)
    await msg.add_reaction('✅')
    for rc in config.rc1:
        msg = await channel.fetch_message(979070956687466506)
        await msg.add_reaction(rc)
