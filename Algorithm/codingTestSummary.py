
# 큰 따옴표, 작은따옴표 출력
print("\"")
print("\'")

# 문자열 인덱싱
a = "hello"
for i in a:
    print(i,end=", ")

# 문자열 슬라이싱
print(a[0:3])
print(a[:-1])

# ! 파이썬에서 문자열은 값을 변경할 수 없음 -> 불변 객체

# 리스트는 가변 객체
# 리스트 덧셈
a = [1,2,3]
b = [4,5,6]
c= a+b
print(c)

# 리스트 컴프리헨션

arr = [5] * 8
print(arr)

#4 * 5 크기의 배열
arr = [[0]*5 for _ in range(4)]
print(arr)

# 4 * 5 를 순서대로 초기화
arr = [[i*5 + j for j in range(5)] for i in range(4)]
print(arr)

# 사전 : 딕셔너리 자료형
data = {}
data[1] = "1"
data[2] = "2"
print(data)
for key,data in data.items():
    print(key,data)

# 딕셔너리를 활용한 갯수 세기
data =  [1,2,3,4,5,1,2,3,5,6]
count = {}

for x in data:
    if x not in count:
        count[x] = 1
    else:
        count[x]+=1
print(count)

# 집합 : set 자료형
# 데이터의 중복을 허용하지 않고 순서가 상관없을 때 사용
data = [1,2,3,5,4,3,1,4]
print(set(data))

visited = set()

for x in data:
    if x not in visited:
        visited.add(x)
    else:
        print("이미 있는 원소 :",x)
print(visited)

# enumerate를 활용해서 인덱스와 함께 반복
data_list = [1,2,3]
for i, data in enumerate(data_list):
    print(i,data)

# 코딩 테스트에서 자주 사용되는 라이브러리

data = [7,2,5,4,1]
print(sum(data))
print(min(data))
print(max(data))
print(sorted(data))

# 순열
from  itertools import  permutations,combinations

arr = ["a","b","c"]
# 2개씩 묶기
result = list(permutations(arr,2))
print(result)

# 조합
result = list(combinations(arr,2))
print(result)

# 중복 순열 - 중복을 포함해서 두개 선택
from itertools import product

result = list(product(arr,repeat=2))
print(result)

# 중복 조합 - 중복을 포함해서 조합 선택
from itertools import combinations_with_replacement

result = list(combinations_with_replacement(arr,2))
print(result)

# 우선 순위 큐를 활용한 힙
import heapq
arr = [1,5,2,8,9,7,4,3,6]
heap = []
result = []

for x in arr:
    heapq.heappush(heap,x)
for i in range(len(heap)):
    x = heapq.heappop(heap)
    result.append(x)
print(result)

# 원하는 문자열 출력 : f- string

score = 70
print(f"학생의 점수는 {score} 입니다")