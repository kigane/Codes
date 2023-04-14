import time
import threading


def count_down(n: int) -> None:
    while n > 0:
        print(f"Count Down: {n}")
        time.sleep(1)
        n -= 1


class CountTask(object):

    def __init__(self) -> None:
        self._running = True

    def terminate(self) -> None:
        self._running = False

    def run(self, n: int) -> None:
        while n > 0 and self._running:
            print(f"Count Down: {n}")
            time.sleep(1)
            n -= 1


if __name__ == '__main__':
    # t = threading.Thread(target=count_down, args=[3], daemon=True)
    task = CountTask()
    t = threading.Thread(target=task.run, args=[3], daemon=True)
    t.start()
    # t.join()
    time.sleep(1)
    task.terminate()
    time.sleep(1)  # terminate需要等当前循环结束才会生效. sleep(1)
    if t.is_alive():
        print('Still running')
    else:
        print('Completed')
    # t.join()
