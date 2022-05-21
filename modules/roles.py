import discord


async def add(bot, payload, guild):
    if payload.member == bot.user:
        return
    if payload.channel_id == 963763374133493812:
        match payload.emoji.name:
            # GENDER
            case '♂️':
                role = discord.utils.get(guild.roles, id=963763373001048137)
                await payload.member.add_roles(role)
            case '♀️':
                role = discord.utils.get(guild.roles, id=963763373001048136)
                await payload.member.add_roles(role)
            # GAMES
            case '🧡':
                role = discord.utils.get(guild.roles, id=963763372422213710)
                await payload.member.add_roles(role)
            case '🤎':
                role = discord.utils.get(guild.roles, id=963763372422213711)
                await payload.member.add_roles(role)
            case '🤍':
                role = discord.utils.get(guild.roles, id=963763372422213709)
                await payload.member.add_roles(role)
            case '💚':
                role = discord.utils.get(guild.roles, id=963763372422213708)
                await payload.member.add_roles(role)
            case '💙':
                role = discord.utils.get(guild.roles, id=963763372833259521)
                await payload.member.add_roles(role)
            case '🐲':
                role = discord.utils.get(guild.roles, id=963763372833259522)
                await payload.member.add_roles(role)
            case '❤':
                role = discord.utils.get(guild.roles, id=963763372422213708)
                await payload.member.add_roles(role)
            # REGION
            case '🐶':
                role = discord.utils.get(guild.roles, id=963763372912935031)
                await payload.member.add_roles(role)
            case '🐱':
                role = discord.utils.get(guild.roles, id=963763372912935030)
                await payload.member.add_roles(role)
            case '🐭':
                role = discord.utils.get(guild.roles, id=963763372912935029)
                await payload.member.add_roles(role)
            case '🐹':
                role = discord.utils.get(guild.roles, id=963763372912935028)
                await payload.member.add_roles(role)
            case '🐹':
                role = discord.utils.get(guild.roles, id=963763372912935027)
                await payload.member.add_roles(role)
            case '🐰':
                role = discord.utils.get(guild.roles, id=963763372912935026)
                await payload.member.add_roles(role)
            case '🦊':
                role = discord.utils.get(guild.roles, id=963763372912935025)
                await payload.member.add_roles(role)
            case '🐻':
                role = discord.utils.get(guild.roles, id=963763372912935024)
                await payload.member.add_roles(role)
            case '🐼':
                role = discord.utils.get(guild.roles, id=963763372912935023)
                await payload.member.add_roles(role)
            case '🐯':
                role = discord.utils.get(guild.roles, id=963763372912935022)
                await payload.member.add_roles(role)
            case '🦁':
                role = discord.utils.get(guild.roles, id=963763372833259529)
                await payload.member.add_roles(role)
            case '🐮':
                role = discord.utils.get(guild.roles, id=963763372833259528)
                await payload.member.add_roles(role)
            case '🐷':
                role = discord.utils.get(guild.roles, id=963763372833259527)
                await payload.member.add_roles(role)
            case '🐸':
                role = discord.utils.get(guild.roles, id=963763372833259526)
                await payload.member.add_roles(role)
            case '🐵':
                role = discord.utils.get(guild.roles, id=963763372833259525)
                await payload.member.add_roles(role)
            case '🐔':
                role = discord.utils.get(guild.roles, id=963763372833259524)
                await payload.member.add_roles(role)
            # AGE
            case '🇦':
                role = discord.utils.get(guild.roles, id=963763372971675687)
                await payload.member.add_roles(role)
            case '🇧':
                role = discord.utils.get(guild.roles, id=963763372971675686)
                await payload.member.add_roles(role)
            case '🇨':
                role = discord.utils.get(guild.roles, id=963763372971675685)
                await payload.member.add_roles(role)
            case '🇩':
                role = discord.utils.get(guild.roles, id=963763372971675684)
                await payload.member.add_roles(role)
            case '🇪':
                role = discord.utils.get(guild.roles, id=963763372971675683)
                await payload.member.add_roles(role)
            case '🇫':
                role = discord.utils.get(guild.roles, id=963763372971675682)
                await payload.member.add_roles(role)
            case '🇬':
                role = discord.utils.get(guild.roles, id=963763372971675681)
                await payload.member.add_roles(role)
            case '🇭':
                role = discord.utils.get(guild.roles, id=963763372971675680)
                await payload.member.add_roles(role)
            case '🇮':
                role = discord.utils.get(guild.roles, id=963763372971675679)
                await payload.member.add_roles(role)
            case _:
                print(payload.emoji.name)
    elif payload.channel_id == 963763374133493810:
        match payload.emoji.name:
            case '✅':
                role = discord.utils.get(guild.roles, id=963763373001048138)
                await payload.member.add_roles(role)
            case '🌱':
                if discord.utils.get(payload.member.roles, id=963763373001048138):
                    role = discord.utils.get(guild.roles, id=963763372422213707)
                    await payload.member.add_roles(role)
            case '⚔':
                if discord.utils.get(payload.member.roles, id=963763373001048138):
                    role = discord.utils.get(guild.roles, id=963763372422213706)
                    await payload.member.add_roles(role)
            case '⛏':
                if discord.utils.get(payload.member.roles, id=963763373001048138):
                    role = discord.utils.get(guild.roles, id=963763372833259520)
                    await payload.member.add_roles(role)
            case '1️⃣':
                if discord.utils.get(payload.member.roles, id=963763373001048138):
                    role = discord.utils.get(guild.roles, id=974369424784097331)
                    await payload.member.add_roles(role)
            case '2️⃣':
                if discord.utils.get(payload.member.roles, id=963763373001048138):
                    role = discord.utils.get(guild.roles, id=974369474805366804)
                    await payload.member.add_roles(role)
            case _:
                print(payload.emoji.name)


