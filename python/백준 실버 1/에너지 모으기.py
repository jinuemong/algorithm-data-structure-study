# n = int(input())
# w = list(map(int, input().split()))
#
# result = 0
# while n > 2:
#     max_result = 0
#     max_idx = 0
#     for i in range(1, n - 1):
#         current = w[i - 1] * w[i + 1]
#         if current > max_result:
#             max_idx = i
#             max_result = current
#     w = w[:max_idx] + w[max_idx+1:]
#     print(w)
#     result+=max_result
#     n = len(w)
# print(result)

## 모든 경우의 수를 구한 후 최대값 구하기

def back_tacking(x):
    global answer

    if len(w) == 2:
        answer = max(answer, x)
        return

    for i in range(1, len(w) - 1):
        target = w[i - 1] * w[i + 1]
        v = w.pop(i)
        back_tacking(x + target)
        w.insert(i, v)


n = int(input())
w = list(map(int, input().split()))
answer = 0
back_tacking(0)
print(answer)