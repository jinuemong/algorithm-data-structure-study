#출처 : https://school.programmers.co.kr/learn/courses/30/lessons/81303

def solution(n, k, cmd):
    answer = ['O' for _ in range(1, n + 1)]
    k += 1
    linked_list = {i: [i - 1, i + 1] for i in range(1, n + 1)}
    del_list = []
    # 앞뒤로 연결한 링크드 리스트 구현

    for c in cmd:
        if c[0] == "U":
            for _ in range(int(c[2:])):  # 앞으로 이동
                k = linked_list[k][0]
        elif c[0] == "D":
            for _ in range(int(c[2:])):  # 뒤로 이동
                k = linked_list[k][1]
        elif c[0] == "C":  # 삭제
            prev, next = linked_list[k]
            del_list.append([k, prev, next])  # 노드 채로 담기
            answer[k - 1] = 'X'

            if next == n+1:
                k = linked_list[k][0]  # 마지막일 경우 이전
            else:
                k = linked_list[k][1]  # 마지막이 아니면 다음

            if prev == 0:  # 이전이 0이면 뒤만 연결
                linked_list[next][0] = prev
            elif next == n + 1:  # 다음이 마지막이면 다음만 연결
                linked_list[prev][1] = next
            else:  # 그 외는 양쪽 연결
                linked_list[next][0] = prev
                linked_list[prev][1] = next

        elif c[0] == "Z":  # 복구
            current, prev, next = del_list.pop()  # 최근 삭제 복구
            answer[current - 1] = 'O'

            if prev == 0:  # 맨 앞에 복구
                linked_list[next][0] = current
            elif next == n + 1:  # 맨 뒤에 복구
                linked_list[prev][1] = current
            else:  # 중간에 복구
                linked_list[next][0] = current
                linked_list[prev][1] = current

    return "".join(answer)

n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
print(solution(n, k, cmd))
