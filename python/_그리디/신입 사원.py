
# a vs b
# 서류 and 면접 비교
# 3 2
# 1 4
# 4 1
# 2 3
# 5 5
#  둘 모두가 어느 한명보다 떨어지는 경우 -> 탈락
# 1 4
# 2 3
# 3 2
# 4 1
# 5 5
# 2번째 인덱스부터 가장 작은 값을 넣음
# 그 값보다 작은 경우 탈락

for _ in range(int(input())):
    n = int(input())
    fail = 0
    graph = []
    for i in range(n):
        graph.append(list(map(int,input().split())))
    graph.sort()
    minimum = graph[0][1]
    for i in range(1,n):
        if graph[i][1] > minimum:
            fail+=1
        minimum = min(minimum,graph[i][1])
    print(n-fail)

