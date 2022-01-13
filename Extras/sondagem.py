import nextcord
from nextcord.ext import commands
import asyncio
client = commands.Bot(command_prefix="EstudaFQ ", intents=nextcord.Intents.all())

class Sondagem(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
    @commands.command()
    async def sondagem(self, ctx):

      """EstudaFQ sondagem canal Título#Descrição#tempo(em segundos)#sim"""
      
      if ctx.author.guild_permissions.administrator or ctx.author.id == 398068173275922433:
        
        perguntas=['Em que canal?', 'Por quanto tempo(em segundos [1h=3600s])?', 'Título:', 'Descrição', 'Queres adicionar a opção de indiferença("🤷")']
        respostas = []

        def checki(mensagem):
          return mensagem.author == ctx.author and mensagem.channel == ctx.channel

        for pergunta in perguntas:
          await ctx.send(pergunta)

          try:
            
            msg = await client.wait_for('message', timeout=15.0, check=checki)
          except asyncio.TimeoutError:

            await ctx.send('Não respondes-te a tempo, tenta ser mais rápido na próxima vez ')
            return
          else:
            respostas.append(msg.content)

        try:
            id_canal = int(respostas[0][2:-1])
        except:
            await ctx.send(f"Não mencionaste um canal válido. Fá-lo assim: {ctx.channel.mention} da próxima vez")

        tempo = int(respostas[1])
        canal = client.get_channel(id_canal)
        

        if len(respostas) != 5:
          await canal.send("Algo deu errado.")

        else:

          carta=nextcord.Embed(title=respostas[2], description=respostas[3])
          mandar_carta = await canal.send(embed=carta)
          confirmacao = await ctx.channel.send(f"Olá {ctx.author.mention}!")
          await asyncio.sleep(3)
          await confirmacao.edit(content=f"Sondagem enviada para `{canal}` com a duração de `{tempo}` segundos")

          await mandar_carta.add_reaction("👍")  

          
          if respostas[4] == "sim" or respostas[4] == "Sim":

            await mandar_carta.add_reaction("🤷")
            await canal.send('🤷 `Significa que te é indiferente.`')
          elif respostas[4] == "não" or respostas[4] == "Não" or respostas[4] == "nao" or respostas[4] == "Nao":
            pass
          else:
            await canal.send("A última palavra do comando tem quer um sim ou não, no caso de quereres ou não um emoji que represente a indeferenciação do utilizador perante a pergunta.", delete_after = 10)

          await mandar_carta.add_reaction("👎")
          await asyncio.sleep(tempo)
          y = await canal.fetch_message(id=mandar_carta.id)
          x = y.reactions
          counts = [r.count for r in x]
          print(y.reactions)
          print(counts)
          emojis = [r.emoji for r in x]
          print(emojis)
          b =  "🤷" in emojis
          print(b)

          
          if b and (x[0].count > x[2].count) and (x[0].count > x[1].count):

            msg_1 = nextcord.Embed(title="Pela sondagem", url = mandar_carta.jump_url, description=f"{ctx.author.mention} Pela sondagem, parece que há **muita gente a favor**.")
            await canal.send(embed=msg_1)

          elif b and (x[2].count > x[0].count) and (x[2].count > x[1].count):
    
            msg_1 = nextcord.Embed(title="Pela sondagem", url = mandar_carta.jump_url, description=f"{ctx.author.mention} Pela sondagem, parece que é **pouco apoiado**.")
            await canal.send(embed=msg_1)


          elif b and (x[1].count > x[0].count) and (x[1].count > x[2].count):
            
            msg_1 = nextcord.Embed(title="Pela sondagem", url = mandar_carta.jump_url, description=f"{ctx.author.mention} Pela sondagem, parece que é **indiferente**.")
            await canal.send(embed=msg_1)
          

          elif (x[0].count > x[1].count):
            
            msg_1 = nextcord.Embed(title="Pela sondagem", url = mandar_carta.jump_url, description=f"{ctx.author.mention} Pela sondagem, parece que há **muita gente a favor**.")
            await canal.send(embed=msg_1)

          elif (x[1].count > x[0].count):
            msg_1 = nextcord.Embed(title="Pela sondagem", url = mandar_carta.jump_url, description=f"{ctx.author.mention} Pela sondagem, parece que é **pouco apoiado**.")
            await canal.send(embed=msg_1)


          else:
            msg_1 = nextcord.Embed(title="Pela sondagem", url = mandar_carta.jump_url, description=f"{ctx.author.mention} Temos um famoso **empate**.")
            await canal.send(embed=msg_1)
      else:
        await ctx.channel.send("faltam-te as `permissões` para usares este comando", delete_after = 8)

    @commands.command()
    async def mute(self, ctx, member: commands.MemberConverter):
      canal = ctx.channel
      guild = self.bot.get_guild(654400102550732804)
      ajudantes = guild.get_role(821168509844979722)
      prof = guild.get_role(702557003339268168)

      if (not ajudantes in ctx.author.roles) or (not prof in ctx.author.roles):
        if ctx.author.id == member.id:
          ctx.send('Não convém votares para te auto-silenciares.')
        elif (ajudantes in member.roles) or (prof in member.roles):
          await ctx.author.edit(roles=[])
          muted = guild.get_role(role_id=839826590209015828)
          await ctx.author.add_roles(muted)
          await ctx.send(f' Boa tentativa {member.mention}.')

        else:
          carta=nextcord.Embed(title=f"Devo proibir o utilizador {member} de mandar mais mensagens?", description="O resultado da votação corresponderá à minha decisão")
          mandar_carta = await canal.send(embed=carta)
        
        

          await mandar_carta.add_reaction("✔️")
          await mandar_carta.add_reaction("❌")

          await asyncio.sleep(10)

          y = await canal.fetch_message(id=mandar_carta.id)
          x = y.reactions

          if (x[0].count > x[1].count):
              
            msg_1 = nextcord.Embed(title="Pela sondagem", url = mandar_carta.jump_url, description=f"O utilizador {member.mention} foi silenciado. ")
            await canal.send(embed=msg_1)

            await member.edit(roles=[])
            guild = self.bot.get_guild(id=654400102550732804)
            muted = guild.get_role(role_id=839826590209015828)
            await member.add_roles(muted)


          elif (x[1].count > x[0].count):
            msg_1 = nextcord.Embed(title="Pela sondagem", url = mandar_carta.jump_url, description=f"{ctx.author.mention} Pela sondagem, parece que é **pouco apoiado**.O utilizador {member.mention} não será silenciado. ")
            await canal.send(embed=msg_1)


          else:
          
            msg_1 = nextcord.Embed(title="Pela sondagem", url = mandar_carta.jump_url, description=f"Embora tenhemos um **empate**. O utilizador {member.mention} será silenciado.")
            await canal.send(embed=msg_1)


            await member.edit(roles=[])
            
            await member.add_roles(None)

      else:
        if ctx.author.id != member.id:
          await member.edit(roles=[])
          await member.add_roles(None)
          await ctx.send(f'O utilizador {member.mention} foi silenciado.')
        else:
          await ctx.send('Não convém.')


def setup(bot):
    bot.add_cog(Sondagem(bot))
