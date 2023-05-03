

# 데이터의 수가 최대 500만개
# O(NlogN)의 정렬 알고리즘 사용

n, k = map(int,input().split())
n_list = list(map(int,input().split()))

print(sorted(n_list)[k-1])