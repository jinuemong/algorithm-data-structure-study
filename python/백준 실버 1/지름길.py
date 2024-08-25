

## 지름길

n,d = list(map(int,input().split()))
data = {}
for _ in range(n):
    start, end, cm = list(map(int,input().split()))
    if start in data:
        if cm < data[start][1]:
            data[start] = [end,cm]
    else:
        data[start] = [end,cm]
result, current = 0, 0
for start,value in data.items():
    result += (start - current)

# while data:
#     if current in data:
#         value = data.pop(current)
#         if value[0] in data:
#             result += value[1]
#             current = value[0]
#     else:
#         break
#
# print(result,current)
# print(d-current + result)
