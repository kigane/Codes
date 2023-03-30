import asyncio
from datetime import datetime
from icecream import ic
ic.configureOutput(prefix=lambda: datetime.now().strftime('%H:%M:%S | '),
                   includeContext=False)


async def fetch_data():
    ic("start fetch")
    await asyncio.sleep(2)
    ic("finish fetch")
    return {"data": 1}


async def print_nums():
    for i in range(10):
        ic(i)
        await asyncio.sleep(0.3)


async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_nums())

    ret = await task1
    ic(ret)

    await task2  # 如果不await task2，则print_nums不会执行完。因为在其执行完之前，主函数已经结束了。

if __name__ == '__main__':
    asyncio.run(main())
