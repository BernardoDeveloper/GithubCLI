import httpx

async def get_async(url):
    async with httpx.AsyncClient() as client:
        return await client.get(url)