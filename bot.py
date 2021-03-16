__version__ = "0.1.0"

import os

import discord
from dotenv import load_dotenv

load_dotenv()


class AutoDisconnect(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(activity=discord.Game("get disconnected"), *args, **kwargs)
        self.channel_id = int(os.environ.get("CHANNEL_ID", None))
        self.startup()

    async def on_ready(self):
        print('-' * 24)
        print('Logged in as:')
        print(bot.user.name + "#" + bot.user.discriminator)
        print("Id: " + str(bot.user.id))
        print(f"Discord version: {discord.__version__}")
        print(f"Bot version: {__version__}")
        print('-' * 24)
        print("I am logged in and ready!")

    def startup(self):
        print('=' * 24)
        print("Auto Disconnect")
        print("By: Cyrus")
        print('=' * 24)

    async def on_voice_state_update(self, member, before, after):
        if after.channel:
            if after.channel.id == self.channel_id:
                await member.move_to(None)


bot = AutoDisconnect()

token = os.environ.get("TOKEN", None)
if token is None or len(token.strip()) == 0:
    print("\nA bot token is necessary for the bot to function.\n")
    raise RuntimeError
else:
    bot.run(token)
