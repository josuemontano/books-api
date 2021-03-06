import os

import aioredis

redis_url = os.getenv("REDIS_URL", None)
if redis_url is None:
    raise RuntimeError("REDIS_URL environment variable is not set")

redis = aioredis.from_url(redis_url)
