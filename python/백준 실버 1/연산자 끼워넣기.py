# 연산자 우선순위를 무시하고 앞에서부터 진행
# 나눗셈은 정수의 몫만 취함
# 음수를 양수로 나누는 경우 양수로 바꾼 후 몫을 음수로 바꿈
# n = int(input())
# an = list(map(int,input().split()))
# plus,minus,multi,dev = map(int,input().split())
# op = ["+"]*plus + ["-"]*minus+["*"]*multi + ["%"]*dev
# min_result = 1_000_000_000
# max_result = -1_000_000_000
# pick_nums = []
# def combination(cnt,next,stack):
#     global min_result,max_result
#     if cnt == n-1:
#         sum = an[0]
#         for i in range(1,n):
#             operation = stack[i-1]
#             if operation == "+":
#                 sum += an[i]
#             elif operation == "-":
#                 sum -= an[i]
#             elif operation == "*":
#                 sum *= an[i]
#             else:
#                 sum = dev(sum,an[i])
#         min_result = min(min_result,sum)
#         max_result = max(max_result,sum)
#         return
#     for a in next:
#         stack.append(a)
#         combination(cnt+1,set(next)-set(a),stack)
#
# def dev(value,divider):
#     return +(abs(value)//divider)
#
# combination(0,op,[])
# print(max_result,min_result)

n = int(input())
an = list(map(int, input().split()))
plus, minus, multi, dev = map(int, input().split())
minimum = 1_000_000_000
maximum = -1_000_000_000


def dfs(cnt, total, plus, minus, multi, dev):
    global maximum, minimum
    if cnt == n:
        maximum = max(maximum, total)
        minimum = min(minimum, total)
        return

    if plus:
        dfs(cnt + 1, total + an[cnt], plus - 1, minus, multi, dev)
    if minus:
        dfs(cnt + 1, total - an[cnt], plus, minus - 1, multi, dev)
    if multi:
        dfs(cnt + 1, total * an[cnt], plus, minus, multi - 1, dev)
    if dev:
        dfs(cnt + 1, int(total / an[cnt]), plus, minus, multi, dev - 1)


dfs(1, an[0], plus, minus, multi, dev)
print(maximum)
print(minimum)
