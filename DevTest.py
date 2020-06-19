import aiohttp
import cfscrape
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        scraper = cfscrape.create_scraper(sess=session)
        print(await scraper.get("https://www.43einhalb.com/en/sneaker"))
    return

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
