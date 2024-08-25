

def solution(sequence, k):
    answer = [0,len(sequence)]
    for i in range(len(sequence)):
        start,total = i,0
        if sequence[i]>k: break
        for j in range(i,len(sequence)):
            total+=sequence[j]
            if total==k:
                if answer[1]-answer[0] > j - start:
                    answer = [start,j]
            if total>k:
                break

    return answer


print(solution([1, 2, 3, 4, 5],7))