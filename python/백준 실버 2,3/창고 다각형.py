# 창고 다각형
# prev보다 커야함 (마지막 인덱스가 아닌 경우 )
# 다음 블럭을 만난 경우 prev * 블럭 수
# 무조건 이전보다 큰 경우는 1칸 점유
# 마지막인 경우만 분기 (큰 경우 -> prev * 블럭) , 작은 경우 -> last*블럭
n = int(input())
l, h = map(int, input().split())
result = h
stack = [(l + 1, h)]
for i in range(n - 2):
    l, h = map(int, input().split())
    if h > stack[-1][1]:
        result += (l - stack[-1][0]) * stack[-1][1] + h
        stack.append((l + 1, h))
l, h = map(int, input().split())  # last
if stack[-1][1] >= h:
    result += (1 + l - stack[-1][0]) * h
else:
    result += (l - stack[-1][0]) * stack[-1][1] + h
print(result)
