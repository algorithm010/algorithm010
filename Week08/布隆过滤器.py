# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/27 11:11 PM

from bitarray import bitarray
import mmh3
class BooleanFilter:
    def __init__(self,size,hash_num):
        self.size = size
        self.hash_num = hash_num
        self.bit_array = bitarray
        self.bit_array.setall(0)
    def get(self,x):
        for seed in range(self.hash_num):
            result = mmh3.hash(x,seed)%self.size#用k位二进制表示是否存在
            self.bit_array[result] = 1
    def lookup(self,x):
        for seed in range(self.hash_num):
            result = mmh3.hash(x,seed)%self.size
            if self.bit_array[result] != 1:
                return 'not in'
        return 'probably in'