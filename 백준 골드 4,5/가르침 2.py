
import sys
from itertools import combinations

input = sys.stdin.readline
first = {'a', 'c', 't', 'n', 'i'}
max_len = 0
n,k = list(map(int,input().split()))
teach_word_count = k - len(first)
if teach_word_count <0: teach_word_count = 0

arr = []
uniqueSet = set()
for _ in range(n):
    data = set(list(input().strip())) - first
    if len(data) <= teach_word_count:
        arr.append(data)
        uniqueSet = uniqueSet | data

if k < 5:
    print(0)
else:
    if len(arr) == 0:
        print(max_len)
    if len(uniqueSet) <= teach_word_count:
        print(max)
for comb in list(combinations(arr,teach_word_count)):
    words = set()
    for i in comb:
        words = words | i
    if len(words) <= teach_word_count:
        max_len = max(max_len,len(comb))


