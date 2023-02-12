from loguru import logger as log


async def info(data: str) -> None:
    return log.INFO(data)