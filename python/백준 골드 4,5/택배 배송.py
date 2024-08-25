## 다시풀기

n, m = map(int, input().split())
graph_list = {i: [] for i in range(1, n + 1)}
weight = {i: [] for i in range(1, n + 1)}
for i in range(m):
    x, y, w = map(int, input().split())
    x, y = min(x, y), max(x, y)
    graph_list[x].append(y)
    weight[x].append(w)
result = []

def find(count, current):
    if current == n:
        result.append(count)
    else:
        current_list = graph_list[current]
        for idx,value in enumerate(current_list):
            find(count+weight[current][idx],value)
find(0,1)
print(min(result))