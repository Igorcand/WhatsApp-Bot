import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '?regras':
            await message.channel.send(f'{message.author.name} as regras do servidor são: {os.linesep}1-Nâo desrespeitar os membros{os.linesep}2-Regra Importante')
        elif message.content == '?nivel':
            await message.author.send('Nivel 1')
    async def on_member_join(self,member):
        guild = member.guild
        if guild.system_channel is not None:
            message = f'{member.mention} acabou de entrar no {guild.name}'
            await guild.system_channel.send(message)


intents = discord.Intents.default()
intents.members = True
client = MyClient(intents=intents)
client.run('ODk1Mjg1NTE5NDUyMzQwMjQ0.YV2VnQ.NrF99YmdHHbmq6X6Up5ASFNyfTE')