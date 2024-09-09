
import sys; input = sys.stdin.readline

n = int(input())
building = [0]
answer = 0

for _ in range(n):
    x, h = map(int,input().split())
    if h > building[-1]:
        answer+=1
        building.append(h)
    else:
        while building[-1] > h :
            building.pop()

        if building[-1] < h:
            answer+=1
            building.append(h)
print(answer)