import asyncio

async def heartbeat():
    while True:
        print("Heartbeat")

        await asyncio.sleep(1) 

async def main():
    await heartbeat()

asyncio.run(main())