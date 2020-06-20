import aiohttp
import aiocfscrape
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        scraper = aiocfscrape.create_scraper(sess=session)
        res = await scraper.request("GET", "https://www.slamjam.com/en_US/man/footwear/sneakers/low/common-project/original-achilles-low-sneakers/J169893.html")
        print(await res.text())
        await session.close()

asyncio.run(main())
