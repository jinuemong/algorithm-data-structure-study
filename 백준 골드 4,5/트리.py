

import sys
input = sys.stdin.readline
count = 0

def dfs(node, node_dic,visited):
    global count
    visited.add(node)
    if node not in node_dic:
        return
    next = node_dic[node]
    if len(next)==0:
        count+=1
    else:
        for n in next:
            if n not in visited:
                dfs(n,node_dic,visited)

n = int(input())
node_dic = {i : [] for i in range(0,n)}
for idx, node in enumerate(list(map(int,input().split()))):
    if node!= -1:
        node_dic[node].append(idx)

print(node_dic)
node_dic.pop(int(input()))
print(node_dic)
dfs(0,node_dic,set())
print(count)

