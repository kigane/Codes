import asyncio
from datetime import datetime
from icecream import ic
ic.configureOutput(prefix=lambda: datetime.now().strftime('%H:%M:%S | '),
                   includeContext=False)


# async 作用：将main函数包装,执行main会返回一个Coroutine对象。
async def main():
    ic("hwk")
    # await foo("hello") # 一直等到foo执行完
    task = asyncio.create_task(foo("hello"))  # 创建任务，不阻塞当前程序执行流
    await task  # 等待任务执行完才继续
    ic("finish")
    return 42


async def foo(text):
    ic(text)
    # asyncio.sleep(1)也是返回Coroutine对象
    # await只能在async函数内使用
    await asyncio.sleep(1)

if __name__ == '__main__':
    result = asyncio.run(main())
    ic(f'Answer: {result}')
