

# 무인도에 갇힌 사람들을
# 구명 보트는 한 번에 최대 2명
# 무게 제한 있음
# 구명보트를 최대한 적게 사용해서 모든 사람을 구출

# 2명씩 나갈 수 있으므로, 가장 무거운 사람, 가벼운 사람 조합으로 내보내기

def solution(people, limit):
    people.sort()
    answer = 0
    start,end  = 0,len(people)-1
    while start<=end:
        if people[start]+people[end] <=limit:
            start+=1
        end-=1
        answer+=1
    return answer


people = [70, 50, 80, 50]
# people = [70,80,50]
print(solution(people,100))