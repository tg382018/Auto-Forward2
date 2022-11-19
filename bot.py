import asyncio
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(lineno)d - %(module)s - %(levelname)s - %(message)s'
)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

import uvloop
uvloop.install()
from config import Config
from pyrogram import Client, filters

class channelforward(Client, Config):
    def __init__(self):
        super().__init__(
            name="CHANNELFORWARD",
            bot_token=self.BOT_TOKEN,
            api_id=self.API_ID,
            api_hash=self.API_HASH,
            workers=20,            
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"New session started for {me.first_name}({me.username})")

    async def stop(self):
        await super().stop()
        print("Session stopped. Bye!!")


@channelforward.on_message(filters.channel)
async def forward(client, message):
    # Forwarding the messages to the channel
   try:
      for id in Config.CHANNEL:
         from_channel, to_channel = id.split(":")
         if message.chat.id == int(from_channel):
#           func = message.copy if False else message.forward
            await message.copy(int(to_channel))
            print("Forwarded a message from", from_channel, "to", to_channel)
            await asyncio.sleep(1)
   except Exception as e:
      logger.exception(e)



if __name__ == "__main__" :
    channelforward().run()
