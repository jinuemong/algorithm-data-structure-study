
# 튜플

d = {"one": 1 , "two" : 2, "three": 3}

print(d["one"])

# 삭제
del d['one']

print(d.keys())
print(d.values())
print(d.items())



# set
s = set('12l3j12l321j')
print(s) # 중복 없음

print(dir(s)) #함수 탐색

s.add('5')
print(s)
s.discard('5')
print(s)
s.update('5','4')
print(s)
# 존재 확인
print('5' in s)

## 간편 뭄ㄴ제
pan = {'a','b','c'}
da = {'a','b','d'}
print(pan.difference(da)) #차집합
print(pan.union(da))


# set의 사용
# 동물의 수 구하기
data = "고양이 개 사자 토끼 뱀 토끼 사자 고양이"
set_list = set(data.split())
dict = {}
for i in data.split():
    dict[i] = data.split().count(i)
print(set_list,dict)

data2 = '1 2 3 4 5 6 7'
print(data2.split())

# 문자를 바로 숫자로 변경

print([int(i) for i in data2.split()])

list(map(int, data2.split()))

#입력받기

n = int(input()) # 수 하나
print(n)
# 각 데이터 공백으로 구분하여 입력

data = list(map(int,input().split()))
print(data)
# 공백을 기준으로 적은 데이터 입력

a,b,c = map(int,input().split())
print(a,b,c)
# 빠른 입력

import sys

data = sys.stdin.readline().rstrip()
print(data)

dat = list(map(int,sys.stdin.readline().rstrip().split()))
print(dat)