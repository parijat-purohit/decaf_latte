import time
import asyncio


class PastaTimer(object):
    def __init__(self):
        self.start, self.end = time.time(), None

    async def boil_pasta(self):
        await asyncio.sleep(5)

    async def prep_items(self):
        await asyncio.sleep(8)

    async def fry_onion(self):
        await asyncio.sleep(3)


batch1 = PastaTimer()

asyncio.run(
    asyncio.gather(
        batch1.boil_pasta(),
        batch1.prep_items(),
        batch1.fry_onion()
    )
)

batch1.end = time.time()
print(f'Total Cooking Time {batch1.end - batch1.start}')
