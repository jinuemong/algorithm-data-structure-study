

# 롤케이크 자르기
# 공평한 롤케이크
# 1,2,3,4 : 토핑의 종류
# 토핑이 있는 케이크를 자를 때 좌, 우 토핑의 종류가 같아야 함
# 공평하게 자르는 경우의 수 리턴
# 공평하게 자를 수 없을 경우 0 리턴
# 두 조각으로 나눠야 하므로 정확하게 반으로 나눠야 함
# 문제풀이
# 이진탐색
# hit -> 좌 우 모두 탐색
# miss -> 더 큰 쪽으로 이동
# hit : 좌 우 수가 같음 -> 좌와 우로 나누어서 탐색
# 둘중 하나라도 0이 나온다면 탐색 x

answer = 0
def solution(topping):
    global answer
    search(topping,len(topping)//2)
    return answer

def search(data,mid):
    global answer
    topping_1,topping_2 = data[:mid],data[mid:]
    if (not 0<=mid<len(data)) or len(topping_1) ==0 or len(topping_2)==0:
        return #범위에 벗어나면 탐색 끝
    if len(set(topping_1)) == len(set(topping_2)):
        print(answer)
        answer+=1 # hit -> 왼 + 오 이동
        search(data,mid-len(topping_1)//2) # 오른쪽 더 길게
        search(data, mid + len(topping_2)//2) # 왼쪽 더 길게
    elif len(set(topping_1)) > len(set(topping_2)): #오른쪽 이동
        search(data, mid - len(topping_1) // 2)
    elif len(set(topping_1)) < len(set(topping_2)): #왼쪽 이동
        search(data, mid + len(topping_2) // 2)

print(solution([1, 2, 1, 3, 1, 4, 1, 2]	))