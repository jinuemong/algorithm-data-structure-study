# 풀이 방식
# 뒤집에서 풀기
h, w = map(int, input().split())
n_list = list(map(int, input().split()))
max_n = max(n_list)
graph = [([1] * (n_list[i]) + [0] * (max_n - n_list[i])) for i in range(len(n_list))]
result = 0
for i in range(len(graph[0])):
    count = 0
    prev = False
    for j in range(len(graph)):
        value = graph[j][i]
        if value == 1 and prev:
            result += count
            count = 0
        elif value == 1 and not prev:
            prev = True
        elif prev:
            count +=1
print(result)

