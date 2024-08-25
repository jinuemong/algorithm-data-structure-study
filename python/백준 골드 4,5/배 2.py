

# 배 2트

# 최대값 순으로 정렬
# 최대값 순으로 내보내기
# 전체 내보낸 횟수 만큼 카운트
# 더 이상 내보낼 수 없으면 종료

import sys; input = sys.stdin.readline
def solve():
    n = int(input())
    cranes = sorted(list(map(int, input().split())),reverse=True)
    m = int(input())
    boxes = sorted(list(map(int, input().split())),reverse=True)
    result= 0

    if cranes[0]< boxes[0]: return -1
    while boxes:
        check_box,next_box = [], []
        if len(boxes)>=n:
            check_box = boxes[:len(cranes)]
            boxes = boxes[len(cranes):]
        else:
            check_box = boxes[:len(boxes)]
            boxes = []
        for i in range(len(check_box)):
            if check_box[i] > cranes[i]:
                next_box.append(check_box[i])

        boxes = next_box+boxes
        result+=1
    return result

print(solve())