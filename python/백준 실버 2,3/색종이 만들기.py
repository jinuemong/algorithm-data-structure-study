
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = {0: 0, 1: 0}

def find(x,y, n):
    count = 0
    for i in range(x,x+n):
        for j in range(y,y+n):
            if graph[j][i] == 1:
                count +=1
    if count == n * n:
        result[1] += 1
    elif count == 0:
        result[0] += 1
    else:
        find(x, y, n//2)
        find(x, y+n//2, n//2)
        find(x+n//2, y, n//2)
        find(x+n//2, y+n//2, n//2)
find(0,0,n)
print(result[0])
print(result[1])
