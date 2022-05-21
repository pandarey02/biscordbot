from datetime import datetime
import discord
import pytz

time = datetime.now(pytz.timezone('Europe/Warsaw'))


async def create(payload, guild):
    stri = payload.member.name
    pve = guild.get_channel(963763373667930114)
    rp = guild.get_channel(963763373667930115)
    days = guild.get_channel(963763373667930116)
    conan = guild.get_channel(976096325403803648)
    rust = guild.get_channel(976096438117363762)
    rpve = discord.utils.get(guild.roles, id=963763373059764260)
    rrp = discord.utils.get(guild.roles, id=963763373059764259)
    rdays = discord.utils.get(guild.roles, id=963763373059764258)
    rconan = discord.utils.get(guild.roles, id=976101841010049024)
    rrust = discord.utils.get(guild.roles, id=976101842624839720)
    emb = discord.Embed(description='Aby zamknąć ten ticket, zareaguj za pomocą 🔒',
                        colour=discord.Colour.from_rgb(24, 167, 161)).set_footer(
        text="Dinozaur Pimpuś ∙ Dziś o " + time.strftime("%H:%M"))
    emb1 = discord.Embed(title='ticket zamknienty', description='zareaguj za pomocą 🔓 aby otworzyć albo ⛔ aby usunąć',
                         colour=discord.Colour.from_rgb(24, 167, 161)).set_footer(
        text="Dinozaur Pimpuś ∙ Dziś o " + time.strftime("%H:%M"))

    class View2(discord.ui.View):
        @discord.ui.button(label="Otwórz ponownie", row=0, style=discord.ButtonStyle.primary, emoji="🔓")
        async def button_callback(self, button, interaction):
            await channel.edit(name='ticket-{0}'.format(stri.lower()))
            await interaction.response.edit_message(embed=emb, view=View())

        @discord.ui.button(label="Usuń", row=0, style=discord.ButtonStyle.danger, emoji="⛔")
        async def button_callback2(self, button, interaction):
            await channel.delete()

    class View(discord.ui.View):
        @discord.ui.button(label="Zamknij ticket", style=discord.ButtonStyle.primary,
                           emoji="🔒")
        async def button_callback2(self, button, interaction):
            await channel.edit(name='closed-{0}'.format(stri.lower()))
            await interaction.response.edit_message(embed=emb1, view=View2())

    match payload.emoji.name:
        case '1️⃣':
            perm = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True, manage_channels=True),
                rpve: discord.PermissionOverwrite(read_messages=True),
                payload.member: discord.PermissionOverwrite(read_messages=True)
            }
            if discord.utils.get(guild.text_channels, name='ticket-{0}'.format(stri),
                                 category=pve) is None:
                channel = await guild.create_text_channel(name='Ticket-{0}'.format(stri), overwrites=perm,
                                                          category=pve)

                await channel.send(content='Witaj <@{0}> w czym możemy pomóc?'.format(payload.user_id),
                                   embed=emb, view=View())

        case '2️⃣':
            perm = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True, manage_channels=True),
                rrp: discord.PermissionOverwrite(read_messages=True),
                payload.member: discord.PermissionOverwrite(read_messages=True)
            }
            if discord.utils.get(guild.text_channels, name='ticket-{0}'.format(stri),
                                 category=rp) is None:
                channel = await guild.create_text_channel(name='Ticket-{0}'.format(stri), overwrites=perm,
                                                          category=rp)
                await channel.send(content='Witaj <@{0}> w czym możemy pomóc?'.format(payload.user_id),
                                   embed=emb, view=View())

        case '3️⃣':
            perm = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True, manage_channels=True),
                rdays: discord.PermissionOverwrite(read_messages=True),
                payload.member: discord.PermissionOverwrite(read_messages=True)
            }
            if discord.utils.get(guild.text_channels, name='ticket-{0}'.format(stri),
                                 category=days) is None:
                channel = await guild.create_text_channel(name='Ticket-{0}'.format(stri), overwrites=perm,
                                                          category=days)
                await channel.send(content='Witaj <@{0}> w czym możemy pomóc?'.format(payload.user_id),
                                   embed=emb, view=View())

        case '4️⃣':
            perm = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True, manage_channels=True),
                rconan: discord.PermissionOverwrite(read_messages=True),
                payload.member: discord.PermissionOverwrite(read_messages=True)
            }
            if discord.utils.get(guild.text_channels, name='ticket-{0}'.format(stri),
                                 category=conan) is None:
                channel = await guild.create_text_channel(name='Ticket-{0}'.format(stri), overwrites=perm,
                                                          category=conan)
                await channel.send(content='Witaj <@{0}> w czym możemy pomóc?'.format(payload.user_id),
                                   embed=emb, view=View())

        case '5️⃣':
            perm = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True, manage_channels=True),
                rrust: discord.PermissionOverwrite(read_messages=True),
                payload.member: discord.PermissionOverwrite(read_messages=True)
            }
            if discord.utils.get(guild.text_channels, name='ticket-{0}'.format(stri),
                                 category=rust) is None:
                channel = await guild.create_text_channel(name='Ticket-{0}'.format(stri), overwrites=perm,
                                                          category=rust)
                await channel.send(content='Witaj <@{0}> w czym możemy pomóc?'.format(payload.user_id),
                                   embed=emb, view=View())
