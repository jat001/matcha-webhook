from time import time
from asyncio import sleep
from sanic.log import logger

from . import Window, has_window


patience_start_time = None


class Fishing(Window):

    def __init__(self):
        super().__init__()
        self.key_binding = self.config['fishing']['key_binding']

    @has_window
    async def fish_bite(self, data_type):
        # TODO: global variable sucks
        global patience_start_time
        await sleep(0.2)

        hookset_key = self.key_binding.get('precision_hookset', self.key_binding['hook']) if data_type == 1 \
            else self.key_binding.get('powerful_hookset', self.key_binding['hook'])
        self.post_message(hookset_key)
        # press the hook button anyway to prevent precision_hookset or powerful_hookset not working
        self.post_message(self.key_binding['hook'])

        await sleep(10)
        if self.key_binding.get('patience') and self.config['fishing'].get('patience_timeout'):
            if not patience_start_time or \
                    time() - patience_start_time >= self.config['fishing']['patience_timeout']:
                self.post_message(self.key_binding['patience'])
                patience_start_time = time()
                logger.info('patience started, timeout %ds' % self.config['fishing']['patience_timeout'])
                await sleep(1)

        n = 0
        # TODO: find a way to test when the fish landing
        while n < 5:
            n += 1
            logger.info('%dth cast' % n)
            self.post_message(self.key_binding['cast'])
            await sleep(2)
