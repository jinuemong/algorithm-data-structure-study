def find_length(arr, current, way):
    count = 0
    while 0 <= current[0] < len(arr) and 0 <= current[1] < len(arr) \
            and arr[current[0]][current[1]] != "_":
        current[0] += way[0]
        current[1] += way[1]
        count += 1
    return count


n = int(input())
arr = []
result = []
for _ in range(n):
    arr.append(list(input()))
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[j][i] == "*":
            result = [i+1, j]
            break
    if len(result)>0: break

result.append(find_length(arr, result[0:2], (0, -1)))
result.append(find_length(arr, result[0:2], (0, 1)))
result.append(find_length(arr, result[0:2], (1, 0)))

result.append(find_length(arr, [result[2] + 1, result[1] - 1], (1, 0)))
result.append(find_length(arr, [result[2] + 1, result[1] - 1], (1, 0)))

for i in range(len(result)):
    if i == 2: print()
    print(result[i], end=" ")
