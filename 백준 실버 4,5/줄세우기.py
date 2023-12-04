
# 항상 20명
# 서로 다른 키
# 학생들의 뒤로 물러난 횟수를 구하라
# 각 자리르 찾아가고, 그 자리만 큼 자리수를 체크

import sys
input = sys.stdin.readline

for i in range(int(input())):
    count = 0
    stack = []
    students = list(map(int,input().split()))[1:]
    for student in students:
        count+=len([data for data in stack if data>student])
        stack.append(student)
    print(i+1,count)