# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/8/8 2:59 PM

def gcd(a,b):#a>=b
    if a%b == 0: return b
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return a*b/gcd(a,b)

res = lcm(2,4)
print(res)
