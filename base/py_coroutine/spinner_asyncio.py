import asyncio
import itertools
import time
import sys


async def spin(msg: str):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + '' + msg
        write(status)
        flush()
        write('\x08' * len(status))  # \x08是退格键
        await asyncio.sleep(0.1)
    write(' ' * len(status) + '\x08' * len(status))


async def slow_function():
    await asyncio.sleep(3)
    return 42


async def supervisor():
    spinner = asyncio.create_task(spin('thinking!'))
    print('spinner task:', spinner)
    result = await slow_function()
    spinner.cancel()
    return result


def main():
    result = asyncio.run(supervisor())
    print('Answer:', result)


if __name__ == '__main__':
    from pprint import pprint
    pprint(globals())
    main()
