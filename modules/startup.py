import config


async def start(bot):
    i = 0
    msg = [1195319030416949338, 1195320155031478292]
    for rc in config.rc:
        for e in rc:
            channel = bot.get_channel(1195316538178293771)
            msi = await channel.fetch_message(msg[i])
            await msi.add_reaction(e)
        i = i + 1

    channel = bot.get_channel(1195316538178293771)
