

# 성 지키키


# 열 기준으로 가드 카운트 함수
def find(list,num):
    result = 0
    for i in range(num):
        if list[i].count('X')==0:
            result+=1
    return result

# 모든 행과 모든 열에 한 명 이상의 경비원이 필요
# 행 기준 * 열 기준으로 필요한 경비원 수를 계산 -> 더 큰 수를 출력
n , m = map(int,input().split())

array = []
for i in range(n):
    array.append(list(input()))


print(max(find(array,n),find(list(zip(*array)),m)))