import asyncio


async def fetch(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)   # <-- yields control here
    print(f"{name} finished")
    return name


async def main():
    tasks = [
        asyncio.create_task(fetch("A", 2)),
        asyncio.create_task(fetch("B", 10)),  # slow I/O
        asyncio.create_task(fetch("C", 3)),
        asyncio.create_task(fetch("D", 1)),
    ]

    results = await asyncio.gather(*tasks)
    print("All done:", results)

asyncio.run(main())


s = 'A8S9W3'
chars = []
nums = []

for st in s:
    if 'A' <= st <= 'Z' or 'a' <= st <= 'z':
        chars.append(st)
    else:
        nums.append(st)
chars.sort()
nums.sort()
print("".join(chars) + "".join(nums))
