# https://discord.com/oauth2/authorize?client_id=1064982556002500678&permissions=8&scope=bot%20applications.commands
import random
from typing import Optional
import discord
from discord import app_commands
import config
from tts import TTS


class ParrotClient(discord.Client):
    def __init__(self, intents) -> None:
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.tree.sync()
        self.tts = TTS()
        self.phrases = [
            "met liefde <3",
            "<3",
            "ok",
            "ok",
            "ok",
            "ok",
            "ok",
            "ok",
            "ok",
            "ok",
            "ok",
            "ok",
            "ok",
            "ok",
            "ok",
            "ok",
            "ok",
            "ok",
            "ok",
            "ok",
            "ok",
            "ok",
            "oke",
            "okee",
            "oki",
            "ja joh, doe maar weer",
            "gast, laat mij maar weer werken",
            "kan je het zelf niet uitspreken",
            "dit bericht zie alleen jij... of toch niet?",
            "ik ben een bot, ik kan niet praten",
        ]

    async def setup_hook(self):
        guild = discord.Object(id=780139459072491550)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

intents = discord.Intents.default()
client = ParrotClient(intents=intents)

@client.tree.command()
@app_commands.describe(
    text = "Text",
    filename = "Filename",
)
async def tts(interaction: discord.Interaction, text: str, filename: Optional[str] = None):
    """Let the Parrot speak for you!"""
    file = client.tts.synthesize(text)
    if filename is None:
        filename = interaction.user.name

    await interaction.response.send_message(random.choice(client.phrases), ephemeral=True)
    await interaction.channel.send(file=discord.File(file, filename=f"{filename}.wav"))
    client.tts.delete_audio(file)

client.run(config.CLIENT_TOKEN)