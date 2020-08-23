# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/18 11:24 PM


from threading import Lock


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_lock = Lock()
        self.even_lock = Lock()
        self.odd_lock = Lock()
        self.even_lock.acquire()
        self.odd_lock.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.zero_lock.acquire()
            printNumber(0)
            if i & 1:
                self.odd_lock.release()
            else:
                self.even_lock.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            if i & 1 == 0:
                self.even_lock.acquire()
                printNumber(i)
                self.zero_lock.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            if i & 1:
                self.odd_lock.acquire()
                printNumber(i)
                self.zero_lock.release()