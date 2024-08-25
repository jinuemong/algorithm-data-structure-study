

# 더 맵게
# 힙 큐 활용

from heapq import  heappop,heappush , heapify
def solution(scoville, K):
    heapify(scoville)
    answer = 0
    while scoville[0]<K:
        heappush(scoville,heappop(scoville) + heappop(scoville)*2)
        answer+=1
        if len(scoville)<2 and scoville[0] < K:
            return -1
    else:
        return answer


scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville,k))