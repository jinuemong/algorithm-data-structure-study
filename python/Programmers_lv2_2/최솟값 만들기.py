
# 최솟값 만들기
# 최소 합을 구해야 하므로
# a그룹에서 최소 * b그룹에서 최대를 해야 최소 값 성립
# heapque 활용
def solution(A,B):
    from _heapq import heappop,heapify
    B = [(-b, b) for b in B]
    heapify(A) ,heapify(B)
    return sum([heappop(A)*heappop(B)[1] for _ in range(len(A))])

a = [1,2]
b = [3,4]
print(solution(a,b))