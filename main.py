import nextcord
import asyncio
import random
import os
from nextcord.ext import commands, tasks
from nextcord import Interaction, SlashOption, ChannelType
import datetime
Token = "ODI5ODEwNzAyMjg0ODgxOTgw.YG9jcA.X-EJyQgiFpeSdfzdcYGQ_pYnhBE"
client = commands.Bot(command_prefix="EstudaFQ ", intents=nextcord.Intents.all())


#guild = client.get_guild(654400102550732804)
#aprendizes = guild.get_role(813122194477285376)
#await message.author.add_roles(aprendizes) anuncia




palavras_de_ajuda = ["ajuda", "não entendo", "nao entendo", "não percebi", "alguém sabe", "alguém me consegue", "não estou a perceber", "nao estou entend", "alguem consegue", "nao perceb", "nao percebo", "não percebo", "alguem sabe", "não estou entend", "alguem me conseg", "nao estou a perceber", "alguem me ajuda", "preciso de saber", "Estou com dúvidas", "estou com dúvidas", "Estou com duvidas",
"estou com duvidas", "Ajudem-me", "ajudem-me", "ajudem", "Ajudem", "tenho uma dúvida", "tenho uma duvida", "Tenho uma dúvida", "Tenho uma duvida"]

agradecimentos = ["ajudado", "Ajudado", "pela ajuda", "Pela ajuda","queres ajuda?", "não consigo ajudar", "nao consigo ajudar", "não consigo ajudar", "nao consigo te", "não consigo te"]

resposta_a_ajuda = "<@&821168509844979722>"


@client.event
async def on_ready():
    await client.change_presence(status=nextcord.Status.idle, activity=nextcord.Game('Estuda FQ! https://estudafq.pt/'))
    print("Estou online")
    #turns on discord components lib

canal_fisica_id = 702558110618877963
canal_quimica_id = 865689817306890260
canal_alem_id = 865691059631161344
canal_bots_id = 763803093308538911
canal_11_id = 702572234392207481
canal_10_id = 702572171897077892



@client.event
async def on_message(message):
    await client.process_commands(message)

    if message.author == client.user:
        return

    if message.channel.id == 865424335475703808 and (message.content == "Concordo com as regras, obrigado." or message.content == "Concordo com as regras, obrigado" or message.content == "Concordo com as regras,obrigado." or message.content == "Concordo com as regras,obrigado" or message.content == "concordo com as regras,obrigado"):
        guild = client.get_guild(654400102550732804)
        aprendizes = guild.get_role(813122194477285376)
        await message.author.add_roles(aprendizes)


    if message.channel.id == 865424335475703808 and message.content != "jwbjvbejwbjvbwjbjkbwkb":
        await message.delete()

    if message.channel.id != 702559343911895041 and (message.content.startswith(".p") or message.content.startswith(".s")):
        guild = client.get_guild(654400102550732804)
        muted = guild.get_role(839826590209015828)
        await message.author.add_roles(muted)
        await message.channel.send(f"{message.author.mention} como não usaste o canal <#702559343911895041>, foi-te atribuída a role 'muted'. Contudo, podes continuar na chamada e ouvir a música que pedis-te.")


    if message.channel.id == 702573944687034411 and not "htt" in message.content:
        await message.delete()

    if (message.channel.id == canal_bots_id or message.channel.id == canal_fisica_id or message.channel.id == canal_11_id or message.channel.id == canal_10_id or message.channel.id == canal_alem_id or message.channel.id == canal_quimica_id) and any(word in message.content for word in agradecimentos):
        pass

    else:

        if (message.channel.id == canal_bots_id or message.channel.id == canal_fisica_id or message.channel.id == canal_11_id or message.channel.id == canal_10_id or message.channel.id == canal_alem_id or message.channel.id == canal_quimica_id) and any(word in message.content for word in agradecimentos):
            if not message.author.guild_permissions.mute_members:
                await message.channel.send(resposta_a_ajuda)

    if message.channel.id == 862368879401238559:

        if message.content.startswith("Posso participar na aula por favor?"):

            membro = message.author

            try:
                aprovacao = client.get_channel(862368596449427476)

                if membro not in aprovacao.members:

                    await message.channel.send(f"{message.author.mention} Não estás no canal de aprovação. Caso esteja cheio, **espera** até que esvazie, junta-te e volta a pedir.")
                    await message.delete()


                else:
                    await message.channel.send(f"{membro.mention} Espera pela tua aprovação.")
                    canal = client.get_channel(862407284290093056)



                    carta = nextcord.Embed(title = f"Aprovação de {membro}", description = f"Nickname = **{membro.nick}**")
                    carta.add_field(name='Juntou-se ao servidor(ano/mês/dia):', value=f"{membro.joined_at.date()}")
                    carta.set_image(url = membro.avatar)

                    msg_carta = await canal.send(embed=carta)
                    await msg_carta.add_reaction("✅")
                    await msg_carta.add_reaction("❌")


                    await asyncio.sleep(10)

                    y = await canal.fetch_message(msg_carta.id)
                    x = y.reactions

                    with open('canal.txt', 'r') as sala:

                        linhas = sala.readlines()

                        vc = linhas[-1]
                        canal_de_voz = client.get_channel(int(vc))



                        if (x[0].count > x[1].count):

                            guild = client.get_guild(654400102550732804)
                            em_aula = guild.get_role(865620701168140288)


                            await membro.move_to(canal_de_voz)
                            await membro.add_roles(em_aula)
                            await message.delete()

                            await message.channel.send(f"{membro.mention} Foste autorizado a entrar na sala.")

                        elif (x[0].count < x[1].count):

                            await message.delete()
                            await message.channel.send(f"{membro.mention} Não foste autorizado a entrar na sala.")
                            await membro.move_to(None)

                        else:

                            await message.delete()
                            await message.channel.send(f"{membro.mention} Não foste autorizado a entrar na sala.")

                            await msg_carta.reply("Como ninguém votou, neguei o acesso.")
                            await membro.move_to(None)



            except Exception as e:
                await canal.send(e)

                await message.channel.send(f"{membro.mention} saíste do canal de aprovação antes da tua aprovação ser considerada. ")



        else:
            await message.delete()

