from datetime import datetime
import discord
import pytz

time = datetime.now(pytz.timezone('Europe/Warsaw'))


async def ticket(bot, guild):
    emb = discord.Embed(description='Aby zamknąć ten ticket naciśnij 🔒',
                        colour=discord.Colour.from_rgb(24, 167, 161)).set_footer(
        text="Dinozaur Pimpuś ∙ Dziś o " + time.strftime("%H:%M"))
    emb1 = discord.Embed(title='ticket zamknienty', description='Naciśnij 🔓 aby otworzyć ticket albo ⛔ aby usunąć',
                         colour=discord.Colour.from_rgb(24, 167, 161)).set_footer(
        text="Dinozaur Pimpuś ∙ Dziś o " + time.strftime("%H:%M"))

    class View2(discord.ui.View):
        @discord.ui.button(label="Otwórz ponownie", row=0, style=discord.ButtonStyle.primary, emoji="🔓")
        async def button_callback(self, button, interaction):
            chan = interaction.channel
            n = interaction.channel.name
            number = n.split('-')
            await chan.edit(name='ticket-{0}'.format(number[1]))
            await interaction.response.edit_message(embed=emb, view=View())

        @discord.ui.button(label="Usuń", row=0, style=discord.ButtonStyle.danger, emoji="⛔")
        async def button_callback2(self, button, interaction):
            chan = interaction.channel
            await chan.delete()

    class View(discord.ui.View):
        @discord.ui.button(label="Zamknij ticket", style=discord.ButtonStyle.primary, emoji="🔒")
        async def button_callback2(self, button, interaction):
            chan = interaction.channel
            n = interaction.channel.name
            number = n.split('-')
            await chan.edit(name='closed-{0}'.format(number[1]))
            await interaction.response.edit_message(embed=emb1, view=View2())

    class MyView(discord.ui.View):
        @discord.ui.select(
            placeholder="Wybierz Kategorie Pomocy",
            min_values=1,
            max_values=1,
            options=[
                discord.SelectOption(
                    label='PVE',
                    description="Pick this if you like vanilla!"
                ),
                discord.SelectOption(
                    label='RP',
                    description="Pick this if you like chocolate!"
                ),
                discord.SelectOption(
                    label='7DAYS',
                    description="Pick this if you like strawberry!"
                ),
                discord.SelectOption(
                    label='RUST',
                    description="Pick this if you like vanilla!"
                ),
                discord.SelectOption(
                    label='CONNAN',
                    description="Pick this if you like chocolate!"
                )
            ]
        )
        async def select_callback(self, select, interaction):
            cat = {
                'PVE': guild.get_channel(963763373667930114),
                'RP': guild.get_channel(963763373667930115),
                '7DAYS': guild.get_channel(963763373667930116),
                'RUST': guild.get_channel(976096325403803648),
                'CONNAN': guild.get_channel(976096438117363762)

            }
            role = {
                'PVE': discord.utils.get(guild.roles, id=963763373059764260),
                'RP': discord.utils.get(guild.roles, id=963763373059764259),
                '7DAYS': discord.utils.get(guild.roles, id=963763373059764258),
                'RUST': discord.utils.get(guild.roles, id=976101841010049024),
                'CONNAN': discord.utils.get(guild.roles, id=976101842624839720)
            }
            ch = await guild.create_text_channel(name='Ticket-{0}'.format(len(cat[select.values[0]].channels) + 1),
                                                 category=cat[select.values[0]])
            await ch.send(content='Witaj <@{0}> w czym możemy pomóc?'.format(interaction.user.id),
                          embed=emb, view=View())

    channel = bot.get_channel(963763373667930120)
    msg = await channel.fetch_message(978965800981495828)
    await msg.edit(view=MyView())
