import nextcord
from nextcord.ext import commands
import time

client = commands.Bot(command_prefix="EstudaFQ ", intents=nextcord.Intents.all())

class ping_cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def ping(self, ctx):
        before = time.monotonic()
        message = await ctx.send('Um momento...')
        ping = (time.monotonic() - before) * 1000
        if ping < 200:
            color = 0x35fc03
        elif ping < 350:
            color = 0xe3f51d
        elif ping < 500:
            color = 0xf7700f
        else:
            color = 0xf7220f
        pEmbed = nextcord.Embed(title="Como estou:", color=color)
        pEmbed.add_field(name="Latência", value=f'{int(ping)}ms')
        pEmbed.add_field(name="API", value=f'{round(self.bot.latency * 1000)}ms')
        pEmbed.set_thumbnail(url=self.bot.user.avatar_url)
        await message.edit(content=None, embed=pEmbed)

def setup(bot):
    bot.add_cog(ping_cmd(bot))