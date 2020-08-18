# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/18 11:08 PM

from threading import Lock
class Foo:
    def __init__(self):
        self.firstJob = Lock()
        self.secondJob = Lock()
        self.firstJob.acquire()
        self.secondJob.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstJob.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.firstJob:#请求锁
        # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.secondJob.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.secondJob:
        # printThird() outputs "third". Do not change or remove this line.
            printThird()