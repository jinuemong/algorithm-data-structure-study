# 타고 삭제 하는 방식

import sys

input = sys.stdin.readline


def dfs(node, node_dic):
    if node not in node_dic:
        return
    next = node_dic[node]
    node_dic.pop(node)
    for n in next:
        dfs(n, node_dic)


node_dic = {i: [] for i in range(0, int(input()))}
for idx, node in enumerate(list(map(int, input().split()))):
    if node != -1:
        node_dic[node].append(idx)

dfs(int(input()), node_dic)
print(len([value for value in node_dic.values() if len(value) == 0]))
