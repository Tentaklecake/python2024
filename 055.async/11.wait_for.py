import asyncio
from time import perf_counter


async def fast() -> None:
    print("fast старт")
    await asyncio.sleep(2)
    print("fast стоп")


async def middle() -> None:
    print("middle старт")
    await asyncio.sleep(4)
    print("middle стоп")


async def slow() -> None:
    print("slow старт")
    await asyncio.sleep(6)
    print("slow стоп")


async def main() -> None:
    # try:
    #     await asyncio.wait_for(fut=middle(), timeout=3)
    # except TimeoutError:
    #     print("таймаут")

    await asyncio.gather(
        *(
            asyncio.wait_for(fut=fast(), timeout=3),
            asyncio.wait_for(fut=middle(), timeout=3),
            asyncio.wait_for(fut=slow(), timeout=3),
        ),
        return_exceptions=True,
    )


if __name__ == "__main__":
    t0 = perf_counter()
    asyncio.run(main())
    print("асинхронный код закончен")
    print(f"{perf_counter() - t0:.4f} сек")
