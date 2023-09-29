

# 배

# 최대값 순으로 정렬
# 최대값 순으로 내보내기
# 전체 내보낸 횟수 만큼 카운트
# 더 이상 내보낼 수 없으면 종료

import sys; input = sys.stdin.readline
from collections import deque
def solve():
    n = int(input())
    n_list = sorted(list(map(int,input().split())),reverse=True)
    m = int(input())
    m_list = sorted(list(map(int,input().split())))
    result,i = 0,0
    
    if n_list[-1] < m_list[0]: return -1

    while m_list:
        check_list = deque([])
        while m_list and len(check_list)<n:
            check_list.appendleft(m_list.pop())
        for i in range(len(n_list)):
            if len(check_list)==0: break
            data = check_list.pop()
            if data > n_list[i]: # 더 큰 경우는 나가지 못함
                check_list.appendleft(data)
        result+=1
        m_list = m_list + list(check_list)
    return result

print(solve())

