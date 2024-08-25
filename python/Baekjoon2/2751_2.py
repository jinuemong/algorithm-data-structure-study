# 2. 병합 정렬 사용

# -> 분할 정복 방식을 사용
# -> 절반씩 합치면서 정렬하면 전체 리스트가 정렬
# -> O(NlogN) 시간 복잡도를 보장

# - 병합할 때는 리스트의 앞 원소부터 차례대로 채워 넣음

# step1> i=0,j=0,k=0  [ i : 리스트 1, j : 리스트 2, k : 정렬 리스트 ]
# 2가지 리스트 {[5,7] , [4,8] }일 때 5와 4를 비교
# 정렬 리스트 : [4,5] <- {[,7] , [,8] }

# step2> i=1,j=1,k=2  [ i : 리스트 1, j : 리스트 2, k : 정렬 리스트 ]
# 정렬 리스트 : [4,5,7,8] <- {[,] , [,] }

def merge_sort(array):
    if len(array) <=1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i,j,k = 0,0,0
    while i< len(left) and j < len(right):
        if left[i]<right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1

    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array = merge_sort(array)

for data in array:
    print(data)