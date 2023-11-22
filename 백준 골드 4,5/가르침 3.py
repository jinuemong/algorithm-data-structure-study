
import sys
from itertools import combinations
from collections import Counter

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
sub_list = []
for comb in list(combinations(arr,teach_word_count)):
    words = set()
    for i in comb:
        words = words | i
    sub_list.append("".join(list(words)))
    if len(words) <= teach_word_count:
        max_len = max(max_len,len(comb))
counter = Counter(sub_list).values()
if len(counter)>0:
    print(max(max_len,max(counter)))
else:
    print(max(max_len))