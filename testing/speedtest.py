from time import perf_counter
from colorama import Fore, Style


class Performance:
    async def __init__(self, func) -> None:
        self.func = func

    @staticmethod
    async def performance_time(func: function) -> None:
        async def run() -> None:
            start: float = perf_counter()
            func()
            end: float = perf_counter() - start
            return print(
                value=f"Execution speed:\t{Fore.RED(end)}"
                      f"{Style.RESET_ALL}",
                end="\n",
            )

        return run
