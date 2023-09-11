

# 조건 1 두 인덱스의 원소와 그 사이 원소를 모두 포함하는 부분 수열이어야 함
# 조건 2 부분 수열의 합은 7이다
# 합이 k인 부분 수열이 여러 개인 경우 길이가 짧은 수열 탐색
# 길이가 짧은 수열이 여러 개인 경우 인덱스가 적은 수열을 찾음

# 해결 : i, j를 두고 j를 계속 증가(sum+seq[j]) -> sum > k
# -> i를 계속 증가 (sum-seq[i])-> sum < k
# -> 이 과정 반복 + sum == k인 순간은 answer에 저장
# answer를 조건으로 정렬 후 맨 처음 출력
def solution(sequence, k):
    answer = []
    sum , start, end = 0,0,-1
    while True:
        if sum < k:
            end+=1
            if end >= len(sequence): break
            sum+=sequence[end]
        else:
            sum -= sequence[start]
            if start >= len(sequence): break
            start+=1
        if sum == k:
            answer.append([start,end])
    answer.sort(key= lambda x : (x[1]-x[0],x[0]))
    return answer[0]


print(solution([1, 2, 3, 4, 5],7))