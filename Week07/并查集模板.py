# -*- coding:utf-8 -*-
# Author : Ray
# Data : 2020/7/20 11:12 PM



SIZE = 7
parent =[-1] * SIZE
rank = [0] * SIZE
# 并查集就是实现了两个方法 一个find一个union
def find(x, parent):
    node = x
    while parent[node] != -1:
        node = parent[node]
    return node

def union(x, y):
    x_root = find(x, parent)
    y_root = find(y, parent)
    if x_root == y_root:
        return
    # parent[y_root] = x_root
    if rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    elif rank[y_root] > rank[x_root]:
        parent[x_root] = y_root
    else:
        parent[x_root] = y_root
        rank[y_root] += 1