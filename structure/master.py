from datetime import datetime

from discord.ext import commands

from structure.providers.helper import get_time


class MasterCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.uptime = datetime.now()

    def get_uptime(self):
        return self.uptime

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user} with {len(self.bot.guilds)} guild(s) at {get_time()}")


async def setup(bot):
    await bot.add_cog(MasterCog(bot))
