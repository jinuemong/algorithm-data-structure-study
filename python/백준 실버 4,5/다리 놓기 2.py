

# 다리 놓기 규칙 적용
import sys
input = sys.stdin.readline
T =  int(input().strip())

for _ in range(T):
    n,m = list(map(int,input().split()))
    n_data, m_data = 1,1
    for i in range(0,n):
        n_data*=(m-i)
        m_data*=(n-i)
    print(n_data//m_data)