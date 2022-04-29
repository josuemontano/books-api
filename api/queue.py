import time

from dotenv import load_dotenv

# Add code that uses environment variables AFTER THE NEXT LINE
load_dotenv()

from huey import RedisHuey, crontab
from redis import Redis

from .helpers.redis import redis_url

huey = RedisHuey("app-queue", url=redis_url)
redis = Redis.from_url(redis_url)


@huey.periodic_task(crontab(minute="*/5"))
def calculate_pi():
    """Calculate the value of pi using Leibniz's series. On each iteration, the value is
    published to the "series:leibniz_pi" channel.
    """
    iterations = 5000
    pi = 4

    for i in range(1, iterations):
        x = i * 2 + 1
        op = 1 if i % 2 == 0 else -1
        pi = pi + op * 4 / x

        redis.publish("series:leibniz_pi", pi)
        time.sleep(0.1)

    return pi
