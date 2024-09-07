n = int(input())
an = list(map(int, input().split()))
bn = list(map(int, input().split()))
prev = sum([an[i] * bn[i] for i in range(n)])
result = float("-inf")

current = 0

for j in range(n):
    if bn[j]:
        current -= an[j]
    else:
        current += an[j]
    if current > result:
        result = current
    if current < 0:
        current = 0
    print(result, current)
print(result+prev)
