import sys
import copy

n = int(sys.stdin.readline().rstrip())
set1 = list(sys.stdin.readline().rstrip())
answer = 0
for i in range(n-1):
    set2 = list(sys.stdin.readline().rstrip())
    c_set1 = copy.deepcopy(set1)
    c_set2 = copy.deepcopy(set2)
    for j in set1:
        if j in set2:
            set2.remove(j)
            c_set1.remove(j)
    if len(set2) <= 1 and len(c_set1) <= 1:
        answer += 1

print(answer)