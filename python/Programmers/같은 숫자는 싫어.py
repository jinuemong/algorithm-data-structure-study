
def solution(arr):
    answer = []
    current = ""
    for a in arr:
        if a != current:
            current = a
            answer.append(current)

    return answer

print(solution([4,4,4,3,3]))