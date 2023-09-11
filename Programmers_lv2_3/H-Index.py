

#


def solution(citations):
    citations = sorted(citations,reverse= True)
    for index, citation in enumerate(citations):
        if index>=citation:
            return index
    return len(citations)

print(solution([3,0,6,1,5]))