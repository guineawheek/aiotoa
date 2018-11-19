# aiotoa
`aiotba` except for The Orange Alliance, the FTC attempt at something similar to TBA.

The season-specific data structures were actually implemented this time because there's only three of them.

# example
```python
import asyncio
from aiotoa import TOASession

async def main():
    ses = TOASession("toa api key here", "toa app name here")
    lanbros = await ses.team(9971)
    print(lanbros.team_name)

asyncio.run(main())
```
this lib follows closely to the endpoints of [APIv3](https://orange-alliance.github.io/TOA-API/) and should cover
all of them (that are functioning...)

# installation
`pip install aiotoa`

# notes
all of this is on a provisional basis and large parts of the api could change at a moment's notice. this isn't "stable" 
yet so to speak.
