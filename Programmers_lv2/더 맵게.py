

# 더 맵게
# 힙 큐 활용

from heapq import  heappop,heappush , heapify
def solution(scoville, K):
    heapify(scoville)
    answer = 0
    while len(scoville)>1 and scoville[0]<K:
        one ,two= heappop(scoville) , heappop(scoville)
        print(one,two)
        heappush(scoville,one+two*2)
        answer+=1
    if answer==0  and scoville[0]<K:
        return -1
    else:
        return answer


scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville,k))