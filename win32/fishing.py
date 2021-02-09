from asyncio import sleep

from . import Window


class Fishing(Window):

    async def fish_bite(self):
        await sleep(0.2)
        self.post_message(self.config['key_binding']['fishing']['hook'])
        await sleep(10)
        self.post_message(self.config['key_binding']['fishing']['cast'])
