import time
import threading


def count_down(n: int, start_evt: threading.Event) -> None:
    print("Count Down Start")
    start_evt.set()  # 将evt的内部变量设为true

    while n > 0:
        print(f"Count Down: {n}")
        time.sleep(1)
        n -= 1


if __name__ == '__main__':
    # event 对象最好单次使用，就是说，你创建一个 event 对象，
    # 让某个线程等待这个对象，一旦这个对象被设置为真，你就应该丢弃它。
    evt = threading.Event()
    t = threading.Thread(target=count_down, args=[3, evt])
    t.start()
    evt.wait()  # 阻塞当前线程，直到evt的内部变量被设为true
    print("Count Down Started")
