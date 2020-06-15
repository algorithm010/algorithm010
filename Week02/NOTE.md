学习笔记

#### 有效的异位词
1.直接对两个字符串进行排序，判断排序后的结果是否一致
```
return sorted(s) == sorted(t)
```
2.根据两个字符串构建hash表，判断两个hash表是否一致
```angular2html
dic1, dic2 = {}, {}
for item in s:
    dic1[item] = dic1.get(item, 0) + 1
for item in t:
    dic2[item] = dic2.get(item, 0) + 1
return dic1 == dic2

```
3.只需要使用一个hash表，前一次遍历增加值，后一次遍历减少值
最后判断hash表中的值是否为0
```angular2html
if len(s) != len(t): return False
hashmap = {}
for substr in s:
    if not hashmap.get(substr):
        hashmap[substr] = 1
    else:
        hashmap[substr] += 1
for substr in t:
    if hashmap.get(substr):
        hashmap[substr] -= 1
    else:
        return False
for value in hashmap.values():
    if value != 0:
        return False
return True

```
4.使用python内置的count函数，统计字符出现的个数 原理与方法2一致

```angular2html
if len(s) != len(t):
    return False
for i in set(s):
    if s.count(i) != t.count(i):
        return False
return True
```
优化
```angular2html

if len(s)!=len(t):return False
tmp = set(s)
if tmp == set(t):#如果两个字符串的set相同进行深入判断
    for i in tmp:
        if s.count(i) != t.count(i): return False
    return True
return False
```