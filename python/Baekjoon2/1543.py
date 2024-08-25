

# 문서 탐색
# 내장 함수 사용
document = input()

print(document.count(input()))


# 알고리즘 구성
# 문서 길이가 2500, 단어 길이 50
# 모든 경우의 수를 계산하여 문제를 해결할 수 있음
# 시간복잡도 O(NM)

document2 = input()
word =input()

index = 0
result = 0
while len(document2) - index >= len(word):
    #남은 인덱스가 단어 길이보다 커야함
    if document2[index:index+len(word)] == word:
        # 0번째 부터 단어 길이만큼 탐색 시작
        result += 1
        index += len(word) #단어 발견 시 단어 길이만큼 이동
    else:
        index += 1 # 단어를 못찾으면 한 칸 이동
print(result)