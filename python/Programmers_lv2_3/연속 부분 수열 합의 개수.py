

def solution(elements):
    answer = set()
    for i in range(1,len(elements)):
        for j in range(0,len(elements)-i+1):
            print(i,j,elements[j:j+i])
            answer.add(sum(elements[j:j+i]))
    answer.add(sum(elements))
    return len(answer)

print(solution([7,9,1,1,4]))