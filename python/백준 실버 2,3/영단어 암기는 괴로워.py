

## 1. 자주 나오는 단어는 앞 배치
## 2. 단어의 길이기 길수록 앞에 배치
## 3. 알파벳 사전 순으로 앞에 배치

## 길이가 M 이상인 경우만 외움

import sys
input = sys.stdin.readline
n,m = map(int,input().split())

words = dict() # 이름 [ # 횟수, 길이, 이름]

for i in range(n):
    word = input().strip()
    if len(word) < m:
        continue
    if word in words:
        words[word][0]-=1
    else:
        words[word] = [100001,10-len(word),word]

for word in sorted(words.values()):
    print(word[2])