async def remove(payload, guild):
    if payload.channel_id == 963763374133493812:
        user = guild.get_member(payload.user_id)
        match payload.emoji.name:
            # GENDER
            case '♂️':
                role = discord.utils.get(guild.roles, id=963763373001048137)
                await user.remove_roles(role)
            case '♀️':
                role = discord.utils.get(guild.roles, id=963763373001048136)
                await user.remove_roles(role)
            # GAMES
            case '🧡':
                role = discord.utils.get(guild.roles, id=963763372422213710)
                await user.remove_roles(role)
            case '🤎':
                role = discord.utils.get(guild.roles, id=963763372422213711)
                await user.remove_roles(role)
            case '🤍':
                role = discord.utils.get(guild.roles, id=963763372422213709)
                await user.remove_roles(role)
            case '💚':
                role = discord.utils.get(guild.roles, id=963763372422213708)
                await user.remove_roles(role)
            case '💙':
                role = discord.utils.get(guild.roles, id=963763372833259521)
                await user.remove_roles(role)
            case '🐲':
                role = discord.utils.get(guild.roles, id=963763372833259522)
                await user.remove_roles(role)
            case '❤':
                role = discord.utils.get(guild.roles, id=963763372422213708)
                await user.remove_roles(role)
            # REGION
            case '🐶':
                role = discord.utils.get(guild.roles, id=963763372912935031)
                await user.remove_roles(role)
            case '🐱':
                role = discord.utils.get(guild.roles, id=963763372912935030)
                await user.remove_roles(role)
            case '🐭':
                role = discord.utils.get(guild.roles, id=963763372912935029)
                await user.remove_roles(role)
            case '🐹':
                role = discord.utils.get(guild.roles, id=963763372912935028)
                await user.remove_roles(role)
            case '🐹':
                role = discord.utils.get(guild.roles, id=963763372912935027)
                await user.remove_roles(role)
            case '🐰':
                role = discord.utils.get(guild.roles, id=963763372912935026)
                await user.remove_roles(role)
            case '🦊':
                role = discord.utils.get(guild.roles, id=963763372912935025)
                await user.remove_roles(role)
            case '🐻':
                role = discord.utils.get(guild.roles, id=963763372912935024)
                await user.remove_roles(role)
            case '🐼':
                role = discord.utils.get(guild.roles, id=963763372912935023)
                await user.remove_roles(role)
            case '🐯':
                role = discord.utils.get(guild.roles, id=963763372912935022)
                await user.remove_roles(role)
            case '🦁':
                role = discord.utils.get(guild.roles, id=963763372833259529)
                await user.remove_roles(role)
            case '🐮':
                role = discord.utils.get(guild.roles, id=963763372833259528)
                await user.remove_roles(role)
            case '🐷':
                role = discord.utils.get(guild.roles, id=963763372833259527)
                await user.remove_roles(role)
            case '🐸':
                role = discord.utils.get(guild.roles, id=963763372833259526)
                await user.remove_roles(role)
            case '🐵':
                role = discord.utils.get(guild.roles, id=963763372833259525)
                await user.remove_roles(role)
            case '🐔':
                role = discord.utils.get(guild.roles, id=963763372833259524)
                await user.remove_roles(role)
            # AGE
            case '🇦':
                role = discord.utils.get(guild.roles, id=963763372971675687)
                await user.remove_roles(role)
            case '🇧':
                role = discord.utils.get(guild.roles, id=963763372971675686)
                await user.remove_roles(role)
            case '🇨':
                role = discord.utils.get(guild.roles, id=963763372971675685)
                await user.remove_roles(role)
            case '🇩':
                role = discord.utils.get(guild.roles, id=963763372971675684)
                await user.remove_roles(role)
            case '🇪':
                role = discord.utils.get(guild.roles, id=963763372971675683)
                await user.remove_roles(role)
            case '🇫':
                role = discord.utils.get(guild.roles, id=963763372971675682)
                await user.remove_roles(role)
            case '🇬':
                role = discord.utils.get(guild.roles, id=963763372971675681)
                await user.remove_roles(role)
            case '🇭':
                role = discord.utils.get(guild.roles, id=963763372971675680)
                await user.remove_roles(role)
            case '🇮':
                role = discord.utils.get(guild.roles, id=963763372971675679)
                await user.remove_roles(role)
            case _:
                print(payload.emoji.name)
    elif payload.channel_id == 963763374133493810:
        user = guild.get_member(payload.user_id)
        match payload.emoji.name:
            case '✅':
                role = discord.utils.get(guild.roles, id=963763373001048138)
                await user.remove_roles(role)
            case '🌱':
                if discord.utils.get(user.roles, id=963763373001048138):
                    role = discord.utils.get(guild.roles, id=963763372422213707)
                    await user.remove_roles(role)
            case '⚔':
                if discord.utils.get(user.roles, id=963763373001048138):
                    role = discord.utils.get(guild.roles, id=963763372422213706)
                    await user.remove_roles(role)
            case '⛏':
                if discord.utils.get(user.roles, id=963763373001048138):
                    role = discord.utils.get(guild.roles, id=963763372833259520)
                    await user.remove_roles(role)
            case '1️⃣':
                if discord.utils.get(user.roles, id=963763373001048138):
                    role = discord.utils.get(guild.roles, id=974369424784097331)
                    await user.remove_roles(role)
            case '2️⃣':
                if discord.utils.get(user.roles, id=963763373001048138):
                    role = discord.utils.get(guild.roles, id=974369474805366804)
                    await user.remove_roles(role)
            case _:
                print(payload.emoji.name)
