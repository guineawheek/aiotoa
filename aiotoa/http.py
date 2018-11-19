from asyncio import sleep
from datetime import datetime
import aiohttp
from async_timeout import timeout as atimeout

from .models import *


class AioTOAError(Exception):
    pass


class TOASession:
    def __init__(self, key: str, app_name: str, aiohttp_session=None, ratelimit=2, close_on_aexit=True):
        self.key = key
        self.app_name = app_name
        self.ratelimit = ratelimit
        self.last_req = datetime.today()
        self.session = aiohttp.ClientSession() if not aiohttp_session else aiohttp_session
        self.close_on_aexit = close_on_aexit

    async def __aenter__(self):
        pass

    async def __aexit__(self, exc_type, exc, tb):
        if self.close_on_aexit:
            await self.session.close()

    async def close(self):
        await self.session.close()

    async def req(self, endpoint: str, model):
        if self.ratelimit:
            now = datetime.now()
            delta = (now - self.last_req).total_seconds()
            if delta < self.ratelimit:
                await sleep(self.ratelimit - delta)
            self.last_req = now

        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint

        headers = {
            "X-Application-Origin": self.app_name,
            "X-TOA-Key": self.key,
            "Content-Type": "application/json"
        }
        
        async with atimeout(5) as _, self.session.get("https://www.thebluealliance.com/api/v3" + endpoint, headers=headers) as response:
            data = await response.json()
            # toa never returns data in dicts, it's always lists
            if isinstance(data, dict):
                raise AioTOAError(f"Request to {endpoint} failed with {response.status} {response.reason} (data={data})")
            return to_model(data, model)

