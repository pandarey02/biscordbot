async def start(bot):
    rc1 = ['♂️', '♀️']
    rc2 = ['🧡', '🤎', '🤍', '💚', '💙', '🐲', '❤']
    rc3 = ['🐶', '🐱', '🐭', '🐹', '🐹', '🐰', '🦊', '🐻', '🐼', '🐯', '🦁', '🦁', '🐮', '🐸', '🐵', '🐔']
    rc4 = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮']
    rc5 = ['🌱', '⚔', '⛏', '1️⃣', '2️⃣']
    rc6 = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣']
    for rc in rc1:
        channel = bot.get_channel(963763374133493812)
        msg = await channel.fetch_message(963781199770304522)
        await msg.add_reaction(rc)
    for rc in rc2:
        channel = bot.get_channel(963763374133493812)
        msg = await channel.fetch_message(963781422995345438)
        await msg.add_reaction(rc)
    for rc in rc3:
        channel = bot.get_channel(963763374133493812)
        msg = await channel.fetch_message(963781510555664434)
        await msg.add_reaction(rc)
    for rc in rc4:
        channel = bot.get_channel(963763374133493812)
        msg = await channel.fetch_message(974365474580205578)
        await msg.add_reaction(rc)
    channel = bot.get_channel(963763374133493810)
    msg = await channel.fetch_message(974366425118548078)
    await msg.add_reaction('✅')
    for rc in rc5:
        channel = bot.get_channel(963763374133493810)
        msg = await channel.fetch_message(974368463097315378)
        await msg.add_reaction(rc)
    for rc in rc6:
        channel = bot.get_channel(963763373667930120)
        msg = await channel.fetch_message(976080090314194975)
        await msg.add_reaction(rc)
