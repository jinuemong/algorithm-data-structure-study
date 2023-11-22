
import itertools
import sys

input = sys.stdin.readline
n,k = list(map(int,input().split()))

def sol(n,k):
    first = {'a', 'c', 't', 'n', 'i'}
    teach_word_count = k - len(first)
    if teach_word_count < 0: teach_word_count = 0
    uniqueList = []
    uniqueSet = set()
    cnt = 0
    for _ in range(n):
        data = set(list(input().strip())) - first
        if len(data) > teach_word_count:
            continue
        if len(data) > 0: # 6글자 이상
            uniqueList.append(data)
            uniqueSet = uniqueSet | data
        else:
            cnt+=1

    if k<len(first):
        return 0

    if len(uniqueList) == 0:
        return

    if len(uniqueSet) <= teach_word_count:
        return cnt + len(uniqueList)


    max_cnt = 0
    for case in itertools.combinations(uniqueSet, teach_word_count):
        caseCnt = 0
        caseSet = set(case)
        for candidateSet in uniqueList:
            if candidateSet.issubset(caseSet):
                caseCnt+=1
        max_cnt = max(max_cnt,caseCnt)
    cnt+=max_cnt
    return cnt



print(sol(n,k))