@client.event
async def on_voice_state_update(membro:nextcord.Member, antes:nextcord.VoiceState, depois:nextcord.VoiceState):
    try:

        with open('canal.txt', 'r') as ficheiro:

            linhas = ficheiro.readlines()

            vc = linhas[-1]


            if antes.channel.id == int(vc):
                guild = client.get_guild(654400102550732804)
                em_aula = guild.get_role(865620701168140288)
                await membro.remove_roles(em_aula)




    except:
        pass


extensions = ['Extras.ping_cmd', 'Extras.sondagem', 'Extras.help']

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)


def convert(tempo):
    pos = ["s", "m", "h", "d"]
    tempo_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : 24*3600}
    unidade = tempo[-1]

    if unidade not in pos:
        return -1
    try:
        valor = int(tempo[:-1])
    except:
        return -2

    return valor * tempo_dict[unidade]


@client.command()
@commands.has_role("El Professor")
async def giveaway(ctx):
    await ctx.send("Responde a estas perguntas, tens 15 segundos!")

    perguntas = ["Em qual canal?", "Quanto tempo? (s|m|h|d)", "Qual é o prémio?" ]

    respostas = []

    def check(mensagem):
        return mensagem.author == ctx.author and mensagem.channel == ctx.channel

    for pergunta in perguntas:
        await ctx.send(pergunta)

        try:
            msg = await client.wait_for('message', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('Não respondes-te a tempo, tenta ser mais rápido na próxima vez ')
            return
        else:
            respostas.append(msg.content)

    try:
        id_canal = int(respostas[0][2:-1])
    except:
        await ctx.send(f"Não mencionaste um canal válido. Fá-lo assim: {ctx.channel.mention} da próxima vez")

    canal = client.get_channel(id_canal)

    tempo = convert(respostas[1])

    if tempo == -1:
        await ctx.send("Não colocas-te o tempo com a unidade certa. Usa s|m|h|d da próxima vez!  ")
        return
    elif tempo == -2:
        await ctx.send("O tempo tem que ser um número seguido de s|m|h|d !")
        return

    premio = respostas[2]

    await ctx.send(f"O *Giveaway* vai estar no canal {canal.mention} e irá durar {respostas[1]}!")

    embed = nextcord.Embed(title="Giveaway!", description=f"{premio}", color = ctx.author.color)

    embed.add_field(name="Anfitrião:", value = ctx.author.mention)

    embed.set_footer(text=f"Acaba em {respostas[1]} a partir deste momento!")

    gw_msg = await canal.send(embed=embed)

    await gw_msg.add_reaction("🎉")

    await asyncio.sleep(tempo)

    gw_msg_reacao = await canal.fetch_message(gw_msg.id)

    participantes = await gw_msg_reacao.reactions[0].users().flatten()
    participantes.pop(participantes.index(client.user))

    vencedor = random.choice(participantes)

    await canal.send(f"Boa! {vencedor.mention} ganhaste {premio}:   {gw_msg_reacao.jump_url}")

@client.command()
@commands.has_role("El Professor")
async def novo(ctx, canal : nextcord.TextChannel, id_ : int):
    try:
        gw_msg_reacao = await canal.fetch_message(id_)

    except Exception as e:
        await ctx.send(f"Id incorreto. {e}")
        return
    participantes = await gw_msg_reacao.reactions[0].users().flatten()
    participantes.pop(participantes.index(client.user))

    vencedor = random.choice(participantes)

    await canal.send(f"E o novo vencedor é {vencedor.mention}!")

@client.command()
@commands.has_role("El Professor")
async def anuncia(ctx):
    perguntas = ["Em que canal?", "Que mensagem devo enviar?", "Queres que envie uma imagem também? (Envia a imagem se sim, ou digita nao para terminares!)"]

    contador = 0

    respostas = []

    def check(mensagem):
        return mensagem.author == ctx.author and mensagem.channel == ctx.channel

    for pergunta in perguntas:
        contador += 1

        await ctx.send(pergunta)

        try:


            msg = await client.wait_for('message', timeout=30.0, check=check)

            if contador == 3:

                try:

                    respostas.append(msg.content)


                    if respostas[2] == "nao":
                        respostas.insert(3, '')

                        break

                    else:


                        msg_id = msg.id
                        canal = ctx.channel

                        msg_1 = await canal.fetch_message(msg_id)
                        imagem = msg_1.attachments[0].url

                        respostas.append(imagem)

                except:

                    await ctx.channel.send("Coloca a imagem se fôr o caso ou apenas coloca 'nao' da próxima vez!")
                    return



        except asyncio.TimeoutError:
            await ctx.send('Não respondes-te a tempo, tenta ser mais rápido na próxima vez ')
            return


        else:
            respostas.append(msg.content)

    try:
        id_canal = int(respostas[0][2:-1])

    except:
        await ctx.send(f"Não mencionaste um canal válido. Fá-lo assim: {ctx.channel.mention} da próxima vez")







    canal = client.get_channel(id_canal)
    print(respostas)
    msg = await canal.send(f"{respostas[1]}                                                           {respostas[3]}")
    await ctx.send("Mensagem enviada!")



@client.command()
async def avatar(ctx, membro: commands.MemberConverter):



    carta = nextcord.Embed(title = "Avatar:")
    carta.set_image(url = membro.avatar)
    carta.set_author(name = membro, icon_url = membro.avatar)

    await ctx.send(embed = carta)



@client.command()
async def sala(ctx, canal:nextcord.VoiceChannel):
    with open('canal.txt', 'w') as canal_voz:

        canal_voz.write(str(canal.id))

    await ctx.send(f"Moverei agora os membros aprovados para o canal de voz `{canal}`")



player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def galo(ctx, p1: nextcord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = ctx.author

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("É a vez de <@" + str(player1.id) + ">.")
        elif num == 2:
            turn = player2
            await ctx.send("é a vez de <@" + str(player2.id) + ">.")
    else:
        await ctx.send("Aacaba o teu jogo anterior para poderes começar um novo")

@client.command()
async def joga(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " ganham!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("Temos um empate!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Verifica se introduziste um número entre 1 e 9(inclusive) numa posição válida.")
        else:
            await ctx.send("Espera pela tua vez..")
    else:
        await ctx.send(f"Convém começares um jogo com o comando `{client.command_prefix}galo`")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@galo.error
async def galo_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Menciona um jogador.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Tenta mencionar jogadores assim: <@id>.")

@joga.error
async def joga_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Insere a posição onde gostarias de jogar.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Verifica se inroduziste um número")



@client.slash_command(guild_ids=[654400102550732804])
async def silenciar(
    interaction=Interaction,
    membro: nextcord.Member = SlashOption(name="membro", description="Qual membro?", required=True),
    tempo: int = SlashOption(name="tempo", description="Por quanto tempo?(segundos)", required=False, default='Tempo não especificado.'),
    razão: str = SlashOption(name="razão", description="Razão?", required=False, default="Razão não dada.")
    ):
        guild = client.get_guild(654400102550732804)
        owner = guild.get_role(702557003339268168)
        ajudantes = guild.get_role(821168509844979722)
        if owner in interaction.user.roles or ajudantes in interaction.user.roles:
    


            muted = guild.get_role(839826590209015828)
            await membro.edit(roles=[muted])
            aprendizes = guild.get_role(813122194477285376)
            await membro.add_roles(muted)
            time = tempo
            if type(tempo)==int:
                tempo = str(tempo)+' segundos.'




            await membro.send(
                    
                embed=nextcord.Embed(
                    title="Foste silenciado!",
                    color=nextcord.Color.dark_red()
                    ).add_field(
                        name="**Info:**",
                        value=f"""
                        \n**Silenciado no server**:\n {guild.name} ({guild.id})
                        \n**Por**:\n {tempo}
                        \n**Responsável**:\n {interaction.user.mention} ({interaction.user.id})
                                """,
                        inline = False
                        
                        ).add_field(

                            name="\n**Razão:**",
                            value=f"{razão}",
                            inline = False

                        )

                )
            await interaction.channel.send(embed=nextcord.Embed(
                title="Silenciado!",
                color=nextcord.Color.green(),
                
                ).add_field(
                    name="**Info:**",
                    value=f"""
                    \n**Silenciado**:\n {membro.mention} ({membro.id})
                    \n**Por**:\n {tempo}
                    \n**Responsável**:\n {interaction.user.mention} ({interaction.user.id})
                    """,
                    inline=False
                ).add_field(
                    name="**Razão:**",
                    value=f"{razão}",
                    inline=False
                )
            )

            if tempo != 'Não especificado.':
                await asyncio.sleep(time)
                await membro.edit(roles=[aprendizes])
        else:
            await interaction.channel.send(f'Não tens permissões para usar este comando {interaction.user.mention}.')
            

































@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '** Só podes votar para dar mute de novo em {:.2f}s**'.format(error.retry_after)
        await ctx.send(msg)
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Esse comando não existe!')

    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Faltam-te as ` perms ` para usares este comando!')




client.run(os.getenv('token'))
