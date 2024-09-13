# 1선택 -> 1
# 2선택 -> 12 ( 경우의 수 +2)

# 2 미선택 -> 1
# 3선택 -> 123 x
# 3 미선택 -> 12  (경우의 수 +0)

# # 4 선택 ->
# 1 45
# 12
# 12 4
# 12 5
# 12 45
# 1 34

# 2 45
# 23
# 23 5

# 34

# 45

# 1부터 N까지
# 연속 수를 카운트한다.
# 다응 인덱스로 이동 시 선택할 지 말지 정한다
# 선택 여부는 연속 수를 넘었는지, 필수 과목인지 체크
# 1부터 탐색을 진행하면서 ->
# count = 연속수 -1인 경우 다음 수가 필수 과목이라면, 현재 과목을 선택하지 말아야 한다
# 즉 반드시 x를 선택하므로 continue로 넘어가자!
# 반면에 현재 과목이 필수 과목이라면 반드시 선택한다 count +1 후 다음으로 넘어간다 (result는 그대로)
# 연속 수를 넘었다면 선택하지 않고, 필수 과목이라면 반드시 선택한다.
# 계속해서 이어나갈 수 있따면 count+1한다
# k는 반드시 n보다 작거나 같으므로 만족못하고 끝나는 경우는 없음
# ex k == 1, n == 1 -> 1
# 경우의 수는 선택 하냐 안하냐
# 123인 경우
# 1 선택 - 2선택 or 2 미선택  - 3선택 or 3 미선택 4
# 1 미선택 - 2섵낵 or 2 미선택 - 3선택 or 3 미선택 4
# = 8가지 2**3
#
MOD = 10 ** 9 + 7

n, k = map(int, input().split())
an = [0] + list(map(int, input().split()))
result = 0


def find(stack, next, flag):
    global result
    if next == n+1:
        if flag:
            result = (result + 1) % MOD
        return
    current_flag = flag
    if len(stack) == k:
        current_flag = True
        find([next], next + 1, current_flag)
        if not an[next]:
            find([], next + 1, current_flag)
    else:
        find(stack + [next], next +1 ,current_flag)
        if not an[next]:
            find(stack, next + 1, current_flag)

find([],1,False)
if result%2 == 0:
    print(result//2)
else:
    print(result//2+1)

