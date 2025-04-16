from litestar.stores.memory import MemoryStore


store = MemoryStore()


async def main() -> None:
    value = await store.get("key")
    print(value)

    await store.set("key", "value")
    value = await store.get("key")
    print(value)

    await store.delete("key")
    value = await store.get("key")
    print(value)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
