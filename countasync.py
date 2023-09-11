import asyncio


async def count(count_from: int) -> None:
    print(count_from)
    await asyncio.sleep(1)
    count_from += 1
    print(count_from)


async def main():
    await asyncio.gather(count(1), count(3), count(5))

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
