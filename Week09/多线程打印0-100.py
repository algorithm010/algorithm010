import threading
import time


# 第一个线程，打印奇数
def threada(n):
    for i in range(1, n + 1):
        if i & 1:
            lockb.acquire()#先请求b锁，保证不会打印偶数
            print(i)
            locka.release()

# 第二个线程，打印偶数
def threadb(n):
    for i in range(2, n + 1):
        if i & 1 == 0:
            locka.acquire()#先请求a锁，使得打印偶数过程不会打印奇数
            print(i),
            lockb.release()

if __name__ == "__main__":
    locka = threading.Lock()
    lockb = threading.Lock()

    ta = threading.Thread(target=threada,args=(100,))
    tb = threading.Thread(target=threadb,args=(100,))

    locka.acquire()  # 保证a先执行

    ta.start()
    tb.start()
