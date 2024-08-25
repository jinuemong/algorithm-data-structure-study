
from collections import Counter
def solution(k, tangerine):
    answer = 0
    for value in sorted(Counter(tangerine).values(),reverse=True):
        if k>0:
            answer+=1
            k-=value
    return answer

print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))