
## 원형이므로 deque를 활용한다
# 문자열을 돌려가며 다른 수가 나왔을 경우 변환한다
# ex aabbaaabaaba
## 회전 bbaaabaab pop (aaa)
## b가 나왔으므로 b를 모두 뺀다 aaabaab pop(aaa) pop(bb)
## 둘을 바꿔서 넣는다 (1)
## aaabaabbbaaa
## 이어서  앞뒤로 a를 모두 뺀다
### baabbbaaa pop(aaa)
### b를 모두 뺀다

### 다시  ( 원형 적용 )

### ex aabbaaabaaba
### a가 나올때까지 화전한다
### 현재 a 로 시작하므로 그대로 진행

#(회전 1)
### 앞뒤로 a인경우 모두 뺀다
### bbaaabaab pop(aaa)
### 앞뒤로 b인 경우 모두 뺀다
### aaabaa pop(aaa) pop(bbb)
### 바꿔서 넣는다
### aaabaaaaabbb

# (회전 2)
### 반복한다
### 앞뒤로 a를 모두 뺀다
### baaaaabbb pop(aaa)
### 앞뒤로 b를 모두 뺀다
### aaaaa pop(aaa) pop(bbbb)
### 바꿔서 넣는다
### aaaaaaaabbbb

# (회전 취소)
### 반복한다
### 앞뒤로 a를 모두 뺀다
### 총 a의 개수와 같으므로 멈춘다

## 회전 수를 출력한다 - > 2

from collections import deque

a_queue = []
b_queue = []

data = deque(list(input()))
a_len = data.count("a")
count = 0
while True:
    if a_len == len(data): break
    while data[-1]=="a":
        data.appendleft(data.pop())
    while data[0]=="a":
        a_queue.append(data.popleft())
    if a_len == len(a_queue):
        break
    while data[-1]=="b":
        data.appendleft(data.pop())
    while data[0]=="b":
        b_queue.append(data.popleft())
    data.extend(a_queue+b_queue)
    a_queue, b_queue = [],[]
    count+=1

print(count)