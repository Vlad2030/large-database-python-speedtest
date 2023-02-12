import asyncio
import testing.database
import testing.speedtest
import testing.logger


async def main() -> None:
    @testing.speedtest.performance_time
    testing.database.async_make()
    return None


if __name__ == "__main__":
    asyncio.run(main())