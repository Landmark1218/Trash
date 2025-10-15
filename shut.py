import discord
from discord import app_commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = 1292687029611790364 

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        guild = discord.Object(id=GUILD_ID)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

client = MyClient()

@client.tree.command(name="shutdown", description="シャットダウンする")
async def shutdown(interaction: discord.Interaction):
    allowed_users = [1031544096948486225]
    if interaction.user.id not in allowed_users:
        await interaction.response.send_message("権限がありません！", ephemeral=True)
        return

    await interaction.response.send_message("シャットダウンします")
    os.system("shutdown /s /t 1")

client.run(TOKEN)
