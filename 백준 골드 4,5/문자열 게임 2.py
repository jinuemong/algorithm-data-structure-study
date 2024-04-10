import string

t = int(input())
for _ in range(t):
    w = list(input())
    k = int(input())
    result = {s: [] for s in string.ascii_lowercase}
    for idx,word in enumerate(w):
        result[word].append(idx)
    min_result, max_result = 10001,-1
    for idx_list in result.values():
        if len(idx_list) >= k:
            for i in range(0,len(idx_list)-k+1):
                max_result = max(max_result,idx_list[i+k-1]-idx_list[i]+1)
                min_result = min(min_result,idx_list[i+k-1]-idx_list[i]+1)

    if min_result == 10001 and max_result == -1:
        print(-1)
    else:
        print(min_result,max_result)
    # k개 포함하면서 가장 짧은 연속 문자열을 구한다 (1번)
    # k개를 포함하면서 첫번째 - 마지막이 같은 가장 긴 연속 문자열을 구한다

# 찾을 수 없다면 -1 출력
