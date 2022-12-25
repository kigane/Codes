
import time

start = time.time()  # start time

time.sleep(5)

end = time.time() # 系统绝对时间
# time.process_time() # 当前进程时间
# time.thread_time() # 当前线程时间
m, s = divmod(end-start, 60)
h, m = divmod(m, 60)
print("Elapsed time is  {} min {} s".format(m, s))
