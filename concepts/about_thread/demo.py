import threading
import time
from datetime import datetime
from icecream import ic
ic.configureOutput(prefix=lambda: datetime.now().strftime(
    '%H:%M:%S | '), includeContext=False)


def foo():
    print('start')
    time.sleep(1)
    ic("done")


if __name__ == '__main__':
    ic(threading.active_count())
    x = threading.Thread(target=foo)
    x.start()
    ic(threading.active_count())
