import discord

class main(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    @commands.command(
        name="say",
        description="say",
        usage="say <message>",
    )
    async def say(self, *, message: str) -> None:
        await ctx.channel.send(message)