
# k글자를 가르침
# k개의 단어만 읽기 가능
# 중복 없음
# anta~ tica
# 시간 초과
import sys
from itertools import combinations
input = sys.stdin.readline
max_len = 0
first = set(['a','c','t','n','i'])
n,k = list(map(int,input().split()))
teach_word_count = k - len(first)
if teach_word_count <0: teach_word_count = 0

arr = []
for _ in range(n):
    data = set(list(input().strip())) - first
    if len(data) <= teach_word_count:
        arr.append(data)
print(arr)

for i in range(len(arr),1,-1):
    for comb in list(combinations(arr,i)):
        words = set()
        for i in comb:
            words = words | i
        if len(words) <= teach_word_count:
            max_len = max(max_len,len(comb))
            break
print(max_len)
