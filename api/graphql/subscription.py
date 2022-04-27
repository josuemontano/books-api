import asyncio
from typing import AsyncGenerator, Optional

import strawberry

from ..helpers.redis import redis


@strawberry.type
class Subscription:
    """Subscriptions are long-lasting GraphQL read operations that can update their result whenever a particular
    server-side event occurs.
    """

    @strawberry.subscription
    async def pi(self, precision: Optional[int] = 10) -> AsyncGenerator[float, None]:
        """This method publishes values of the Leibniz's series to calculate PI.

        It uses Redis' pubsub. Any value published to the "series:leibniz_pi" channel will be trasmitted to the
        client.
        ```
        redis.publish("series:leibniz_pi", 4 - 4/3 + 4/5 - 4/7 + 4/9)
        ```
        """
        pubsub = redis.pubsub()
        await pubsub.subscribe("series:leibniz_pi")

        while True:
            try:
                message = await pubsub.get_message(ignore_subscribe_messages=True)
                if message is not None:
                    yield round(float(message["data"]), precision)
                await asyncio.sleep(0.1)
            except asyncio.TimeoutError:
                pass
