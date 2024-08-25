# 리스트 컴프리헨션

array = [i for i  in range(20) if i % 2 == 1]

print(array)


# 2차원 초기화 : 잘못 된 경우
# 내부적으로 3개 리스트 모두 동일한 객체에 대한 래퍼런스로 인식
# n 행 m 열
n = 3
m = 4

array = [[0]*m] * n
print(array)

array[1][1] = 5
print(array)

# 정상적인 2차원 초기화

array = [[0] * m for _ in range(n)]
print(array)

array[1][1] = 5
print(array)

# 리스트 함수 정리

a = [1,4,3]

# append() O(1)

a.append(2)

# sort()

a.sort()
a.sort(reverse=True)

# reverse()

a.reverse()
a.reverse()

# insert() O(N)
# 특정 원소에 추가

a.insert(2,3)

# count()
# 특정 값 세기
a.count(3)

# remove() O(N)
# 특정 값 삭제

a.remove(1)

## remove는 큰 시간 복잡도를 가짐
## set을 활용하는 것이 좋음

a = [1,2,3,4,5,5,5]
remove_set = {3,5}

result = [i for i in a if i not in remove_set]
# [넣을 값 for 넣을 값 in 리스트 if 조건문]
print(result)


data = list(zip(['a','b','c','d'],[1,2,3,4],"ABCD"))
# zip
print(data)
print(sorted(data,key=lambda x:x[0])) #0 번 인덱스로 정렬
print(sorted(data,key=lambda x:x[1])) #1 번 인덱스로 정렬
print(sorted(data,key=lambda x:x[2])) #2 번 인덱스로 정렬

# sorted
print(sorted(["11","22","333","4444","555"],key=len,reverse=True))
print(sorted(["11","22","333","4444","555"],key=str,reverse=True))