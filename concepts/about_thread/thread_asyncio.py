import threading
import asyncio
import time


def worker():
    print("worker start")
    time.sleep(1)
    # loop = asyncio.get_event_loop()
    # print(loop)
    print("worker done")


async def foo():
    await asyncio.sleep(1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print(loop)

    x = threading.Thread(target=worker)
    x.start()
    x.join()
